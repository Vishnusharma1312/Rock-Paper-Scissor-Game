import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image =[rock,paper,scissors]
user_choice= int(input("what do you choose ? type 0 for rock 1 for paper 2 for scissors. \n"))
print(game_image[user_choice])
computer_choice= random.randint(0,2)
print("computer chose :")
print(game_image[computer_choice])
#print(f"Computer chose {computer_choice}")
 
if user_choice >= 3 and computer_choice < 0:
 print("yo type an invalid number , you lose !")
elif user_choice == 0 and computer_choice ==2:
 print("you win !")
elif computer_choice > user_choice :
 print("you lose !")
elif computer_choice < user_choice:
 print("you win !")
elif computer_choice == user_choice :
 print("match draw ! play Again")
else :
 print("you type an invalid number, you lose")
     
 