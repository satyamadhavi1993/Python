num1 = "123ayu456"
num2 = 123
num3 = 12.33
num4 = -33
num5 = -5.33

# Check If the String is Integer in Python using isdigit() Method

# Time Complexity: O(N)
# Space Complexity: O(1)
def check_input1(num):
	if num.isdigit():
		print("Input is a number")
	else:
		print("Input is not a number")

check_input1(num1)
check_input1(num2)
check_input1(num3)
check_input1(num4)
check_input1(num5)

# Using try

# Time Complexity: O(N)
# Space Complexity: O(1)

def check_input2(string):
	try:
		int(string)
		print("Digit")
	except ValueError:
		print("Not a Digit")

check_input2(num1)
check_input2(num2)
check_input2(num3)
check_input2(num4)
check_input2(num5)


# Check If a String is a Number Python using Regular Expressions (re.match)

# Time Complexity: O(N)
# Space Complexity: O(1)

import re

def is_number_regex(input_str):
	return bool(re.match(r'^\d+$', input_str))

is_number_regex(num1)
is_number_regex(num2)
is_number_regex(num3)
is_number_regex(num4)
is_number_regex(num5)


# Check If the String is Integer in Python using isnumeric() Method

# Time Complexity: O(n)
# Auxiliary Space: O(1)
def check_input3(num):
	num.isnumeric()
	
check_input3(num1)
check_input3(num2)
check_input3(num3)
check_input3(num4)
check_input3(num5)

# Python Check if Given String is Numeric or Not using Python Regex

# Time Complexity: O(1)
# Auxiliary Space: O(1)
import re

def check_input4(num):
	regex = "^[0-9]+$"
	return re.match(regex, num)

check_input4(num1)
check_input4(num2)
check_input4(num3)
check_input4(num4)
check_input4(num5)


# Python Check If String is Number Without any built-in Methods

# Time Complexity: O(n)
# Auxiliary Space: O(1)
import re

def check_input5(num):
	for i in num:
		if i not in range(0, 9):
			return print("Is number False")
		return print("Is number :: True")

check_input5(num1)
check_input5(num2)
check_input5(num3)
check_input5(num4)
check_input5(num5)

def check_input6(num):
	num = num.replace('-', '').replace('.', '')
	print(f"Is number :: {num.isdigit}")

check_input6(num1)
check_input6(num2)
check_input6(num3)
check_input6(num4)
check_input6(num5)

def check_input7(num):
	print(f"Is number :: {abs(num).isdigit}")

check_input7(num1)
check_input7(num2)
check_input7(num3)
check_input7(num4)
check_input7(num5)

def check_input8(string):
	try:
		float(string)
		print("Digit")
	except ValueError:
		print("Not a Digit")
		
check_input8(num1)
check_input8(num2)
check_input8(num3)
check_input8(num4)
check_input8(num5)
