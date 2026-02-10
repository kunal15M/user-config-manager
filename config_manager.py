def add_setting(settings_dict, key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()

    if key in settings_dict:
        return f"Setting '{key}' already exists!"
    
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict, key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()

    if key not in settings_dict:
        return f"Setting '{key}' does not exist!"

    settings_dict[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings_dict, key):
    key = key.lower()

    if key not in settings_dict:
        return "Setting not found!"

    del settings_dict[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."

    output = "Current User Settings:\n"
    for k, v in settings_dict.items():
        output += f"- {k.capitalize()}: {v}\n"

    return output
