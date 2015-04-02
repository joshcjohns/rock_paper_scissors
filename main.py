import random
import sys

user_wins = 0
cpu_wins = 0
ties = 0

def run_game():
    global user_wins
    global cpu_wins
    global ties
    user_choice = 0
    cpu_choice = random.randrange(2)
    while user_choice < 1 or user_choice > 3:
        user_choice = raw_input("Rock(1), Paper(2), Scissors(3), SHOOT! Enter a number: ")
        user_choice = int(user_choice)
        if (user_choice > 3) or (user_choice < 1):
            print "Please enter a number 1 through 3."

    #If user plays Rock
    if user_choice == 1:
        print "You chose Rock."
        print "Computer chose %s." % cpu_choice_str(cpu_choice)
        if cpu_choice == 0:
            print "You tied!"
            ties += 1
        elif cpu_choice == 1:
            print "Computer's Paper covers your Rock! You lost."
            cpu_wins += 1
        elif cpu_choice == 2:
            print "Your Rock smashes computer's Scissors! You win!"
            user_wins += 1

    #If user plays Paper
    elif user_choice == 2:
        print "You chose Paper."
        print "Computer chose %s." % cpu_choice_str(cpu_choice)
        if cpu_choice == 0:
            print "Your Paper covers computer's Rock! You win!"
            user_wins += 1
        elif cpu_choice == 1:
            print "You tied!"
            ties += 1
        elif cpu_choice == 2:
            print "Computer's Scissors cut your Paper! You lose."
            cpu_wins += 1

    #If user plays Scissors
    elif user_choice == 3:
        print "You chose Scissors."
        print "Computer chose %s." % cpu_choice_str(cpu_choice)
        if cpu_choice == 0:
            print "Computer's Rock smashes your Scissors! You lose"
            cpu_wins += 1
        elif cpu_choice == 1:
            print "Your Scissors cut computer's Paper! You win!"
            user_wins += 1
        elif cpu_choice == 2:
            print "You tied!"
            ties += 1

    print "Thanks for playing!"
    print "Your wins: %d" % user_wins
    print "Computer wins: %d" % cpu_wins
    print "Ties: %d" % ties

def cpu_choice_str(x):
    if x == 0:
        return "Rock"
    elif x == 1:
        return "Paper"
    else:
        return "Scissors"

print "Let's play a game of Rock, Paper, Scissors."
run_game()
play_again = True
while play_again:
    response = raw_input("Do you want to play again? (Y/N): ").lower()
    if response == "y" or response == "yes":
        play_again = True
        run_game()
    else:
        sys.exit()