def YesOrNo(YN):
    return YN.lower() == "yes" or YN.lower() == "no"

def validUserName(userName):
    return userName != '' and not userName.isnumeric()

def isGreaterthanZero(bid_num):
    return int(bid_num) > 0

def verify(userInput, verifying, invalidInput):
    userVal = input(userInput)

    while not verifying(userVal):
        print(invalidInput)
        userVal = input(userInput)

    return userVal
