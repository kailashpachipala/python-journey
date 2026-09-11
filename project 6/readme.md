Unit Converter – Convert km to miles, kg to grams, etc.

Yes. For a Unit Converter project, I’d recommend supporting several common conversion categories rather than only km → miles and kg → grams.

📏 Unit Converter — Features
Category	Conversions
📐 Length	km ↔ miles, m ↔ feet, cm ↔ inches
⚖️ Weight	kg ↔ grams, kg ↔ pounds, grams ↔ ounces
🌡️ Temperature	Celsius ↔ Fahrenheit, Celsius ↔ Kelvin
⏱️ Time	seconds ↔ minutes, minutes ↔ hours, hours ↔ days
💧 Volume	liters ↔ milliliters, liters ↔ gallons
🖥️ Data	KB ↔ MB, MB ↔ GB, GB ↔ TB
⭐ Difficulty

Easy → Medium

🐍 Suggested Python project
unit-converter/
│
├── unit_converter.py
├── README.md
└── requirements.txt

Dependencies: None — the project can be built entirely with Python's standard library.

If you're building this as one of your Python mini-projects, I can also create the 
complete unit_converter.py + README.md + requirements.txt in the same format as your Simple Interest and Number Guessing projects.

Create the complete unit_converter.py, README.md, and requirements.txt files

Done. I created the complete Unit Converter project with:

unit_converter.py — length, weight, temperature, time, volume, and data conversions
README.md — setup, usage, supported conversions, examples, and project details
requirements.txt — no external dependencies required
📁 Project files

Download unit_converter.py

Download README.md

Download requirements.txt

Project structure
unit-converter/
├── unit_converter.py
├── README.md
└── requirements.txt

You can run it with:

python unit_converter.py

unit_converter.py
Code
README.md
Document
requirements.txt
Document

Library
/
python projects
/
README.md
Unit Converter

A simple Python command-line Unit Converter that converts values between common units of length, weight, temperature, time, volume, and digital data.

Features
📏 Length conversion
⚖️ Weight/mass conversion
🌡️ Temperature conversion
⏱️ Time conversion
💧 Volume conversion
💾 Digital data conversion
🔄 Convert repeatedly without restarting the program
❌ Input validation for invalid numbers, categories, and units
🐍 Uses only Python's standard library
Supported Conversions
1. Length
Unit	Symbol
Millimeter	mm
Centimeter	cm
Meter	m
Kilometer	km
Inch	in
Foot	ft
Yard	yd
Mile	mi

Examples:

1 km = 0.621371192237334 mi
1 mi = 1.609344 km
100 cm = 1 m
2. Weight / Mass
Unit	Symbol
Milligram	mg
Gram	g
Kilogram	kg
Ounce	oz
Pound	lb

Examples:

1 kg = 1000 g
1 kg = 2.20462262185 lb
1 lb = 453.59237 g
3. Temperature
Unit	Symbol
Celsius	c
Fahrenheit	f
Kelvin	k

Examples:

0 C = 32 F
100 C = 212 F
0 C = 273.15 K
4. Time
Unit	Symbol
Second	s
Minute	min
Hour	h
Day	day

Examples:

60 s = 1 min
60 min = 1 h
24 h = 1 day
5. Volume
Unit	Symbol
Milliliter	ml
Liter	l
Teaspoon	tsp
Tablespoon	tbsp
Cup	cup
Gallon	gal
6. Digital Data
Unit	Symbol
Byte	b
Kilobyte	kb
Megabyte	mb
Gigabyte	gb
Terabyte	tb

Digital data uses binary multiples: 1 KB = 1024 bytes, 1 MB = 1024 KB, etc.

Project Structure
unit-converter/
│
├── unit_converter.py
├── README.md
└── requirements.txt
Requirements
Python 3.9 or later
No external Python packages are required
Installation
1. Clone or download the project

Open a terminal in the project folder.

2. Optional: create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate
3. Install requirements
pip install -r requirements.txt

There are no third-party dependencies, so this command does not install external packages.

How to Run

Windows:

python unit_converter.py

macOS/Linux:

python3 unit_converter.py
Example Run
=============================================
        UNIT CONVERTER
=============================================

Available categories:
1. Length
2. Weight
3. Temperature
4. Time
5. Volume
6. Data

Choose a category (1-6) or Q to quit: 1

Available units for Length:
mm | cm | m | km | in | ft | yd | mi

From unit: km
To unit: mi
Enter value: 10

=============================================
10 km = 6.2137119224 mi
=============================================

Do you want to convert again? (y/n): y
Conversion Logic

The program uses a base unit for most categories.

For example, length uses meters as the base unit:

value × source_unit_factor ÷ target_unit_factor

For temperature, direct formulas are used:

Celsius to Fahrenheit
F = (C × 9/5) + 32
Fahrenheit to Celsius
C = (F - 32) × 5/9
Celsius to Kelvin
K = C + 273.15
Error Handling

The program handles:

Invalid category selections
Invalid unit names
Non-numeric input
Repeated conversions
Quit option

Example:

Enter value: abc
Invalid number. Please enter a numeric value.
Learning Objectives

This project demonstrates:

Python functions
Dictionaries
Loops
Conditional statements
Exception handling
Type hints
Function references
User input/output
Modular program design
Future Improvements

Possible extensions:

Add area conversion
Add speed conversion
Add pressure conversion
Add energy conversion
Add a graphical user interface using Tkinter
Add command-line arguments
Add automated unit tests
Add a web interface
License

This project is free to use for learning and educational purposes.