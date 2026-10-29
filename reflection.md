# Lab 5 Reflection — Static Code Analysis

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without running the program. It can identify likely bugs, unsafe coding patterns, and style violations early, making code easier to maintain and safer to use.

## 2. What did Pylint, Bandit, and Flake8 each help identify?

Pylint reviews general code quality and potential logical or maintainability problems. Bandit focuses on common security risks in Python code. Flake8 checks style and formatting issues, including violations of Python's PEP 8 conventions. Their checks overlap in places, but they focus on different aspects of code quality.

## 3. What issues were fixed in this program?

The revised program uses parameterized SQL statements instead of building SQL with string concatenation, generates PINs with Python's `secrets` module, avoids a mutable default list, removes a blanket exception handler that silently ignored errors, handles unknown station IDs safely, validates station inputs, and follows conventional Python naming and formatting.

## 4. How does static analysis improve software quality, and what are its limitations?

Static analysis helps detect issues before deployment and provides repeatable feedback that can be checked after changes. However, tools can produce warnings that require human judgment, and they cannot prove that a program behaves correctly in every situation. The program should still be run and tested, and the before-and-after reports should be reviewed.
