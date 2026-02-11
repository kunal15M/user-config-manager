from config_manager import *

def main():
    settings = {
        "theme": "dark",
        "notifications": "enabled",
        "volume": "high"
    }

    while True:
        print("\n===== User Configuration Manager =====")
        print("1. Add Setting")
        print("2. Update Setting")
        print("3. Delete Setting")
        print("4. View Settings")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            key = input("Enter setting name: ")
            value = input("Enter setting value: ")
            print(add_setting(settings, (key, value)))

        elif choice == "2":
            key = input("Enter setting name to update: ")
            value = input("Enter new value: ")
            print(update_setting(settings, (key, value)))

        elif choice == "3":
            key = input("Enter setting name to delete: ")
            print(delete_setting(settings, key))

        elif choice == "4":
            print(view_settings(settings))

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()
