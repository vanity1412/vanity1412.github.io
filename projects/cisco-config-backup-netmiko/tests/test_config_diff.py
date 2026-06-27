from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "backup_config.py"

spec = importlib.util.spec_from_file_location("backup_config", MODULE_PATH)
backup_config = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["backup_config"] = backup_config
spec.loader.exec_module(backup_config)


class ConfigDiffTests(unittest.TestCase):
    def test_normalize_config_removes_volatile_lines(self) -> None:
        first = """Building configuration...
Current configuration : 1234 bytes
! Last configuration change at 10:10:10 UTC Sat Jun 27 2026
hostname R1
ntp clock-period 123456
interface GigabitEthernet0/0
 description LAN
"""

        second = """Building configuration...
Current configuration : 9999 bytes
! Last configuration change at 11:11:11 UTC Sat Jun 27 2026
hostname R1
ntp clock-period 987654
interface GigabitEthernet0/0
 description LAN
"""

        self.assertEqual(backup_config.normalize_config(first), backup_config.normalize_config(second))


    def test_build_config_diff_detects_meaningful_change(self) -> None:
        previous = """hostname R1
interface GigabitEthernet0/0
 description LAN
"""

        current = """hostname R1
interface GigabitEthernet0/0
 description USERS-LAN
"""

        diff_text = backup_config.build_config_diff(previous, current, "previous", "current")

        self.assertIn("- description LAN", diff_text)
        self.assertIn("+ description USERS-LAN", diff_text)


if __name__ == "__main__":
    unittest.main()
