class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


line = input()
patter = r""
valid_emails = ['.com', '.bg', '.org', '.net']

while not line == "End":

    if len(line.split("@")[0]) < 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")
    elif "." + line.split("@")[1].split(".")[1] not in valid_emails:
        raise InvalidDomainError(f"Domain must be one of the following: {' '.join(valid_emails)}")

    print("Email is valid")

    line = input()