def ask_input(prompt, validator, error_msg = "Invalid option, try again."):
    value = input(prompt)

    while not validator(value):
        print(error_msg)
        value = input(prompt)

    return value
