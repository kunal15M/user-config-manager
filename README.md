# User Configuration Manager ⚙️

A simple Python-based user configuration manager that allows users to add, update, delete, and view application settings.

## Features
- Add new settings
- Update existing settings
- Delete settings
- View all settings

## Technologies Used
- Python 3

## Example Usage
```python
settings = {"theme": "dark"}

add_setting(settings, ("language", "english"))
update_setting(settings, ("theme", "light"))
view_settings(settings)
