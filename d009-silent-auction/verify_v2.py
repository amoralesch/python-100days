                       
def YesOrNo(YN):
    return YN.lower() == "yes" or YN.lower() == "no"

def getUserName(userName):
    return userName != '' or userName.isnumeric
    
def isGreaterthanZero(bid_num):
    if int(bid_num) > 0:
        return bid_num
    return False

def verify(userInput, verifying, invalidInput):
    userVal = input(userInput)
    
    while not verifying(userVal):
        print(invalidInput)
        userVal = input(userInput)
        print(userVal)
    return userVal




#def verify(userNum, numGreaterthanZero, invalidBid):
#    name = input("What is your name?: \n")
#    user_bid = int(input(userNum)) 
#       
#    while numGreaterthanZero(user_bid):
#        print(invalidBid)
#        user_bid = int(input(userNum))
#    
#    return user_bid

#    print(f"winner bid is: {user_bid}")
