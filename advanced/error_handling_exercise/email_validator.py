import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email_name_minimum_size = 4
email_domain_list = ['.com', '.bg', '.org', '.net']
email_name_pattern = r'^[\w+\.]+'
email_domain_pattern = r'\.[a-z]+$'

while True:
    email = input()
    if email == "End":
        break

    if len(re.findall(email_name_pattern, email)[0]) <= email_name_minimum_size:
        raise NameTooShortError("Name must be more than 4 characters")
    elif '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif email.count('@') > 1:
        raise MoreThanOneAtSymbolError("The must be only one @ symbol in the email")
    elif re.findall(email_domain_pattern, email)[0] not in email_domain_list:
        raise InvalidDomainError(f"Domain must be one of the following: {' '.join(email_domain_list)}")

    print("Email is valid")





