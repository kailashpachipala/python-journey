# Python Basics

A concise reference covering the fundamental concepts of Python programming.

---

## 📚 Table of Contents

1. [What is Python?](#1-what-is-python)
2. [Python Versions](#2-python-versions)
3. [Basic Syntax Rules](#3-basic-syntax-rules)
4. [Variables and Data Types](#4-variables-and-data-types)
5. [Input and Output](#5-input-and-output)
6. [Operators](#6-operators)
7. [Conditional Statements](#7-conditional-statements)
8. [Loops](#8-loops)
9. [Functions](#9-functions)
10. [Type Conversion](#10-type-conversion)
11. [Common Built-in Functions](#11-common-built-in-functions)
12. [Quick Revision Checklist](#12-quick-revision-checklist)

---

# 1. What is Python?

**Python** is a high-level, interpreted, general-purpose programming language known for its simple and readable syntax.

It was created by **Guido van Rossum** and first released in **1991**.

### Key Features

| Feature                  | Description                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| **Interpreted**          | Python code is executed by the Python interpreter.                                     |
| **High-Level**           | Provides abstractions that hide low-level hardware details.                            |
| **Dynamically Typed**    | Variable types are determined at runtime.                                              |
| **Object-Oriented**      | Supports classes, objects, inheritance, and polymorphism.                              |
| **Open Source**          | Free to use, modify, and distribute.                                                   |
| **Platform Independent** | Python programs can run on different operating systems with little or no modification. |

---

# 2. Python Versions

| Version        | Notes                                                                       |
| -------------- | --------------------------------------------------------------------------- |
| **Python 2.x** | Legacy version; officially discontinued in January 2020.                    |
| **Python 3.x** | Modern Python standard and the version recommended for current development. |

> **Recommendation:** Always learn and use **Python 3.x** for new projects.

---

# 3. Basic Syntax Rules

Python has a simple syntax designed to make code readable.

### Important Rules

* Python uses **indentation** to define blocks of code.
* Curly braces `{}` are not used to define code blocks.
* Statements generally do not require a semicolon `;`.
* Comments begin with `#`.
* Python is **case-sensitive**.
* Consistent indentation is required.

### Single-Line Comment

```python
# This is a single-line comment
print("Hello, Python!")
```

### Multi-Line Documentation / String

Python does not have a dedicated multi-line comment syntax. Triple-quoted strings are commonly used for **docstrings** and can also be used as multi-line string literals.

```python
"""
This is a multi-line string.
It is commonly used for documentation.
"""
```

---

# 4. Variables and Data Types

A **variable** is a name that refers to a value.

Python does not require explicit variable declarations.

```python
x = 10
pi = 3.14
name = "Alice"
flag = True
```

### Built-in Data Types

| Category | Data Type  | Example             |
| -------- | ---------- | ------------------- |
| Numeric  | `int`      | `10`, `-5`          |
| Numeric  | `float`    | `3.14`, `-0.5`      |
| Numeric  | `complex`  | `3 + 4j`            |
| Text     | `str`      | `"Hello"`           |
| Boolean  | `bool`     | `True`, `False`     |
| Sequence | `list`     | `[1, 2, 3]`         |
| Sequence | `tuple`    | `(1, 2, 3)`         |
| Mapping  | `dict`     | `{"name": "Alice"}` |
| Set      | `set`      | `{1, 2, 3}`         |
| Special  | `NoneType` | `None`              |

### Checking Data Types

Use `type()` to determine the type of a value.

```python
print(type(42))
# <class 'int'>

print(type("hello"))
# <class 'str'>

print(type(3.14))
# <class 'float'>
```

---

# 5. Input and Output

## Output

The `print()` function is used to display output.

```python
print("Hello, World!")
```

## Input

The `input()` function is used to accept input from the user.

> **Important:** `input()` always returns a `str`.

```python
name = input("Enter your name: ")

print("Hello,", name)
```

### Converting Input to Integer

```python
age = int(input("Enter your age: "))

print(age)
```

### Converting Input to Float

```python
salary = float(input("Enter your salary: "))

print(salary)
```

---

# 6. Operators

Operators are symbols or keywords used to perform operations on values.

## 6.1 Arithmetic Operators

| Operator | Operation      |  Example | Result |
| -------- | -------------- | -------: | -----: |
| `+`      | Addition       |  `5 + 3` |    `8` |
| `-`      | Subtraction    |  `5 - 3` |    `2` |
| `*`      | Multiplication |  `5 * 3` |   `15` |
| `/`      | Division       |  `5 / 2` |  `2.5` |
| `//`     | Floor Division | `5 // 2` |    `2` |
| `%`      | Modulus        |  `5 % 2` |    `1` |
| `**`     | Exponentiation | `2 ** 3` |    `8` |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## 6.2 Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Meaning                  | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal to                 | `x == y` |
| `!=`     | Not equal to             | `x != y` |
| `>`      | Greater than             | `x > y`  |
| `<`      | Less than                | `x < y`  |
| `>=`     | Greater than or equal to | `x >= y` |
| `<=`     | Less than or equal to    | `x <= y` |

Example:

```python
x = 10
y = 5

print(x > y)    # True
print(x == y)   # False
print(x != y)   # True
```

---

## 6.3 Logical Operators

| Operator | Description                            | Example           |
| -------- | -------------------------------------- | ----------------- |
| `and`    | True if both conditions are true       | `x > 0 and y > 0` |
| `or`     | True if at least one condition is true | `x > 0 or y > 0`  |
| `not`    | Inverts the Boolean result             | `not(x > 0)`      |

Example:

```python
x = 10
y = 5

print(x > 0 and y > 0)  # True
print(x > 0 or y < 0)   # True
print(not(x > 0))       # False
```

---

# 7. Conditional Statements

Conditional statements control the flow of a program based on conditions.

Python uses:

* `if`
* `elif`
* `else`

### Example

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```

### Exam Tip

Python uses **`elif`**, not `else if`.

---

# 8. Loops

Loops are used to execute a block of code repeatedly.

Python provides two primary loops:

* `for`
* `while`

---

## 8.1 `for` Loop

A `for` loop is commonly used when iterating over a sequence or a known range of values.

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### `range()`

The general syntax is:

```python
range(start, stop, step)
```

> **Important:** The `stop` value is excluded.

Example:

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

---

## 8.2 `while` Loop

A `while` loop continues executing as long as its condition is `True`.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

## 8.3 Loop Control Statements

| Statement  | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| `break`    | Immediately exits the loop.                                  |
| `continue` | Skips the current iteration and moves to the next iteration. |
| `pass`     | Does nothing; used as a placeholder.                         |

### Example

```python
for i in range(1, 10):

    if i == 5:
        break

    if i % 2 == 0:
        continue

    print(i)
```

Output:

```text
1
3
```

---

# 9. Functions

A **function** is a reusable block of code designed to perform a specific task.

Functions are defined using the `def` keyword.

### Basic Function

```python
def greet(name):
    return "Hello, " + name


print(greet("Alice"))
```

Output:

```text
Hello, Alice
```

### Function Execution

```text
Input
  ↓
Arguments passed to function
  ↓
Function body executes
  ↓
return statement
  ↓
Output
```

---

## Default Arguments

A function parameter can have a default value.

```python
def power(base, exp=2):
    return base ** exp


print(power(3))
# 9

print(power(2, 10))
# 1024
```

In the first call, `exp` automatically uses the default value `2`.

---

# 10. Type Conversion

**Type conversion**, also called **type casting**, means converting a value from one data type to another.

| Function  | Converts To | Example         | Result  |
| --------- | ----------- | --------------- | ------- |
| `int()`   | Integer     | `int("10")`     | `10`    |
| `float()` | Float       | `float("3.14")` | `3.14`  |
| `str()`   | String      | `str(100)`      | `"100"` |
| `bool()`  | Boolean     | `bool(0)`       | `False` |

### Example

```python
number = "100"

number = int(number)

print(number)
print(type(number))
```

Output:

```text
100
<class 'int'>
```

---

# 11. Common Built-in Functions

Python provides many useful built-in functions.

| Function  | Purpose               | Example           | Result     |
| --------- | --------------------- | ----------------- | ---------- |
| `print()` | Display output        | `print("Hi")`     | `Hi`       |
| `input()` | Take user input       | `input("Name: ")` | User input |
| `len()`   | Return length         | `len("Hello")`    | `5`        |
| `range()` | Generate a sequence   | `range(1, 6)`     | `1–5`      |
| `type()`  | Return data type      | `type(3.14)`      | `float`    |
| `abs()`   | Return absolute value | `abs(-7)`         | `7`        |
| `max()`   | Find maximum          | `max(3, 7, 1)`    | `7`        |
| `min()`   | Find minimum          | `min(3, 7, 1)`    | `1`        |
| `sum()`   | Calculate sum         | `sum([1, 2, 3])`  | `6`        |
| `round()` | Round a number        | `round(3.567, 2)` | `3.57`     |

---

# 12. Quick Revision Checklist

Use this checklist before moving to the next Python topic.

* [ ] Python is high-level, interpreted, and dynamically typed.
* [ ] Python uses indentation to define code blocks.
* [ ] Variables do not require explicit type declarations.
* [ ] Python is case-sensitive.
* [ ] `input()` always returns a string.
* [ ] Use `int()` or `float()` when numeric input is required.
* [ ] `/` performs regular division.
* [ ] `//` performs floor division.
* [ ] `%` returns the remainder.
* [ ] `**` performs exponentiation.
* [ ] `elif` is used instead of `else if`.
* [ ] `range(start, stop, step)` generates a sequence.
* [ ] The `stop` value in `range()` is excluded.
* [ ] `for` and `while` are Python's primary loops.
* [ ] `break` exits a loop.
* [ ] `continue` skips the current iteration.
* [ ] `pass` is a placeholder statement.
* [ ] Functions are defined using `def`.
* [ ] `return` sends a value back from a function.
* [ ] Type conversion can be performed using `int()`, `float()`, `str()`, and `bool()`.

---

## 🎯 Practice Tasks

After learning these concepts, practice writing small programs such as:

1. Print your name, age, and college.
2. Calculate the area of a circle.
3. Check whether a number is even or odd.
4. Find the largest of three numbers.
5. Calculate a student's grade from marks.
6. Print numbers from 1 to 100.
7. Print all even numbers from 1 to 50.
8. Calculate the sum of numbers from 1 to `n`.
9. Create a function to calculate the square of a number.
10. Create a simple calculator using functions and operators.

---

## 📌 Key Takeaway

The fundamental Python flow is:

```text
Variables
    ↓
Data Types
    ↓
Input / Output
    ↓
Operators
    ↓
Conditions
    ↓
Loops
    ↓
Functions
    ↓
Type Conversion
    ↓
Built-in Functions
    ↓
Practice
```

These concepts form the foundation for learning **Data Structures, NumPy, Pandas, Machine Learning, Automation, and AI development**.
