import random

def run_game():
    user_choice = 0
    cpu_choice = random(2)
    user_choice = raw_input("Rock(1), paper(2), scissors(3), SHOOT! Enter a number:")
    user_choice = int(user_choice)