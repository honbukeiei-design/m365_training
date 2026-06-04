LICENSE_FEATURES = {
    "Microsoft 365 F3": {
        "desktop": False,
        "web_office": True,
        "onedrive": True,
        "sharepoint": True,
        "teams_basic": True,
        "advanced_security": False,
        "copilot_ready": False,
        "label": "現場・Web中心",
    },
    "Microsoft 365 Business Standard": {
        "desktop": True,
        "web_office": True,
        "onedrive": True,
        "sharepoint": True,
        "teams_basic": True,
        "advanced_security": False,
        "copilot_ready": True,
        "label": "標準業務向け",
    },
    "Microsoft 365 E3": {
        "desktop": True,
        "web_office": True,
        "onedrive": True,
        "sharepoint": True,
        "teams_basic": True,
        "advanced_security": True,
        "copilot_ready": True,
        "label": "組織管理強化",
    },
}


def has_feature(license_type: str | None, feature: str) -> bool:
    return bool(LICENSE_FEATURES.get(license_type or "", {}).get(feature, False))


def get_license_profile(license_type: str | None) -> dict:
    return LICENSE_FEATURES.get(license_type or "", {})
