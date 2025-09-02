import json
import sys
import cdp_sender

def test_parse_args_config_file(tmp_path, monkeypatch):
    cfg = {
        "interface": "eth1",
        "device_id": "DeviceX",
        "software_version": "v1",
        "platform": "PlatformX",
        "ttl": 100,
        "capabilities": "0x0001",
    }
    config_file = tmp_path / "cfg.json"
    config_file.write_text(json.dumps(cfg))
    monkeypatch.setattr(sys, "argv", ["cdp_sender.py", "--config", str(config_file)])
    args = cdp_sender.parse_args()
    assert args.interface == "eth1"
    assert args.device_id == "DeviceX"
    assert args.software_version == "v1"
    assert args.platform == "PlatformX"
    assert args.ttl == 100
    assert args.capabilities == 0x0001
