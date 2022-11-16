from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
valid_domains = ['.com', '.bg', '.org', '.net']

email = input()

counter = 0
searched_letter = "@"
for letter in email:
    if searched_letter == letter:
        counter += 1

while email != 'End':
    try:
        if email.count('@') > 1:
            raise MoreThanOneAtSymbolError("Email should contain only @!")
        elif len(findall(pattern_name, email.split("@")[0])[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        elif len(findall(pattern_name, email.split('@')[0])[0]) != len(email.split('@')[0]):
            raise InvalidNameError("Email name should contain only letters, numbers underscores and dots.")
        elif "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        elif findall(pattern_domain, email.split('@')[1])[0] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

        print("Email is valid")
    except IndexError:
        print("Invalid email")

    email = input()
