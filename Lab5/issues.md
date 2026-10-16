# Lab 5: Static Code Analysis — Issue Report

## Project: Fitness Club Class Booking Ledger

**File analyzed:** `gym_system.py`

**Tools used:** Pylint, Bandit, Flake8

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution (B605) | Security — High | 36 | `os.system()` executed a shell command using a variable, creating a potential command-injection vulnerability. | Replaced shell execution with Python's `pathlib.Path.glob()` and `unlink()` methods to remove matching JSON files safely. |
| Mutable default argument (W0102) | Code quality | 8 | The `attendance_log=[]` default could cause the same list to be shared across multiple function calls. | Changed the default to `None` and initialized a new list inside the function when required. |
| Incorrect capacity comparison | Logic bug | 12 | The `>` comparison allowed an additional booking when the roster had already reached its capacity. | Changed the comparison to `>=` to prevent bookings once the class is full. |
| Bare exception handling (W0702/E722) | Error handling | 21 | A bare `except` could hide unexpected errors and make debugging difficult. | Replaced it with `except (KeyError, ValueError)` to handle expected cancellation failures. |
| Missing module docstring (C0114) | Code quality | 1 | The Python module did not describe its purpose. | Added a module-level docstring describing the fitness booking system. |
| Missing function docstrings (C0116) | Code quality | Multiple | Several functions did not explain their purpose. | Added descriptive docstrings to the functions. |
| Invalid function naming (C0103) | Code style | 27 | `addMembers()` did not follow the recommended snake_case naming convention. | Renamed the function to `add_members()` and updated its calls. |
| Inefficient string formatting (C0209) | Code quality | 15 | Percent-based string formatting was used instead of an f-string. | Replaced the formatting expression with an f-string. |
| Unsafe file handling (W1514/R1732) | Code quality | 32 | The output file was opened without an explicit encoding or context manager. | Used `with open(file, "w", encoding="utf-8")` to ensure correct encoding and automatic file closure. |
| Dictionary iteration (C0206) | Code quality | 39 | The roster-display function iterated over dictionary keys and then accessed values separately. | Used `rosters.items()` to iterate over class names and their members together. |
| Missing blank lines (E302/E305) | Code style | Multiple | Function definitions and the final top-level call did not follow PEP 8 blank-line requirements. | Applied the required blank-line spacing during the Flake8 cleanup. |
| Excessive line length (E501) | Code style | 77 | A line exceeded Flake8's 79-character limit. | Split the guest-count input expression across multiple lines using parentheses. |
| Unused import (W0611) | Code quality | 2 | The `os` module was no longer needed after removing `os.system()`. | Removed the unused `os` import. |

## Conclusion

Static code analysis helped identify security vulnerabilities, potential logic errors, code-quality issues, and formatting violations in the original program. Bandit was used to address the shell-command security finding, Pylint guided improvements to code quality and maintainability, and Flake8 identified formatting issues.

The fixes were organized into separate commits for Bandit, Pylint, and Flake8. The final code was checked again using all three tools to verify the improvements.

