def isEncodeOrDecode(encodeOrdecode):
    return (encodeOrdecode == 'encode' or encodeOrdecode == 'decode')



def validChoice(options, user_choice, re_select): 
    selectOption = 'try'
    while not isEncodeOrDecode(selectOption):
        selectOption = input(options)   #encode  
        
        if not isEncodeOrDecode(selectOption):
            print(re_select)    #here
    print(f"encode text is {selectOption}")

validChoice("Type 'encode' to encode a text, or 'decode' to decode it.\n", isEncodeOrDecode, "Invalid, try again.")




print("---------------------")
def isGreaterthanZero(bid_num):
    if not bid_num > 0:
        return bid_num
    return False


def verify(userNum, numGreaterthanZero, invalidBid):
    name = input("What is your name?: \n")
    user_bid = int(input(userNum)) 
    
    while isGreaterthanZero(user_bid):
        print(invalidBid)
        user_bid = int(input(userNum))

    print(f"winer bid is: {user_bid}")

verify("What's your bid?: $" , isGreaterthanZero, "Invalid bid. Try again.")    

  

    

    



















            
                      
            
            
            
            
 