# User Configuration Manager ⚙️

A simple Python-based user configuration manager that allows users to add, update, delete, and view application settings.

## Features
- Add new settings
- Update existing settings
- Delete settings
- View all settings

## Technologies Used
- Python 3

## How to Run

1. Clone the repository:
   git clone https://github.com/kunal15M/user-config-manager.git

2. Navigate to the project folder:
   cd user-config-manager

3. Run the program:
   python demo.py
   
## Example Usage
```python
settings = {"theme": "dark"}

add_setting(settings, ("language", "english"))
update_setting(settings, ("theme", "light"))
view_settings(settings)

