# Profile Settings Manager (CLI)

A clean, robust Python tool for managing user preferences. This project demonstrates core backend logic: handling dictionary data structures, validating user input, and maintaining a persistent runtime loop.

## 🎯 Project Goal
The objective was to move beyond simple "print" statements and build a system that interacts with data dynamically. This program allows for real-time updates, additions, and removals of profile settings, ensuring that data types (Booleans and Integers) are preserved rather than treated as simple strings.

## 🛠️ Key Engineering Features
- **Data Type Validation:** Automatically detects if a user input should be a `Boolean` (True/False) or an `Integer` to keep the dictionary technically accurate.
- **Safety Checks:** Implements key-existence checks before deletion to prevent `KeyError` crashes.
- **Kebab-Case Architecture:** Organized within a standardized folder structure for better repository navigation.

---

## 🔍 Logic Trace (Internal Mechanics)

| Action | Logic Path | Result |
| :--- | :--- | :--- |
| **Update** | `if setting in profile_settings` | Checks existence before overwriting. |
| **Data Type** | `.isdigit()` or `.lower() == "true"` | Converts string input to proper Python types. |
| **Remove** | `del profile_settings[key]` | Safely removes entry after confirmation. |

---

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone the repository:
   ```bash
   git clone [https://github.com/koromafoday840-rgb/backend-mastery-lab.git](https://github.com/koromafoday840-rgb/backend-mastery-lab.git)