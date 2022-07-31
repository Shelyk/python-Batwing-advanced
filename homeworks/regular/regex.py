import re


# 1.  Write a Python program which search a phone numbers.
# Valid example: Hello, my phone number is 251-65-23.
# Invalid example: Henry Ford was born July 30, 1863, on a farm in Springwells Township, Michigan.

def check_phone_number(text):
    pattern = '[\d]+-[\d]+-[\d]+'
    result = re.findall(pattern=pattern, string=text)
    print(result)


test = r'Hello, my phone number is 251-65-23'
test2 = r'Henry Ford was born July 30, 1863, on a farm in Springwells Township, Michigan.'
check_phone_number(test)
check_phone_number(test2)

# 2.  Write a Python program basic validation for email.
# Local part should be consisted of lower/upper case, number, underscore and dot.
# Domain part - the same but dot symbol could not be the first character.


def check_email(text):
    pattern = r"[\wd\.]{1,255}@\w+\.+[\wd\.]{1,255}"
    result = re.findall(pattern=pattern, string=text)
    print(result)

test = 'test_1@gmail.com, test-2@.gmail.com, test.3@email.com'

check_email(test)


# 3.  Write a Python program to remove redundant zeros from an IP address.
# Example: "216.008.094.196" -> "216.8.94.196"

def check_ip_address(text):
    pattern = '\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
    temp_ip = re.findall(pattern=pattern, string=text)
    ip_address = re.sub(pattern='0', repl='', string=str(temp_ip))
    print(ip_address)

text = 'My ip - 216.008.094.196'

check_ip_address(text)


# 4.  Write a Python program that check if IP address is valid.
#
#  Valid Example: 216.8.94.196, 0.0.0.0, 127.0.0.1
#
#  Invalid Example: 216.8.94, 14.0..139, 153.192.392.84

def check_valid_ip_address(text):
    pattern = '^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
    result = re.match(pattern=pattern, string=text)
    print(result.group()) if result else print('IP Incorrect')

text = '153.192.192.84'

check_valid_ip_address(text)