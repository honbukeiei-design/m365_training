LICENSE_FEATURES = {
    "Microsoft 365 F3": {
        "desktop": False,
        "web_office": True,
        "onedrive": True,
        "sharepoint": True,
        "teams_basic": True,
        "advanced_security": False,
        "copilot_ready": False,
        "storage_label": "軽量利用向け",
    },
    "Microsoft 365 Business Standard": {
        "desktop": True,
        "web_office": True,
        "onedrive": True,
        "sharepoint": True,
        "teams_basic": True,
        "advanced_security": False,
        "copilot_ready": True,
        "storage_label": "標準的な業務利用",
    },
    "Microsoft 365 E3": {
        "desktop": True,
        "web_office": True,
        "onedrive": True,
        "sharepoint": True,
        "teams_basic": True,
        "advanced_security": True,
        "copilot_ready": True,
        "storage_label": "大規模・管理強化",
    },
}


def has_feature(license_type: str | None, feature: str) -> bool:
    if not license_type:
        return False
    return bool(LICENSE_FEATURES.get(license_type, {}).get(feature, False))


def get_license_profile(license_type: str | None) -> dict:
    return LICENSE_FEATURES.get(license_type or "", {})
