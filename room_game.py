from sys import exit
# based on different rooms, you will either die or go to next room and loops over.
def tea_room():
    print("What kind of tea would you like?")
    
    next = input("> Enter 0 or 1 for tea, or else! ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("You are poisoned! You dead!")
        
    if how_much < 50:
        print("The best healing tea in the world! You are alive. You win!")
        exit(0)
    else:
        dead("No healing tea. You are dead.")
# rooms start out with prints. then you move on to choices by while/if/else.
def snack_room():
    print("There are snacks on the table.")
    print("The snacks are far away from you to reach.")
    print("There is a security guard guarding snacks near the table.")
    print("How are you going to get them?")
    snack_eaten = False
    
    while True:
        next = input("> ")
        
        if next == "Walk away":
            dead("You get nothing. Boo!")
        elif next == "taunt security guard" and not snack_eaten:
            print("Security guard walked away, and you can get snacks now.")
            snack_eaten = True
        elif next == "taunt security guard" and snack_eaten:
            dead("You stole the snacks! You will get punished!")
        elif next == "walk to table" and snack_eaten:
            tea_room()
        else:
            print("What are you talking about?")
            
def dining_room():
    print("Here is dining room with a full of family.")
    print("They are all happy eating last dinner together.")
    print("Are you going to join them or walk away?")
    
    next = input("> ")
    
    if "walk" in next:
        start()
    elif "join" in next:
        dead("You will be stuck here forever. Muhahaha!")
    else:
        dining_room()
        
def dead(why):
    print(why, "See you in next life!")
    exit(0)
# You start from here. Then you chose which directions to go.
# based on above, you get to go different rooms.
def start():
    print("You are in a space.")
    print("You can either go straight or turn back.")
    print("Which way would you take?")
     
    next = input("> ")
    
    if next == "go straight":
        snack_room()
    elif next == "turn back":
        dining_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()
    
    
