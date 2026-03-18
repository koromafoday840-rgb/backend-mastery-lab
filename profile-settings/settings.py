"""
Author: Foday Christopher Koroma
Date: March 18, 2026

This is a simple command-line program for managing profile settings.

The goal here was to move beyond theory and actually interact with data in a way
that feels real. Instead of just learning what dictionaries are, this program
uses them to store user preferences and lets those preferences change over time.

The user can update existing settings, add new ones, remove unwanted ones,
and view everything at any point. The program keeps running until the user
decides to exit, which makes it behave more like a real system rather than
a one-off script.

I also made a small effort to preserve data types where possible, so values like
True/False and numbers are stored correctly instead of being treated as plain text.
"""


# Starting point: a few default settings so the system has something to work with
profile_settings = {
    "theme": "dark",
    "font_size": "small",
    "notifications": True
}


# Keep the program alive until the user chooses to exit
while True:
    print("\n___Profile Settings___")
    print("Actions: [1] Update [2] Add [3] Remove [4] View All [5] Exit")

    choice = input("Choose option (1-5): ").strip()

    # --- UPDATE ---
    if choice == "1":
        print("Available settings:", profile_settings.keys())
        setting = input("Select setting to update: ").strip()

        # Only update if the setting already exists
        if setting in profile_settings:
            new_value = input("Enter new value: ").strip()

            # Convert input into a more meaningful type when possible
            if new_value.lower() == "true":
                new_value = True
            elif new_value.lower() == "false":
                new_value = False
            elif new_value.isdigit():
                new_value = int(new_value)

            profile_settings[setting] = new_value
            print("Setting updated.")
        else:
            print("Setting not found. Use 'Add' instead.")

    # --- ADD ---
    elif choice == "2":
        new_setting = input("Enter new setting name: ").strip()
        new_value = input("Enter value: ").strip()

        # Same idea here: try not to store everything as plain text
        if new_value.lower() == "true":
            new_value = True
        elif new_value.lower() == "false":
            new_value = False
        elif new_value.isdigit():
            new_value = int(new_value)

        profile_settings[new_setting] = new_value
        print("Setting added.")

    # --- REMOVE ---
    elif choice == "3":
        removed_setting = input("Select setting to remove: ").strip()

        # Avoid crashing if the key doesn't exist
        if removed_setting in profile_settings:
            del profile_settings[removed_setting]
            print("Setting removed.")
        else:
            print("Setting not found.")

    # --- VIEW ---
    elif choice == "4":
        if not profile_settings:
            print("No settings available.")
        else:
            print("\nCurrent Profile Settings:")
            for key, value in profile_settings.items():
                print(f"{key}: {value}")

    # --- EXIT ---
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    # --- INVALID INPUT ---
    else:
        print("Invalid choice. Please select (1-5).")