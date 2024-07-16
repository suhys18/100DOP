import random
rps =[ """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
     """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
  """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]


choice = input("Choose Rock/Paper/Scissors:").lower()
if choice == 'rock':
    print("you chose:\n" + rps[0])

elif choice == 'paper':
    print("you chose:\n" + rps[1])

elif choice == 'scissors':
    print("you chose:\n" + rps[2])
else:
  print("tie")


random_rps = random.randint(0,len(rps)-1)
rand_rps = rps[random_rps]
print("bot chose:" + rand_rps)

if choice == 'scissors' and rand_rps == rps[0]:
  print("You lose")

elif choice == 'scissors' and rand_rps == rps[1]:
  print("You win")

elif choice == 'paper' and rand_rps == rps[0]:
  print("YOu win")

elif choice == 'paper' and rand_rps == rps[2]:
  print("YOu lose")

elif choice == 'rock'and rand_rps == rps[1]:
  print("you lose")

elif choice == 'rock' and rand_rps == rps[2]:
  print("you won")
else:
  print("tie")


