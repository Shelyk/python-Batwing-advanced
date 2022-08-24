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
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    result = re.findall(pattern=pattern, string=text)
    print(result)


email_1 = "test_1@gmail.com"
email_2 = "123_test123@test123_test.test"
email_3 = "test-2@.gmail.com"
email_4 = "test_test@.email.com"

check_email(email_1)
check_email(email_2)
check_email(email_3)
check_email(email_4)

# 3.  Write a Python program to remove redundant zeros from an IP address.
# Example: "216.008.094.196" -> "216.8.94.196"

def check_ip_address(ip):
    pattern = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
    temp_ip = re.findall(pattern=pattern, string=ip)
    res_to_str = '.'.join([str(elem) for elem in temp_ip])
    ip_address = re.sub(r'\b0+(\d)', r'\1', res_to_str)
    print(ip_address)


ip_1 = "216.008.094.196"
ip_2 = "216.010.000.196"
ip_3 = "200.100.050.000"
ip_4 = "000.000.000.001"

check_ip_address(ip_1)
check_ip_address(ip_2)
check_ip_address(ip_3)
check_ip_address(ip_4)
# 4.  Write a Python program that check if IP address is valid.
#
#  Valid Example: 216.8.94.196, 0.0.0.0, 127.0.0.1
#
#  Invalid Example: 216.8.94, 14.0..139, 153.192.392.84

def check_valid_ip_address(text):
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[" \
              r"0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    result = re.match(pattern=pattern, string=text)
    print(result.group()) if result else print('IP Incorrect')

text = '153.192.192.84'


check_valid_ip_address(text)
