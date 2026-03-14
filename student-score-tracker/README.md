# Student Score Tracker: Dictionary-Based Aggregator

A Python-based utility designed to process student performance data. This project focuses on handling complex nested data structures and ensuring computational accuracy through manual state verification.

## Technical Implementation

* **Nested State Management**: Implements a dictionary-of-dictionaries structure to group multi-subject scores by student identity.
* **Defensive Aggregation**: Utilizes `setdefault()` for safe dictionary initialization and `try/except` blocks to handle potential `ZeroDivisionError` during average calculations.
* **Data Integrity**: Processes raw student records into structured averages for both individual subjects and overall performance.

## Technical Validation
To ensure full logical transparency, I have verified both the **Data Transformation** (grouping) and **Aggregation** (averaging) phases using manual trace tables.

### 1. Data Transformation Trace (Grouping Logic)
![Trace Table 1](IMG_20260314_131636.jpg)

### 2. Aggregation Logic Trace (Averaging Logic)
![Trace Table 2](IMG_20260314_155451.jpg)

## Execution Instructions
Ensure you are in the project root directory, then run:

```bash
python student-score-tracker/student_logic.py
