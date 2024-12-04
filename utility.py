def validate_name(name):
    try:
        str(name)
        return True
    except ValueError:
        return False


def validate_phone(phone):
    try:
        int(phone)
        return True
    except ValueError:
        return False
