import random
import time

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
---'   ____)____
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

choices = [rock, paper, scissors]

print("🎮 Welcome to Rock-Paper-Scissors Game 🎮")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("What do you choose? (0=Rock, 1=Paper, 2=Scissors): ").strip().lower()


    if user_input in ["exit"]:
        print("\n👋 Thanks for playing! Goodbye!\n")
        break


    if not user_input.isdigit() or int(user_input) not in [0, 1, 2]:
        print("❌ Invalid choice! Please enter 0, 1, or 2.")
        continue

    user_choice = int(user_input)
    print("\nYou chose:")
    time.sleep(1)
    print(choices[user_choice])

    print("\nComputer is choosing...")
    time.sleep(2)
    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    time.sleep(1)
    print(choices[computer_choice])

    time.sleep(1)
    print("\nResult:")
    time.sleep(1.5)

    if user_choice == computer_choice:
        print("🤝 Draw!\n")
    elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
        print("🏆 You win!\n")
    else:
        print("💔 You lose!\n")

    time.sleep(1)
