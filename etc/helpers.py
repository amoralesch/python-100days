def is_encode_or_decode(value):
    return value == 'encode' or value == 'decode'


def is_yes_or_no(value):
    return value.lower() == "yes" or value.lower() == "no"


def is_valid_username(username):
    return username != '' and not username.isnumeric()


def is_greater_than_zero(bid_num):
    return int(bid_num) > 0


def is_integer(value):
    return value.strip().isnumeric()


def ask_input(prompt, validator, error_msg = "Invalid option, try again."):
    value = input(prompt)

    while not validator(value):
        print(error_msg)
        value = input(prompt)

    return value
