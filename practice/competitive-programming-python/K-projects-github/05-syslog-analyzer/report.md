# Syslog Analysis Report

- Total logs: 5
- Interface down: 2
- Login failed: 2

## Errors by hostname
- router01: 3
- switch01: 1

## Logs by severity
- Severity 3: 2
- Severity 4: 2
- Severity 5: 1

## Interface down
- `Jun 22 09:00:01 router01 %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down`
- `Jun 22 09:01:12 switch01 %LINK-3-UPDOWN: Interface GigabitEthernet0/24, changed state to down`

## Login failed
- `Jun 22 09:00:04 router01 %SEC_LOGIN-4-LOGIN_FAILED: Login failed [user: admin] [Source: 10.0.0.9]`
- `Jun 22 09:02:10 router01 %SEC_LOGIN-4-LOGIN_FAILED: Login failed [user: root] [Source: 10.0.0.9]`
