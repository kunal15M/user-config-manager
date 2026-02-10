from config_manager import *

settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}

print(add_setting(settings, ("language", "English")))
print(update_setting(settings, ("volume", "medium")))
print(delete_setting(settings, "notifications"))
print(view_settings(settings))
