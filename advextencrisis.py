
import random

while True:
    print("WELCOME TO PARADOX DOOR! where the end is the beginning and the beginning is the ending, created to deal with your existential crisis")

    selection = input("Hello! my name is Nyan catu, are you ready to take the adventure (Y/N)? ").upper()
    if selection == "Y":
        print('''      ______
   ,-' ;  ! `-.
  / :  !  :  . \\
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|''')

        door = input("Do you want to enter the door (Y/N)? ").upper()
        if door == "Y":
            print("You're entering, be careful...")

            while True:
                weapon = input("You have seen three weapons, what do you want? (MSCISSORS, MCARDS, MCLOTH) ").upper()
                if weapon == "MSCISSORS":
                    print("You received MSCISSORS")
                    print('''    _    _
   (_)  / )
     | (_/ 
    _+/  
   //|\\
  // | )
 (/  |/     ''')
                    break
                elif weapon == "MCARDS":
                    print("You received MCARDS")
                    print('''                                      .------.
                   .------.           |A .   |
                   |A_  _ |    .------; / \  |
                   |( \/ )|-----. _   |(_,_) |
                   | \\  / | /\\  |( )  |  I  A|
                   |  \\/ A|/  \\ |_x_) |------'
                   `-----+\\  / | Y  A|
                         |  \\/ A|-----'    hjw
                         `------' ''')
                    break
                elif weapon == "MCLOTH":
                    print("You received MCLOTH")
                    print('''     ___________
  [===|  _       |====]
      | |_       ||
      | |_ |     ||
      |   _||\\/| ||
      |     |  | ||
      |          ||
ejm97 |==========||
      |==========||
      '"'""""'"'"'|
       |          |
       '""'"""'"'"' ''')
                    break
                else:
                    print("Invalid choice, try again.")
                    
            while True:
                door1 = input("Choose door (1/2/3): ")
                if door1 == "1":
                    print("You lost your weapon!")
                    print("You need to find a way out...")
                    break
                elif door1 == "2":
                    print("You see a baby girl crying and instantly you're out.")
                    print("You feel a strange sense of deja vu...")
                    break
                elif door1 == "3":
                    print("You entered into it and you see three more doors.")
                    break
                else:
                    print("Invalid choice, try again.")

            while True:
                door2 = input("Select door (1/2/3): ")
                if door2 == "1":
                    print("You found a hidden passage, but it leads you back to the beginning.")
                    break
                elif door2 == "2":
                    print("You encounter a wise old man who gives you cryptic advice and sends you back to the start.")
                    break
                elif door2 == "3":
                    print("You find a treasure chest, but as you open it, you are transported back to the beginning.")
                    break
                else:
                    print("Invalid choice, try again.")
        else:
            print("You are ready to leave the place. Come back when you're ready for an adventure.")

    else:
        print("Get back, don't waste my time!")
