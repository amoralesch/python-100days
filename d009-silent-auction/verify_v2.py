import os
def isGreaterthanZero(bid_num):
    if not bid_num > 0:
        return bid_num
    return False

register = {}
def verify(userNum, numGreaterthanZero, invalidBid):
#    name = input("What is your name?: \n")
    user_bid = int(input(userNum)) 
    
    
    while numGreaterthanZero(user_bid):
        print(invalidBid)
        user_bid = int(input(userNum))
    
    return user_bid
#    register[name] = user_bid
#    return register[name]

#    print(f"winner bid is: {user_bid}")
    

#verify("What's your bid?: $" , isGreaterthanZero, "Invalid bid. Try again.")    

  