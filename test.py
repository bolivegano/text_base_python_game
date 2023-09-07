import random

TURN_ORDER = []

#create a function that selects a list from two pattern options:
def turn_order():
   return random.choice([["a", "b", "b", "a"], ["b", "a", "a", "b"]])
 
def print_turn():
    #set our TURN_ORDER global variable to the result of our function to pick a list pattern:
    TURN_ORDER = turn_order()
    
    #make a copy of TURN_ORDER:
    UPCOMING_TURNS = TURN_ORDER.copy()
    
    #create an empty list called "turns"
    turns = []

    #create a for loop that runs 50 times
    for _ in range(50):
        # I don't know what's happening next, what logic is being tested?***:
        if not UPCOMING_TURNS:
            #set UPCOMING_TURNS equal to our copy of TURN_ORDER again. (I assume this is because we need to continue the pattern?)
            UPCOMING_TURNS = TURN_ORDER.copy()
        #take the last item off "UPCOMING_TURNS" and append it to "turns" list. but why the last item?
        turns.append(UPCOMING_TURNS.pop())
    #print an empty sting but join it with the entire contents of "turns" (50 characters). why the join method here? is that necessary because its pulling from a list?
    print("".join(turns))

print_turn()
