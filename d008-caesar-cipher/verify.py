def isEncodeOrDecode(encodeOrdecode):
    return (encodeOrdecode == 'encode' or encodeOrdecode == 'decode')

def isYesOrNo(value):
    return value == 'yes' or value == 'no'

def validChoice(options, inputEncodeOrDecode, re_select="Invalid, try again."):
    selectOption = 'try'
    while not inputEncodeOrDecode(selectOption):
        selectOption = input(options).lower()

        if not inputEncodeOrDecode(selectOption):
            print(re_select)

    return selectOption

def isGreaterthanZero(bid_num):
    if not bid_num > 0:
        return bid_num
    return False

def verify(userNum, numGreaterthanZero, invalidBid):
    name = input("What is your name?: \n")
    user_bid = int(input(userNum))

    while numGreaterthanZero(user_bid):
        print(invalidBid)
        user_bid = int(input(userNum))
