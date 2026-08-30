1\. What is Python?

Python is a high-level, interpreted, general-purpose programming language known for its simple and readable syntax. It was created by Guido van Rossum and first released in 1991.



Key Features

Feature	Description

Interpreted	Code is executed line by line; no separate compilation step

High-Level	Closer to human language; abstracts hardware complexity

Dynamically Typed	Variable types are determined at runtime

Object-Oriented	Supports classes, objects, and inheritance

Open Source	Free to use, modify, and distribute

Platform Independent	"Write once, run anywhere" across OS platforms

2\. Python Versions

Version	Notes

Python 2.x	Legacy; officially discontinued since Jan 2020

Python 3.x	Current standard; not fully backward compatible with Python 2

3\. Basic Syntax Rules

Python uses indentation (whitespace) to define blocks of code instead of {} braces.

Statements do not end with a semicolon (;) — though it is allowed.

Comments begin with #.

python

\# This is a single-line comment

"""

This is a

multi-line comment (docstring)

"""



4\. Variables and Data Types

Variable — a named memory location used to store a value. No declaration keyword is needed.



python

x = 10          # int

pi = 3.14       # float

name = "Alice"  # str

flag = True     # bool

Built-in Data Types

Category	Data Type	Example

Numeric	int	10, -5

Numeric	float	3.14, -0.5

Numeric	complex	3 + 4j

Text	str	"Hello"

Boolean	bool	True, False

Sequence	list	\[1, 2, 3]

Sequence	tuple	(1, 2, 3)

Mapping	dict	{"key": "value"}

Set	set	{1, 2, 3}

None	NoneType	None

python

\# Check data type using type()

print(type(42))       # <class 'int'>

print(type("hello"))  # <class 'str'>

5\. Input and Output

python

\# Output

print("Hello, World!")

Input (always returns a string)



name = input("Enter your name: ")

print("Hello,", name)

Type casting input to int/float



age = int(input("Enter age: "))

salary = float(input("Enter salary: "))

6\. Operators

Arithmetic Operators

Operator	Operation	Example	Result

\+	Addition	5 + 3	8

\-	Subtraction	5 - 3	2

Multiplication	5 3	15

/	Division (float)	5 / 2	2.5

//	Floor Division	5 // 2	2

%	Modulus	5 % 2	1

Exponentiation	2 3	8

Comparison Operators

Operator	Meaning	Example

==	Equal to	x == y

!=	Not equal to	x != y

>	Greater than	x > y

<	Less than	x < y

>=	Greater than or equal	x >= y

<=	Less than or equal	x <= y

Logical Operators

Operator	Description	Example

and	True if both are true	x > 0 and y > 0

or	True if at least one is true	x > 0 or y > 0

not	Inverts the result	not(x > 0)

7\. Conditional Statements

Conditional statements control the flow of execution based on a condition.



python

\# if-elif-else

marks = int(input("Enter marks: "))

if marks >= 90:

&#x20;   print("Grade: A")

elif marks >= 75:

&#x20;   print("Grade: B")

elif marks >= 60:

&#x20;   print("Grade: C")

else:

&#x20;   print("Grade: F")



> Exam Tip: Python uses elif, not else if.



8\. Loops

for Loop — used when the number of iterations is known

python

\# Iterate over a range

for i in range(1, 6):

&#x20;   print(i)   # Prints 1 to 5

while Loop — used when the condition controls iteration

python

\# while loop

count = 1

while count <= 5:

&#x20;   print(count)

&#x20;   count += 1

Loop Control Statements

Statement	Description

break	Exits the loop immediately

continue	Skips current iteration, moves to next

pass	Does nothing; used as a placeholder

python

for i in range(1, 10):

&#x20;   if i == 5:

&#x20;       break       # stops at 5

&#x20;   if i % 2 == 0:

&#x20;       continue    # skips even numbers

&#x20;   print(i)

9\. Functions

Function — a reusable, named block of code that performs a specific task.



python

\# Defining and calling a function

def greet(name):

&#x20;   return "Hello, " + name

print(greet("Alice"))   # Hello, Alice



Algorithm: Function Execution

text

Input   → Arguments passed by the caller

Process → Statements inside the function body execute

Output  → Value returned via return statement

Default and Keyword Arguments

python

def power(base, exp=2):       # exp has a default value

&#x20;   return base  exp

print(power(3))       # 9  (exp defaults to 2)

print(power(2, 10))   # 1024



10\. Type Conversion (Casting)

Type conversion — converting a value from one data type to another.



Function	Converts to	Example

int()	Integer	int("10") → 10

float()	Float	float("3.14") → 3.14

str()	String	str(100) → "100"

bool()	Boolean	bool(0) → False

11\. Common Built-in Functions

Function	Purpose	Example

print()	Display output	print("Hi")

input()	Take user input	input("Name: ")

len()	Length of object	len("Hello") → 5

range()	Generate number sequence	range(1, 6)

type()	Return data type	type(3.14) → float

abs()	Absolute value	abs(-7) → 7

max()	Maximum value	max(3, 7, 1) → 7

min()	Minimum value	min(3, 7, 1) → 1

sum()	Sum of iterable	sum(\[1, 2, 3]) → 6

round()	Round a number	round(3.567, 2) → 3.57

12\. Quick Revision Checklist

\[ ] Python is interpreted, dynamically typed, and indentation-based

\[ ] Variables need no type declaration

\[ ] input() always returns a str; cast when needed

\[ ] / returns float; // returns int (floor division)

\[ ] elif is used instead of else if

\[ ] range(start, stop, step) — stop is excluded\*\*

\[ ] Functions are defined with def and return values using return

