# Lab 5: Static Code Analysis — Fitness Club Class Booking Ledger

#### Repository Link - https://github.com/sameerdeshpande17/L5_04_fitness_booking

## Static Code Analysis and Fixes

Three static code analysis tools were used to identify and fix security, code quality, and formatting issues in `gym_system.py`.

### Commit 1: Fix Bandit Security Issues
**Tool:** Bandit

- Identified an insecure use of `os.system()` for deleting old JSON export files.
- Replaced the shell command with Python's `pathlib.Path` to safely identify and delete matching files.
- Removed the unnecessary `os` import.
- Verified the changes by rerunning Bandit.

### Commit 2: Fix Pylint Code Quality Issues
**Tool:** Pylint

- Added module and function docstrings.
- Replaced the mutable default argument with `None`.
- Replaced `%` string formatting with f-strings.
- Replaced the bare `except` with specific exceptions.
- Renamed `addMembers()` to `add_members()` to follow Python naming conventions.
- Added file encoding and used a context manager when opening files.
- Improved dictionary iteration using `.items()`.
- Fixed the class-capacity condition to prevent bookings when a class is full.

**Result:** Pylint score improved from **6.60/10 to 10.00/10**.

### Commit 3: Fix Flake8 Formatting Issues
**Tool:** Flake8

- Corrected blank-line spacing around function definitions.
- Fixed the line-length violation by splitting a long input statement across multiple lines.
- Ensured the code follows Python's formatting conventions.
- Reran Flake8 to verify the fixes.

### Verification

All three tools were rerun after the fixes to check the updated code:

- **Bandit:** No security issues identified.
- **Pylint:** Score of 10.00/10.
- **Flake8:** No remaining style violations.

The changes were organized into three separate commits, making it easier to track the fixes introduced by each tool.


