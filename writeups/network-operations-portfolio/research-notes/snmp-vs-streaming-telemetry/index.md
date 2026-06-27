---
layout: page-toc
title: "SNMP vs Streaming Telemetry"
permalink: /writeups/network-operations-portfolio/research-notes/snmp-vs-streaming-telemetry/
toc: true
---

# SNMP vs Streaming Telemetry — Giám sát Mạng từ Pull sang Push

> **Đối tượng:** Network/IP Engineer định hướng Automation và AI/Big Data, muốn nắm vững nền tảng thu thập dữ liệu mạng hiện đại — từ SNMP truyền thống đến Streaming Telemetry real-time.
>
> **Mức độ:** Intermediate — giả định bạn đã quen với các khái niệm cơ bản về network management và muốn hiểu sâu về lý do và cách chuyển đổi sang telemetry.

---

## Mục lục

1. [Bối cảnh và tầm quan trọng của dữ liệu giám sát](#1-bối-cảnh-và-tầm-quan-trọng-của-dữ-liệu-giám-sát)
2. [SNMP — Mô hình Pull truyền thống](#2-snmp--mô-hình-pull-truyền-thống)
3. [Giới hạn của SNMP ở scale lớn](#3-giới-hạn-của-snmp-ở-scale-lớn)
4. [Streaming Telemetry — Mô hình Push hiện đại](#4-streaming-telemetry--mô-hình-push-hiện-đại)
5. [YANG Data Model — nền tảng dữ liệu structured](#5-yang-data-model--nền-tảng-dữ-liệu-structured)
6. [gNMI và gRPC — transport layer của Telemetry](#6-gnmi-và-grpc--transport-layer-của-telemetry)
7. [So sánh chi tiết SNMP vs Streaming Telemetry](#7-so-sánh-chi-tiết-snmp-vs-streaming-telemetry)
8. [Phân tích số liệu: Scale 1000 thiết bị](#8-phân-tích-số-liệu-scale-1000-thiết-bị)
9. [Telemetry Pipeline — từ thiết bị đến dashboard](#9-telemetry-pipeline--từ-thiết-bị-đến-dashboard)
10. [OpenConfig — chuẩn hóa YANG model](#10-openconfig--chuẩn-hóa-yang-model)
11. [Ứng dụng AI/ML và Automation](#11-ứng-dụng-aiml-và-automation)
12. [Triển khai thực tế: Lộ trình chuyển đổi](#12-triển-khai-thực-tế-lộ-trình-chuyển-đổi)
13. [Lab mini: gNMI subscribe thực hành](#13-lab-mini-gnmi-subscribe-thực-hành)
14. [Glossary](#14-glossary)
15. [Tài liệu tham khảo](#15-tài-liệu-tham-khảo)

---

## 1. Bối cảnh và Tầm quan trọng của Dữ liệu Giám sát

### Dữ liệu là nền tảng của Automation và AI

Mạng càng lớn và phức tạp, dữ liệu giám sát càng trở thành tài sản chiến lược. Xu hướng hiện đại trong network operations đòi hỏi:

- **Closed-loop automation:** phát hiện sự cố → phân tích → tự động khắc phục, không cần người thao tác
- **AI/ML anomaly detection:** nhận biết bất thường trước khi thành sự cố
- **Capacity planning chính xác:** dự đoán khi nào link/thiết bị đạt ngưỡng, không chờ đến lúc nghẽn
- **SLA assurance real-time:** đảm bảo cam kết dịch vụ với data liên tục, không phải định kỳ

Tất cả những điều này đều yêu cầu **dữ liệu chất lượng cao, độ phân giải cao, real-time**. SNMP — ra đời năm 1988 — không được thiết kế cho thế giới này. Streaming Telemetry được.

### Sự chuyển dịch mô hình

```
Thế hệ 1 (1988 - ~2010): SNMP polling
  NMS hỏi → Thiết bị trả lời → Lặp lại mỗi 5 phút
  Giám sát cơ bản, đủ cho mạng vài trăm node

Thế hệ 2 (~2010 - 2016): SNMP cải tiến + Syslog + NetFlow
  Thêm syslog tập trung, NetFlow/IPFIX cho traffic analysis
  Vẫn chủ yếu pull model, thêm event-driven với trap

Thế hệ 3 (~2016 - nay): Streaming Telemetry + YANG + gNMI
  Thiết bị chủ động push dữ liệu structured
  Tích hợp vào big data pipeline, AI/ML
  Mạng backbone lớn (Google, Facebook, các ISP tier-1) tiên phong
  
Thế hệ 4 (emerging): Intent-Based Networking + AI-Ops
  Telemetry là input, AI là engine, automation là output
  Mạng tự vận hành, tự tối ưu
```

---

## 2. SNMP — Mô hình Pull Truyền thống

### Lịch sử và kiến trúc

SNMP (Simple Network Management Protocol) được định nghĩa trong RFC 1157 (1988). Mục tiêu ban đầu: một giao thức đơn giản để quản lý thiết bị mạng từ xa.

**Hai mô hình hoạt động song song:**

```
1. POLLING (Request-Response):

    ┌──────────────────┐                        ┌──────────────────┐
    │   NMS/Manager    │                        │  Network Device  │
    │  (e.g. Zabbix,   │                        │  (Agent chạy     │
    │   LibreNMS,      │                        │   SNMP daemon)   │
    │   Nagios)        │                        │                  │
    │                  │─── GetRequest ────────►│                  │
    │                  │    (OID: 1.3.6.1.2...) │                  │
    │                  │◄── GetResponse ─────── │                  │
    │                  │    (value: 95%)         │                  │
    │                  │                        │                  │
    │  (60 giây sau)   │                        │                  │
    │                  │─── GetRequest ────────►│                  │
    │                  │◄── GetResponse ─────── │                  │
    └──────────────────┘                        └──────────────────┘

    Đặc điểm: NMS chủ động, thiết bị bị động. Lặp lại vô tận.

2. TRAP (Event-driven, bất đồng bộ):

    ┌──────────────────┐                        ┌──────────────────┐
    │   NMS/Manager    │                        │  Network Device  │
    │                  │◄── Trap (UDP 162) ──── │                  │
    │                  │    "Link down on       │                  │
    │                  │     GigE0/0/1"         │                  │
    └──────────────────┘                        └──────────────────┘

    Đặc điểm: Thiết bị chủ động gửi khi có sự kiện.
    Nhược điểm: UDP → không đảm bảo delivery. Trap có thể bị mất.
    SNMPv2c Inform: thêm acknowledgment, nhưng vẫn UDP.
```

### MIB và OID — cấu trúc dữ liệu SNMP

**MIB (Management Information Base):** là tập hợp các object được định nghĩa, mỗi object có một OID (Object Identifier) duy nhất.

**OID:** chuỗi số phân cấp, dạng `1.3.6.1.2.1.x.y.z`, đại diện cho một metric cụ thể.

```
Cây OID (rút gọn):

iso(1)
 └─ org(3)
      └─ dod(6)
           └─ internet(1)
                └─ mgmt(2)
                     └─ mib-2(1)
                          ├─ system(1)       → thông tin system
                          ├─ interfaces(2)   → interface counters
                          │    └─ ifTable(2)
                          │         └─ ifEntry(1)
                          │              ├─ ifDescr(2)         → "GigabitEthernet0/0/1"
                          │              ├─ ifSpeed(5)         → 1000000000 (bps)
                          │              ├─ ifInOctets(10)     → bytes received
                          │              ├─ ifOutOctets(16)    → bytes sent
                          │              ├─ ifInErrors(14)     → input errors
                          │              └─ ifOperStatus(8)    → 1=up, 2=down
                          ├─ ip(4)           → IP statistics
                          └─ tcp(6)          → TCP statistics

Ví dụ OID đầy đủ:
  ifInOctets cho interface đầu tiên = 1.3.6.1.2.1.2.2.1.10.1
                                       ↑ mib-2 ↑ ifTable ↑ index
```

**Vấn đề với OID:** đây là số, không phải text. Cần map OID → tên có nghĩa thông qua MIB file. NMS phải load MIB, parse, rồi mới hiểu dữ liệu.

### Các phiên bản SNMP

| Phiên bản | Năm | Bảo mật | Ghi chú |
|---|---|---|---|
| SNMPv1 | 1988 | Community string (plaintext) | RFC 1157, cực kỳ cơ bản |
| SNMPv2c | 1996 | Community string (plaintext) | Thêm GetBulk, Inform; vẫn không mã hóa |
| SNMPv3 | 2002 | Authentication + Encryption | RFC 3410-3418; nên dùng |

**SNMPv3 security model:**
- **Authentication:** HMAC-MD5 hoặc HMAC-SHA (đảm bảo integrity, chống giả mạo)
- **Privacy (Encryption):** DES hoặc AES-128/256 (mã hóa payload)
- **Access Control:** VACM (View-based Access Control Model) — phân quyền chi tiết

```
SNMPv3 User configuration (Cisco IOS):
  snmp-server group MONITORING v3 priv read MIBVIEW
  snmp-server user collector MONITORING v3
    auth sha AuthPassword123
    priv aes 128 PrivPassword456
  snmp-server view MIBVIEW interfaces included
  snmp-server view MIBVIEW ip included
```

> **Thực tế vận hành:** SNMPv1/v2c vẫn phổ biến vì dễ cấu hình, nhưng community string `public` hay `private` đi qua network plaintext là lỗ hổng bảo mật nghiêm trọng. Bất kỳ mạng production nào cũng nên dùng SNMPv3 hoặc chuyển sang Telemetry.

---

## 3. Giới hạn của SNMP ở Scale Lớn

### Vấn đề 1: Độ phân giải thời gian

Chu kỳ poll SNMP điển hình: 60–300 giây. Trong khoảng thời gian đó, rất nhiều sự kiện có thể xảy ra và biến mất:

```
Timeline 60 giây:

t=0s    Poll 1 → ifInErrors = 1,000
        │
t=5s    Link flap xảy ra (interface down/up trong 200ms)
        Micro-burst traffic: link đạt 100% utilization trong 3 giây
        Error counter tăng vọt
        │
t=60s   Poll 2 → ifInErrors = 1,850
                  ifInOctets tăng bình thường

NMS thấy gì? Counter tăng thêm 850 errors. Không biết lúc nào, không biết
interface có flap không. Không biết có micro-burst không.

Với Telemetry ở 1s interval:
  t=0s:   errors=1000, status=up, util=45%
  t=1s:   errors=1000, status=up, util=46%
  t=5s:   status=DOWN ← alert ngay lập tức!
  t=5.2s: status=UP ← recovered, biết được duration 200ms
  t=6s:   errors=1120, util=98% ← micro-burst detected!
  t=7s:   errors=1340, util=100% ← sustained high util
  t=10s:  errors=1850, util=47% ← burst ended
```

### Vấn đề 2: Tải CPU và băng thông khi scale

SNMP poll là synchronous: với mỗi OID, NMS gửi GetRequest, chờ GetResponse, rồi mới poll OID tiếp theo (hoặc dùng GetBulk để hỏi nhiều OID một lần, nhưng vẫn bị giới hạn).

```
Bài toán scale:
  - 1,000 thiết bị
  - Mỗi thiết bị: 48 interface × 10 counter = 480 interface OID
                   + 50 system OID (CPU, memory, BGP, v.v.)
                   = ~530 OID/thiết bị
  - Poll interval: 60 giây

Số lượng GetRequest/Response mỗi giây:
  1,000 × 530 / 60 ≈ 8,833 requests/giây

Vấn đề:
  1. CPU thiết bị: SNMP agent chạy trên CPU control plane
                   → cạnh tranh với routing protocols (OSPF, BGP)
                   → trên mạng busy, SNMP response có thể bị delay/drop
  
  2. NMS bottleneck: NMS phải xử lý 8,833 response/giây, parse MIB,
                     correlate, lưu DB → NMS dễ trở thành bottleneck
  
  3. Thực tế: nhiều NMS buộc giãn poll interval ra 300s hoặc hơn
              → mất độ phân giải, mất visibility
```

### Vấn đề 3: Dữ liệu không structured

OID là số. MIB là text. Parsing MIB để hiểu dữ liệu không chuẩn hóa, phụ thuộc vendor:

```
Cisco: sysDescr.0 = "Cisco IOS Software, Version 15.6(3)M..."
Juniper: sysDescr.0 = "Juniper Networks, Inc. mx480 ..."
Nokia: sysDescr.0 = "TiMOS-B-20.2.R1..."

→ Mỗi vendor có MIB riêng, OID riêng cho cùng một metric
→ NMS phải có MIB riêng cho từng vendor/thiết bị
→ Khi thêm vendor mới: import MIB, test, v.v.

Ví dụ: BGP peer state
  Cisco IOS: 1.3.6.1.2.1.15.3.1.3 (standard MIB)
             1.3.6.1.4.1.9.9.187... (Cisco proprietary MIB)
  Juniper:   1.3.6.1.4.1.2636.5... (Juniper proprietary)
  
→ Không có schema chuẩn, khó integrate vào Big Data pipeline
```

### Vấn đề 4: Security gaps

- SNMPv1/v2c: community string đi cleartext trên network → sniff được
- Không có encryption, không có per-user access control
- Trap không có xác thực → dễ bị forge
- SNMPv3 giải quyết được, nhưng complex hơn nhiều để cấu hình

---

## 4. Streaming Telemetry — Mô hình Push Hiện đại

### Nguyên lý cơ bản: đảo ngược mô hình

Thay vì NMS đi hỏi từng thiết bị, trong Streaming Telemetry:

1. **Collector** gửi **subscription** đến thiết bị: "Tôi muốn nhận dữ liệu về X với tần suất Y"
2. **Thiết bị** chủ động **push** dữ liệu theo subscription
3. **Dữ liệu có cấu trúc** (YANG model) → không cần parse MIB
4. **Transport an toàn** (TLS/gRPC) mặc định

```
Flow tổng quát:

┌──────────────────────────────────────────────────────────────────────┐
│                        Streaming Telemetry Architecture              │
└──────────────────────────────────────────────────────────────────────┘

  Subscriber side                              Device side
  ┌─────────────┐                           ┌───────────────────────┐
  │             │──── gNMI Subscribe ──────►│  Subscription Manager │
  │  Collector  │     (path: /interfaces/   │                       │
  │  (e.g.,     │      interface[name=*]/   │  ┌─────────────────┐  │
  │  Telegraf,  │      state/counters,      │  │  Data Sampler   │  │
  │  Pipeline)  │      interval: 1s)        │  │  (every 1s,     │  │
  │             │                           │  │   collect all   │  │
  │             │◄═══ gRPC stream ══════════│  │   interface     │  │
  │             │◄═══ (protobuf, ~1s) ══════│  │   counters)     │  │
  │             │◄═══════════════════════════│  └─────────────────┘  │
  └─────────────┘                           │                       │
        │                                   │  ┌─────────────────┐  │
        ▼                                   │  │  On-Change      │  │
  ┌──────────┐                              │  │  Detector       │  │
  │  Kafka   │                              │  │  (BGP state,    │  │
  │  (buffer)│                              │  │   link status)  │  │
  └──────────┘                              │  └─────────────────┘  │
        │                                   └───────────────────────┘
        ▼
  ┌────────────────────────────────────┐
  │  Time-Series DB                    │
  │  (InfluxDB / Prometheus / TimescaleDB) │
  └────────────────────────────────────┘
        │
        ├──► Grafana (visualization)
        ├──► Alertmanager (alerting)
        └──► AI/ML Pipeline (anomaly detection)
```

### Hai chế độ subscription

**1. Sample (Periodic):** Đẩy data theo chu kỳ cố định, bất kể giá trị có thay đổi hay không.

```
Use case: Interface counters, CPU utilization, memory, traffic stats
Interval: 10s, 30s, 1s (tùy metric và thiết bị)

Ví dụ (pseudo):
  t=0:   {ifInOctets: 1,000,000, ifOutOctets: 800,000}
  t=1s:  {ifInOctets: 1,012,500, ifOutOctets: 810,200}
  t=2s:  {ifInOctets: 1,024,800, ifOutOctets: 821,100}
  ...
→ Granular enough để tính bandwidth utilization per-second
```

**2. On-Change:** Chỉ đẩy khi giá trị thay đổi.

```
Use case: BGP peer state, interface operational status, routing table changes
          (những thứ hiếm khi thay đổi nhưng quan trọng khi thay đổi)

Ví dụ:
  t=0:     {bgpPeerState: "Established"}   ← initial value
  (silence...không có gì thay đổi)
  t=3600:  {bgpPeerState: "Idle"}          ← BGP session drop! Push ngay
  t=3605:  {bgpPeerState: "Active"}        ← Attempting reconnect
  t=3618:  {bgpPeerState: "Established"}   ← Recovered

→ Không tốn bandwidth lúc bình thường
→ Alert ngay khi thay đổi, không đợi poll interval
```

---

## 5. YANG Data Model — Nền tảng Dữ liệu Structured

### YANG là gì?

**YANG (Yet Another Next Generation)** — RFC 6020/7950 — là ngôn ngữ mô hình hóa dữ liệu cho configuration và operational state của thiết bị mạng.

YANG giải quyết vấn đề lớn nhất của SNMP: **thiếu schema chuẩn hóa**. Với YANG, mọi thứ được định nghĩa rõ ràng: tên field, kiểu dữ liệu, hierarchy, relationship.

```
So sánh:

SNMP MIB (kiểu cũ):
  OID: 1.3.6.1.2.1.2.2.1.10.1 = 1234567890
  Hỏi: Con số này là gì? Phải tra MIB mới biết là ifInOctets, interface index 1
  Kiểu dữ liệu: Counter32 (số nguyên 32-bit, rollover sau 4GB)
  Không có context về đơn vị, không có relationship

YANG model (hiện đại):
  /interfaces/interface[name=GigabitEthernet0/0/1]/state/counters/in-octets
  Value: 1234567890
  → Tên tự mô tả: "in-octets" của interface "GigabitEthernet0/0/1"
  → Kiểu: uint64 (không rollover sớm)
  → Có schema, có validation
```

### Ví dụ YANG module (OpenConfig)

```yang
// openconfig-interfaces.yang (rút gọn)

module openconfig-interfaces {
  namespace "http://openconfig.net/yang/interfaces";

  container interfaces {
    list interface {
      key "name";
      
      leaf name {
        type string;         // e.g., "GigabitEthernet0/0/1"
      }
      
      container state {
        leaf admin-status {
          type enumeration {
            enum UP;
            enum DOWN;
            enum TESTING;
          }
        }
        
        leaf oper-status {
          type enumeration {
            enum UP;
            enum DOWN;
            // ...
          }
        }
        
        container counters {
          leaf in-octets {
            type yang:counter64;    // 64-bit, không rollover
          }
          leaf out-octets {
            type yang:counter64;
          }
          leaf in-errors {
            type yang:counter64;
          }
          leaf in-discards {
            type yang:counter64;
          }
          // ...
        }
      }
    }
  }
}
```

**Điểm mạnh của YANG:**
- **Self-documenting:** tên path mô tả ý nghĩa
- **Strongly typed:** uint64, string, enum, boolean → validate trước khi dùng
- **Hierarchical:** reflect đúng cấu trúc dữ liệu (interface → sub-interface → IP)
- **Vendor-neutral khi dùng OpenConfig:** một model, nhiều vendor
- **Machine-readable:** code có thể generate tự động từ YANG schema

### Encoding: JSON vs Protobuf

Dữ liệu YANG có thể encode theo nhiều format:

```
JSON (human-readable):
{
  "openconfig-interfaces:interfaces": {
    "interface": [{
      "name": "GigabitEthernet0/0/1",
      "state": {
        "oper-status": "UP",
        "counters": {
          "in-octets": 1234567890,
          "out-octets": 987654321,
          "in-errors": 0
        }
      }
    }]
  }
}
Size: ~200 bytes cho ví dụ này

Protobuf (binary, compact):
  Field 1 (name): "GigabitEthernet0/0/1"
  Field 2 (oper-status): 1 (enum UP)
  Field 3 (in-octets): 1234567890
  ...
Size: ~40 bytes (tiết kiệm ~80%)
Parse speed: 5-10x nhanh hơn JSON

→ Production telemetry thường dùng protobuf để giảm bandwidth và tăng throughput
→ Debug/development thường dùng JSON vì readable
```

---

## 6. gNMI và gRPC — Transport Layer của Telemetry

### gRPC là gì?

**gRPC (gRPC Remote Procedure Call)** — do Google phát triển, open-source — là framework RPC hiện đại dựa trên:
- **HTTP/2:** multiplexing nhiều stream trên 1 connection, header compression
- **Protocol Buffers (protobuf):** serialization format compact và nhanh
- **TLS:** encryption mặc định

gRPC cho phép client gọi function trên server như gọi local, nhưng thực ra đi qua network.

### gNMI — gRPC Network Management Interface

**gNMI (gRPC Network Management Interface)** — được OpenConfig community định nghĩa — là giao thức cụ thể dùng gRPC để:
- **Get:** lấy một lần dữ liệu tại thời điểm hiện tại
- **Set:** cấu hình thiết bị (thay thế CLI/NETCONF cho config push)
- **Subscribe:** đăng ký nhận stream dữ liệu liên tục
- **Capabilities:** hỏi thiết bị hỗ trợ những YANG model nào

```
gNMI Subscribe request (pseudo-protobuf):

SubscribeRequest {
  subscribe {
    prefix {
      path_element { name: "interfaces" }
    }
    subscription [
      {
        path {
          path_element { name: "interface" key { name: "*" } }
          path_element { name: "state" }
          path_element { name: "counters" }
        }
        mode: SAMPLE        // hoặc ON_CHANGE
        sample_interval: 1000000000  // 1 giây (nanoseconds)
      },
      {
        path {
          path_element { name: "interface" key { name: "*" } }
          path_element { name: "state" }
          path_element { name: "oper-status" }
        }
        mode: ON_CHANGE     // chỉ push khi thay đổi
      }
    ]
    encoding: PROTO         // hoặc JSON_IETF
  }
}
```

**gNMI Subscribe response (stream):** thiết bị gửi liên tục các `SubscribeResponse`:

```
SubscribeResponse {
  update {
    timestamp: 1719446400000000000  // nanoseconds since epoch
    prefix { path_element { name: "interfaces" } }
    update [
      {
        path { ... "GigabitEthernet0/0/1" ... "in-octets" }
        val { uint_val: 1234567890 }
      },
      {
        path { ... "GigabitEthernet0/0/1" ... "out-octets" }
        val { uint_val: 987654321 }
      }
      // ... tất cả interface counters trong 1 response
    ]
  }
}
```

### NETCONF vs gNMI

Một số vendor cũng hỗ trợ **NETCONF** (RFC 6241) + **YANG** cho telemetry, sử dụng:
- **NETCONF:** XML-based, SSH transport, mature nhưng verbose
- **RESTCONF:** REST API, JSON/XML, dễ tích hợp với web tools

| Tiêu chí | gNMI/gRPC | NETCONF | RESTCONF |
|---|---|---|---|
| Transport | HTTP/2 (gRPC) | SSH | HTTP/1.1 hoặc HTTP/2 |
| Encoding | Protobuf / JSON | XML | JSON / XML |
| Streaming | Native (subscribe) | Event notification (RFC 5277) | Server-Sent Events |
| Performance | Tốt nhất | Trung bình | Trung bình |
| Vendor support | IOS-XR, NX-OS, Junos, EOS | Rộng rãi | Rộng rãi |

---

## 7. So sánh Chi tiết SNMP vs Streaming Telemetry

### Bảng so sánh toàn diện

| Tiêu chí | SNMPv2c | SNMPv3 | Streaming Telemetry (gNMI) |
|---|---|---|---|
| **Mô hình** | Pull (polling) | Pull (polling) | Push (streaming) |
| **Transport** | UDP 161/162 | UDP 161/162 | TCP + TLS (gRPC) |
| **Reliability** | Unreliable (UDP) | Unreliable (UDP) | Reliable (TCP) |
| **Bảo mật** | Community string (plaintext) | Auth + Encrypt | TLS mặc định |
| **Mô hình dữ liệu** | OID / MIB | OID / MIB | YANG (structured) |
| **Encoding** | BER/ASN.1 (binary) | BER/ASN.1 | Protobuf / JSON |
| **Schema** | Implicit (MIB file) | Implicit (MIB file) | Explicit (YANG) |
| **Chu kỳ dữ liệu** | 60–300 giây | 60–300 giây | 100 ms – 10 giây |
| **Latency phát hiện** | Phút | Phút | Giây / dưới giây |
| **Event detection** | Trap (UDP, unreliable) | Inform (acknowledged) | On-Change (TCP, reliable) |
| **CPU tải thiết bị** | Cao khi scale | Cao khi scale | Thấp hơn (push model) |
| **Tải NMS/Collector** | Tăng tuyến tính với device | Tương tự v2c | Phân tán được qua Kafka |
| **Phù hợp AI/Big Data** | Hạn chế | Hạn chế | Tốt nhất |
| **Multi-vendor** | Khó (MIB khác nhau) | Khó | Tốt (OpenConfig chuẩn hóa) |
| **Hỗ trợ thiết bị cũ** | Rất rộng | Rộng | Chỉ thiết bị/OS mới |
| **Năm ra đời** | 1996 | 2002 | 2016+ |
| **Độ phức tạp setup** | Thấp | Trung bình | Cao hơn |

### Khi nào dùng gì?

```
Dùng SNMP khi:
  ✓ Thiết bị cũ không hỗ trợ gNMI/telemetry
  ✓ Giám sát cơ bản (up/down, bandwidth thô) đủ
  ✓ Infrastructure nhỏ, team không có telemetry expertise
  ✓ Legacy NMS đã invest (Zabbix, Cacti, LibreNMS, MRTG)

Dùng Streaming Telemetry khi:
  ✓ Cần độ phân giải giây hoặc dưới giây
  ✓ Scale lớn (100+ thiết bị quan trọng)
  ✓ Input cho AI/ML anomaly detection
  ✓ Closed-loop automation
  ✓ Multi-vendor cần chuẩn hóa (OpenConfig)
  ✓ Thiết bị hỗ trợ: IOS-XR 6.3+, NX-OS 9.2+, Junos 18.1+, EOS 4.21+
```

---

## 8. Phân tích Số liệu: Scale 1,000 Thiết bị

### Kịch bản so sánh định lượng

**Setup:**
- 1,000 thiết bị mạng (router, switch lõi)
- Mỗi thiết bị: 48 interface vật lý + 200 sub-interface/logical
- Mỗi interface: 10 counter (in/out octets, packets, errors, drops) = ~500 OID/device
- Thêm: CPU, memory, BGP peers, OSPF state = ~50 OID nữa
- Tổng: ~550 OID/thiết bị
- Mục tiêu: độ phân giải **1 giây**

### SNMP Analysis

```
Tính toán yêu cầu SNMP:

Requests cần thiết (với GetBulk, mỗi request ~30 OID):
  550 OID / 30 = ~19 GetBulk requests/thiết bị
  1,000 thiết bị × 19 requests = 19,000 GetBulk requests mỗi giây

Bandwidth (mỗi GetBulk response ~1,500 bytes UDP):
  19,000 × 1,500 bytes = 28.5 MB/giây = ~228 Mbps
  (chỉ cho management traffic!)

Thực tế: NMS thường không xử lý nổi tốc độ này
→ Giải pháp thực tế: giãn interval ra 60s hoặc 300s
→ Hệ quả: mất độ phân giải 1 giây, chỉ có 1/60 hoặc 1/300 dữ liệu mong muốn

CPU thiết bị: SNMP agent chạy trên control plane CPU
  → Trên router đang busy (nhiều BGP update, OSPF SPF), SNMP response delay
  → Timeout xảy ra → NMS đánh dấu "data missing" → gap trong đồ thị
```

### Telemetry Analysis

```
Với Streaming Telemetry (protobuf):

Thiết bị gom tất cả 550 giá trị vào 1 message protobuf mỗi giây:
  550 fields × ~8 bytes/field (uint64) + overhead ≈ ~6,000 bytes/message
  
Băng thông:
  1,000 thiết bị × 6,000 bytes/giây = 6 MB/giây = ~48 Mbps
  (giảm ~5x so với SNMP bandwidth)

Đặc biệt: với protobuf compression → thực tế có thể ~15-20 Mbps

CPU thiết bị:
  → Data collection chạy trên data plane hoặc dedicated process
  → Không cạnh tranh với routing protocols
  → Consistent latency, không bị delay khi busy

Data points per ngày:
  SNMP (60s interval): 1,000 × 550 × 1,440 = 792 triệu data points/ngày
  Telemetry (1s): 1,000 × 550 × 86,400 = 47.5 tỷ data points/ngày
  
  → Gấp 60 lần dữ liệu, với infrastructure ít bị stress hơn!
```

### Kết quả so sánh (tóm tắt)

| Chỉ số | SNMP (thực tế) | Telemetry (1s) |
|---|---|---|
| Interval đạt được | 60–300 giây | 1 giây |
| Data points/ngày (1,000 devices) | ~13 triệu | ~47.5 tỷ |
| Management bandwidth | ~228 Mbps (lý thuyết) | ~20–50 Mbps (thực tế) |
| CPU impact trên device | Cao (control plane) | Thấp (dedicated) |
| Micro-burst detection | Không | Có |
| Interface flap detection | Delay 60–300s | Ngay lập tức |
| Data loss risk | Cao (UDP + timeout) | Thấp (TCP + reconnect) |

---

## 9. Telemetry Pipeline — Từ Thiết bị đến Dashboard

### Kiến trúc pipeline điển hình

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Telemetry Data Pipeline                          │
└─────────────────────────────────────────────────────────────────────┘

Layer 1: Collection
  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │ Router 1 │  │ Router 2 │  │Switch 1  │  │  ...     │
  │ gNMI     │  │ gNMI     │  │ gNMI     │  │          │
  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
       │              │              │              │
       └──────────────┴──────────────┴──────────────┘
                               │ gRPC streams
                               ▼
Layer 2: Ingestion & Buffering
  ┌────────────────────────────────────────────────────┐
  │              Telegraf / Pipeline / gNMIc           │
  │  (decode protobuf, transform, tag enrichment)      │
  └────────────────────────┬───────────────────────────┘
                           │
                           ▼
  ┌────────────────────────────────────────────────────┐
  │              Apache Kafka (message queue)           │
  │  Topics: telemetry.interfaces, telemetry.bgp, ...  │
  │  Retention: 24-72 giờ (replay capability)          │
  └────────────────────────┬───────────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼

Layer 3: Storage & Processing
  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
  │  InfluxDB    │  │  Prometheus  │  │  Flink /     │
  │  (time-series│  │  (metrics +  │  │  Spark       │
  │   storage)   │  │   alerting)  │  │  (streaming  │
  │              │  │              │  │   analytics) │
  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
         │                 │                 │
         └─────────────────┴─────────────────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │

Layer 4: Visualization & Action
  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
  │   Grafana    │  │ Alertmanager │  │  AI/ML       │
  │  (dashboard) │  │  (PagerDuty, │  │  Engine      │
  │              │  │   Slack,     │  │  (anomaly    │
  │              │  │   Email)     │  │   detection) │
  └──────────────┘  └──────────────┘  └──────┬───────┘
                                              │
                                              ▼
                                    ┌──────────────────┐
                                    │  Automation      │
                                    │  (Ansible/NSO/   │
                                    │   custom scripts)│
                                    └──────────────────┘
```

### Các thành phần quan trọng

**Telegraf (InfluxData):**
- Agent thu thập data, hỗ trợ cả SNMP và gNMI input
- Plugin architecture: 200+ input plugins, 50+ output plugins
- Transform data: rename fields, add tags, filter, aggregate

```toml
# Telegraf config: gNMI input
[[inputs.gnmi]]
  addresses = ["192.168.1.1:57400", "192.168.1.2:57400"]
  username = "telemetry_user"
  password = "secret"
  tls_enable = true
  
  [[inputs.gnmi.subscription]]
    name = "interface_counters"
    path = "/interfaces/interface/state/counters"
    subscription_mode = "sample"
    sample_interval = "1s"
    
  [[inputs.gnmi.subscription]]
    name = "interface_status"
    path = "/interfaces/interface/state/oper-status"
    subscription_mode = "on_change"

[[outputs.kafka]]
  brokers = ["kafka1:9092", "kafka2:9092"]
  topic = "telemetry.interfaces"
```

**Apache Kafka:**
- Message queue với durability (lưu trên disk)
- Decoupling: collector không phụ thuộc vào DB downstream
- Replay: nếu DB down, data vẫn ở Kafka, replay khi DB up lại
- Fan-out: nhiều consumer (InfluxDB, Spark, AI) nhận cùng stream

**InfluxDB:**
- Time-series database tối ưu cho telemetry data
- Tự động expire data cũ (Retention Policy)
- Flux query language cho aggregation phức tạp
- InfluxDB 3.x: Parquet storage, Apache Arrow, SQL support

**Prometheus:**
- Pull model (scrape exporter) + PushGateway
- Phổ biến trong Kubernetes/cloud environment
- AlertManager tích hợp sẵn
- PromQL mạnh cho query và alerting

---

## 10. OpenConfig — Chuẩn hóa YANG Model

### Vấn đề: YANG nhưng mỗi vendor một kiểu

YANG giải quyết được vấn đề schema, nhưng nếu Cisco định nghĩa:
- `/Cisco-IOS-XR-ifmgr-oper:interface-properties/data-nodes/...`

Và Juniper định nghĩa:
- `/interfaces/interface-information/physical-interface/...`

Thì collector vẫn phải xử lý riêng từng vendor → vẫn bị vendor lock-in.

### OpenConfig: vendor-neutral YANG models

**OpenConfig** (openconfig.net) — consortium gồm Google, AT&T, Microsoft, Apple, Facebook, v.v. — định nghĩa **YANG model chuẩn**, vendor-neutral:

```
OpenConfig path (chuẩn hóa, giống nhau trên Cisco, Juniper, Nokia, Arista):

/openconfig-interfaces:interfaces/interface[name=GigabitEthernet0/0/1]/state/counters/in-octets
/openconfig-network-instance:network-instances/network-instance[name=default]/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=10.0.0.1]/state/session-state
/openconfig-platform:components/component[name=CPU0]/cpu/utilization/state/avg

→ Viết 1 lần collector code → chạy được trên tất cả vendor hỗ trợ OpenConfig
```

**OpenConfig YANG modules phổ biến:**

| Module | Nội dung |
|---|---|
| openconfig-interfaces | Interface config + state + counters |
| openconfig-bgp | BGP peers, state, stats |
| openconfig-isis | IS-IS adjacency, metrics |
| openconfig-mpls | LSP state, traffic |
| openconfig-platform | Hardware: CPU, memory, optic, power |
| openconfig-lldp | Neighbor discovery |
| openconfig-qos | Queue stats, drops |
| openconfig-network-instance | VRF, routing table |

### Vendor support matrix (as of mid-2026)

| Vendor / Platform | gNMI | OpenConfig | Native YANG |
|---|---|---|---|
| Cisco IOS-XR | ✓ (6.3+) | Partial | Cisco YANG |
| Cisco NX-OS | ✓ (9.2+) | Partial | Cisco YANG |
| Cisco IOS-XE | ✓ (17.x+) | Limited | Cisco YANG |
| Juniper Junos | ✓ (18.1+) | Good | Juniper YANG |
| Arista EOS | ✓ (4.21+) | Good | Arista YANG |
| Nokia SR-OS | ✓ | Partial | Nokia YANG |
| Huawei VRP | ✓ | Limited | Huawei YANG |
| SONiC | ✓ | Good | Native |

---

## 11. Ứng dụng AI/ML và Automation

### Tại sao Telemetry là nền tảng của AI-Ops

AI/ML cần dữ liệu tốt để làm việc. "Tốt" ở đây nghĩa là:

```
Yêu cầu dữ liệu cho AI/ML:
  ✓ Granular: độ phân giải giây để phát hiện pattern ngắn hạn
  ✓ Continuous: không có gap (SNMP timeout tạo gap)
  ✓ Structured: schema rõ ràng, consistent naming
  ✓ Timestamped chính xác: nanosecond timestamp từ thiết bị
  ✓ Low latency: dữ liệu thực trong vài giây, không phải vài phút
  ✓ Volume: đủ data points để train model

SNMP đáp ứng: 1-2/6 tiêu chí trên
Telemetry đáp ứng: 5-6/6 tiêu chí
```

### Use Case 1: Anomaly Detection

```
Training phase (offline):
  1. Thu thập 6-12 tháng Telemetry data
  2. Label các sự kiện (link flap, congestion, BGP reset)
  3. Train model: CNN/LSTM trên time-series
     → Model học: "trước khi CRC errors tăng, thường có pattern X trong 30s"

Inference phase (real-time):
  Telemetry stream → Feature extraction → Model → Anomaly score
  
  Nếu score > threshold:
    → Alert: "Xác suất 89% link Core-A-B sẽ lỗi trong 5 phút"
    → Proactive: shift traffic trước khi lỗi thực sự xảy ra

Không thể làm được với SNMP 60s data: pattern ngắn hạn bị mất
```

### Use Case 2: Capacity Planning Tự động

```
Với Telemetry 1s data trong 90 ngày:
  - Biết chính xác peak utilization (không phải trung bình 5 phút)
  - Biết duration của peak (micro-burst 3s vs sustained 1h)
  - Time-of-day pattern, day-of-week pattern
  
AI model dự đoán:
  "Link Core-B-C sẽ đạt 80% utilization vào Q3 nếu traffic growth 
   tiếp tục theo trend hiện tại"
  
→ Capacity planning 3-6 tháng trước, không phải phản ứng khi đã nghẽn
```

### Use Case 3: Closed-Loop Automation

```
Full automation pipeline:

                    ┌─────────────────────────────────────┐
                    │         Control Loop                 │
                    │                                     │
  Telemetry Stream → AI Engine → Decision → Automation  → Network
       ↑            (anomaly      (reroute,   (gNMI Set,   (apply
       │            detected)      ACL, etc)   Ansible,     change)
       │                                       NSO)         │
       └─────────────────── feedback ──────────────────────┘

Ví dụ thực tế:
  1. Telemetry: link utilization tăng lên 92% (threshold: 85%)
  2. AI Engine: dự đoán sẽ đạt 100% trong 8 phút
  3. Decision Engine: shift 30% traffic sang link dự phòng
  4. gNMI Set: cập nhật traffic engineering policy trên router
  5. Telemetry xác nhận: utilization giảm về 65%
  6. Toàn bộ: ~30 giây, không cần người can thiệp

→ Đây chính là "Closed-Loop Automation" và "Intent-Based Networking"
```

### Use Case 4: Optical + IP Correlation

Kết hợp với DWDM telemetry (từ bài 1):

```
Optical telemetry: OSNR giảm dần trên link quang (BER tăng)
IP telemetry:      CRC errors bắt đầu tăng trên interface 100G tương ứng

AI correlation:
  "Optical OSNR suy giảm 2 dB/ngày → dự kiến pre-FEC BER vượt threshold
   trong 3 ngày → IP link sẽ flap"

→ Dispatch maintenance trước khi outage
→ Đây là giá trị thực sự của cross-layer telemetry tích hợp
```

---

## 12. Triển khai Thực tế: Lộ trình Chuyển đổi

### Giai đoạn 1: Baseline và Song song (Tháng 1-3)

```
Mục tiêu: Thiết lập Telemetry mà không làm gián đoạn hệ thống hiện tại

Bước 1: Audit thiết bị
  → Inventory: thiết bị nào hỗ trợ gNMI? Phiên bản OS nào?
  → Ưu tiên: Core router trước (ít thiết bị nhưng quan trọng nhất)
  
Bước 2: Setup pipeline cơ bản
  → Deploy Telegraf (gNMI input) → InfluxDB → Grafana
  → Bắt đầu với 5-10 thiết bị Core
  
Bước 3: Define subscription
  → Interface counters: sample 30s (bắt đầu bảo thủ)
  → BGP/OSPF state: on-change
  → CPU/memory: sample 60s
  
Bước 4: Run parallel
  → SNMP vẫn chạy bình thường
  → So sánh data từ SNMP và Telemetry → validate accuracy
```

### Giai đoạn 2: Mở rộng và Tinh chỉnh (Tháng 4-6)

```
Bước 5: Tăng granularity
  → Giảm interval từ 30s → 10s → 1s (theo khả năng chịu tải)
  → Monitor CPU thiết bị: Telemetry subscription có tác động không?
  
Bước 6: Thêm Kafka
  → Nếu nhiều consumer (InfluxDB + AI engine + alerting)
  → Kafka làm buffer và fan-out
  
Bước 7: Migrate alerting
  → Chuyển alert quan trọng từ SNMP trap sang Telemetry on-change
  → BGP state change, interface flap → alert dưới 5 giây thay vì phút
  
Bước 8: Mở rộng ra access/distribution layer
  → Thêm switch, thiết bị tốc độ thấp hơn
```

### Giai đoạn 3: AI/Analytics và Full Automation (Tháng 7+)

```
Bước 9: Data science pipeline
  → Đủ historical data (3-6 tháng) → bắt đầu train anomaly model
  → Jupyter notebook + Python (scikit-learn, PyTorch) trên InfluxDB data
  
Bước 10: Proactive alerting
  → Alert "sẽ xảy ra" thay vì "đã xảy ra"
  → Tích hợp với ticketing system
  
Bước 11: Closed-loop experiment
  → Pilot automation trên môi trường lab/staging trước
  → Roll out từng use case: traffic engineering → ACL → route policy
  
Bước 12: Deprecate SNMP dần dần
  → Giữ SNMP cho legacy device không hỗ trợ gNMI
  → Core network: 100% Telemetry
```

### Common Pitfalls khi triển khai

```
❌ Pitfall 1: Subscription interval quá thấp ngay từ đầu
   Bắt đầu với 1s cho tất cả metric → overload collector và thiết bị
   ✓ Fix: Start với 30-60s, giảm dần sau khi validate

❌ Pitfall 2: Không plan storage retention
   Telemetry tạo data nhiều gấp 60x SNMP → InfluxDB đầy nhanh
   ✓ Fix: Set retention policy (raw data 7 ngày → downsample 5m cho 30 ngày → 1h cho 1 năm)

❌ Pitfall 3: Single collector, no HA
   Collector down → data gap → AI model không tin cậy
   ✓ Fix: Active-active collectors, Kafka để buffer khi downstream down

❌ Pitfall 4: Bỏ qua SNMP hoàn toàn
   Thiết bị legacy, vendor cũ, embedded switch → vẫn cần SNMP
   ✓ Fix: Hybrid approach, SNMP cho legacy, Telemetry cho core

❌ Pitfall 5: Không validate data chất lượng
   Một số vendor có bug trong YANG implementation → counter lạ
   ✓ Fix: Sanity check: so sánh counter delta vs NetFlow vs SNMP
```

---

## 13. Lab Mini: gNMI Subscribe Thực hành

### Setup môi trường lab

Không cần thiết bị thật — dùng **gNMIc** (CLI tool) kết nối vào thiết bị lab hoặc emulator (IOS-XRv, Junos vMX, Arista cEOS):

```bash
# Cài đặt gNMIc
bash -c "$(curl -sL https://get-gnmic.openconfig.net)"

# Hoặc với Docker:
docker pull ghcr.io/openconfig/gnmic:latest
```

### Thực hành 1: Capabilities (thiết bị hỗ trợ gì?)

```bash
gnmic -a 192.168.1.1:57400 \
      -u admin -p admin \
      --tls-no-verify \
      capabilities

# Output mẫu:
# Supported Models:
#   - openconfig-interfaces, openconfig.net/yang/interfaces, 2021-04-06
#   - openconfig-bgp, openconfig.net/yang/bgp, 2021-01-15
#   - Cisco-IOS-XR-ifmgr-oper, ...
# Supported Encodings: JSON_IETF, PROTO
```

### Thực hành 2: Get một lần (tương đương SNMP GetRequest)

```bash
# Lấy danh sách interfaces và trạng thái
gnmic -a 192.168.1.1:57400 \
      -u admin -p admin \
      --tls-no-verify \
      get \
      --path /openconfig-interfaces:interfaces/interface/state

# Output (JSON_IETF):
# {
#   "openconfig-interfaces:interfaces": {
#     "interface": [
#       {
#         "name": "GigabitEthernet0/0/0",
#         "state": {
#           "name": "GigabitEthernet0/0/0",
#           "type": "iana-if-type:ethernetCsmacd",
#           "mtu": 1514,
#           "oper-status": "UP",
#           "admin-status": "UP",
#           "counters": {
#             "in-octets": "1234567890",
#             "out-octets": "987654321",
#             "in-errors": "0"
#           }
#         }
#       }
#     ]
#   }
# }
```

### Thực hành 3: Subscribe sample (stream liên tục)

```bash
# Subscribe interface counters mỗi 10 giây
gnmic -a 192.168.1.1:57400 \
      -u admin -p admin \
      --tls-no-verify \
      subscribe \
      --path /openconfig-interfaces:interfaces/interface/state/counters \
      --mode stream \
      --stream-mode sample \
      --sample-interval 10s \
      --format flat

# Output (flat format, dễ đọc):
# 2026-06-27T10:00:00Z interfaces/interface[name=Gi0/0/0]/state/counters/in-octets: 1234567890
# 2026-06-27T10:00:00Z interfaces/interface[name=Gi0/0/0]/state/counters/out-octets: 987654321
# 2026-06-27T10:00:10Z interfaces/interface[name=Gi0/0/0]/state/counters/in-octets: 1234580000
# ...
```

### Thực hành 4: Subscribe on-change (BGP state)

```bash
# Subscribe BGP peer state, chỉ khi thay đổi
gnmic -a 192.168.1.1:57400 \
      -u admin -p admin \
      --tls-no-verify \
      subscribe \
      --path /openconfig-network-instance:network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor/state/session-state \
      --mode stream \
      --stream-mode on-change

# → Yên lặng khi BGP ổn định
# → Ngay khi BGP flap: push ngay, không chờ interval
```

### Thực hành 5: gNMIc với config file (production-like)

```yaml
# gnmic.yaml
username: telemetry
password: secret
tls-no-verify: false
tls-ca: /certs/ca.crt

targets:
  router-core-01:57400:
    username: telemetry
    password: secret
  router-core-02:57400:
    username: telemetry
    password: secret

subscriptions:
  interface-counters:
    paths:
      - /interfaces/interface/state/counters
    mode: stream
    stream-mode: sample
    sample-interval: 1s
    encoding: proto

  bgp-state:
    paths:
      - /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state
    mode: stream
    stream-mode: on-change
    encoding: proto

outputs:
  kafka-out:
    type: kafka
    address: kafka:9092
    topic: telemetry
```

```bash
gnmic --config gnmic.yaml subscribe
# → Subscribe tất cả targets với tất cả subscription trong config
```

---

## 14. Glossary

| Thuật ngữ | Tiếng Anh đầy đủ | Giải nghĩa ngắn gọn |
|---|---|---|
| SNMP | Simple Network Management Protocol | Giao thức quản lý mạng pull-based, 1988 |
| NMS | Network Management System | Hệ thống quản lý mạng tập trung |
| OID | Object Identifier | Định danh duy nhất của một metric trong SNMP |
| MIB | Management Information Base | Tập hợp định nghĩa OID |
| Trap | SNMP Trap | Cảnh báo bất đồng bộ từ thiết bị đến NMS (UDP) |
| Inform | SNMP Inform | Trap có acknowledgment (SNMPv2c+) |
| YANG | Yet Another Next Generation | Ngôn ngữ mô hình hóa dữ liệu mạng (RFC 6020) |
| gNMI | gRPC Network Management Interface | Giao thức telemetry dùng gRPC |
| gRPC | gRPC Remote Procedure Call | Framework RPC của Google, HTTP/2 + Protobuf |
| Protobuf | Protocol Buffers | Binary serialization format của Google |
| NETCONF | Network Configuration Protocol | Giao thức cấu hình thiết bị, XML + SSH |
| RESTCONF | REST + NETCONF | NETCONF qua HTTP REST API |
| OpenConfig | - | Tổ chức định nghĩa YANG model vendor-neutral |
| TSDB | Time Series Database | DB tối ưu cho dữ liệu theo thời gian |
| InfluxDB | - | TSDB phổ biến cho telemetry |
| Prometheus | - | Monitoring system + TSDB, phổ biến trong K8s |
| Grafana | - | Visualization platform cho time-series data |
| Kafka | Apache Kafka | Distributed message queue, backbone của pipeline |
| Telegraf | - | Agent thu thập metrics, nhiều input/output plugin |
| On-Change | - | Subscription mode: push khi giá trị thay đổi |
| Sample | - | Subscription mode: push định kỳ |
| Anomaly Detection | - | Phát hiện bất thường bằng AI/ML |
| Closed-Loop | - | Automation tự động không cần người can thiệp |
| gNMIc | gNMI client | CLI tool để tương tác với gNMI trực tiếp |
| AI-Ops | AI for Operations | Ứng dụng AI vào network operations |
| Intent-Based | Intent-Based Networking | Mạng tự quản lý dựa trên intent của operator |

---

## 15. Tài liệu Tham khảo

### RFCs và Tiêu chuẩn
- **RFC 1157** — A Simple Network Management Protocol (SNMP)
- **RFC 3410–3418** — SNMPv3 Framework (Architecture, Security, Applications)
- **RFC 6020** — YANG — A Data Modeling Language for the Network Configuration Protocol
- **RFC 7950** — The YANG 1.1 Data Modeling Language (update)
- **RFC 6241** — Network Configuration Protocol (NETCONF)
- **RFC 8040** — RESTCONF Protocol
- **RFC 5277** — NETCONF Event Notifications

### OpenConfig và gNMI
- **OpenConfig Specifications** — openconfig.net
- **gNMI Specification** — github.com/openconfig/reference/tree/master/rpc/gnmi
- **gNMIc Tool** — gnmic.openconfig.net (CLI client, documentation)
- **OpenConfig YANG Models** — github.com/openconfig/public

### Vendor Documentation
- **Cisco Model-Driven Telemetry (MDT)** — IOS-XR, NX-OS
- **Juniper Telemetry Interface (JTI)** — Junos documentation
- **Arista CloudVision Telemetry** — arista.com
- **Nokia Model-Driven Telemetry** — SR-OS documentation

### Tools và Projects
- **Telegraf** — docs.influxdata.com/telegraf — agent thu thập data
- **InfluxDB** — docs.influxdata.com/influxdb — time series database
- **Prometheus** — prometheus.io/docs — monitoring và alerting
- **Grafana** — grafana.com/docs — visualization
- **Apache Kafka** — kafka.apache.org/documentation — message streaming
- **Apache Flink** — flink.apache.org — stream processing

### Báo cáo và Bài viết
- **"Streaming Telemetry: Network Data as a Service"** — NANOG presentations
- **"OpenConfig: Consuming Telemetry at Scale"** — Google SRE blog
- **"From SNMP to Streaming Telemetry"** — Cisco DevNet learning series

---

*Bài viết phản ánh trạng thái công nghệ tính đến mid-2026. Hệ sinh thái OpenConfig và gNMI vẫn đang phát triển nhanh — một số YANG path và vendor implementation có thể thay đổi giữa các phiên bản OS.*

*Tác giả: IP/Core Network Engineer — Series "Networking from the Ground Up"*
