from player import Player
from deck import GameDeck
from artwork import black_jack_logo
import os
import time


def game_logic(user, dealer):

    # game logic starts here
    card_deck = GameDeck()

    while True:
        bet = int(input(f"You have a balance of ${user.balance}.\nHow much would you like to bet this round? $"))
        if bet >= 50:
            break
        else:
            print(f"The minimum bet is $50. Your bet is ${bet}. Please increase your bet.")

    print("")

    for _ in range(2):
        user.cards.append(card_deck.draw_card())
        dealer.cards.append(card_deck.draw_card())

    # user.cards.append(12)
    # user.cards.append(6)
    user.calculate_score()
    user.print_cards()

    dealer.print_cards(True)

    if user.has_black_jack():
        print(f"Congratulations {user.name}! You got a black jack 😎!")
        user.balance += bet * 2
        print(f"You won ${bet * 2}! You have a balance of ${user.balance}")

    elif user.has_double_ace():
        print(f"Congratulations {user.name}! You got double aces 🤩!")
        user.balance += bet * 3
        print(f"You won ${bet * 3}! You have a balance of ${user.balance}")

    else:

        print(f"\nYour score is {user.score}.")

        while user.score < 21:
            another_card = input("Would you like another card? 'y' or 'n': ")
            if another_card.lower() == 'n':
                print("")
                break
            
            user.cards.append(card_deck.draw_card())
            user.calculate_score()
            user.print_cards()
            print(f"Your score is {user.score}")

            if user.five_card_win():
                print(f"Congratulations {user.name}! You got five cards win 🥳!")
                user.balance += bet * 2
                print(f"You won ${bet * 2}! You have a balance of ${user.balance}")
                return

        
        # dealer shows hand
        if dealer.has_black_jack():
            print(f"Oops! {dealer.name} got a black jack 😭!")
            user.balance -= bet * 2
            print(f"You loss ${bet * 2}! You have a balance of ${user.balance}")
            return

        elif dealer.has_double_ace():
            print(f"Oops {dealer.name} got double aces 🤬!")
            user.balance -= bet * 3
            print(f"You lost ${bet * 3}! You have a balance of ${user.balance}")
            return

        dealer.calculate_score()

        print("")
        dealer.print_cards()
        print(f"{dealer.name} current score is {dealer.score}\n")

        while dealer.score < 17:
            dealer.cards.append(card_deck.draw_card())
            dealer.calculate_score()
            dealer.print_cards()
            time.sleep(1)
            # print(f"{dealer.name} score is {dealer.score}")

        #game ends
        print("\n\nResults:")
        print(f"You scored: {user.score}")
        print(f"{dealer.name} scored: {dealer.score}")

        if dealer.score > 21 and user.score > 21:
            print("It's a draw! 🤪")
        elif dealer.score > user.score and dealer.score <= 21:
            print(f"{dealer.name} won! you lost ${bet}. 😭")
            user.balance -= bet
            print(f"You have ${user.balance} remaining.")
        elif dealer.score < user.score and user.score <= 21:
            print(f"You won! you won ${bet}. 😝")
            user.balance += bet
            print(f"You have ${user.balance} remaining.")
        elif dealer.score > 21 and user.score <= 21:
            print(f"You won! you won ${bet}. 😝")
            user.balance += bet
            print(f"You have ${user.balance} remaining.")
        elif dealer.score <= 21 and user.score > 21:
            print(f"{dealer.name} won! you lost ${bet}. 😭")
            user.balance -= bet
            print(f"You have ${user.balance} remaining.")
        elif dealer.score == user.score:
            print("It's a draw! 🤪")


def game_start():
    print(black_jack_logo)

    start_game = input("Would you like to play a game of black jack? 'y' or 'n': ")
    if start_game.lower() == 'n':
        return

    name = input("What is your name?\n")
    balance = int(input(f"Hi {name}! Min bet is $50.\nHow much would you like to start with? $"))

    if name == "":
        name = "user"

    if balance < 50:
        print(f"Please bring more than ${balance} next time.")
        return

    user = Player(name, balance)
    dealer = Player("Alice", 1000000)

    while True:
        game_logic(user, dealer)

        if user.balance < 50:
            print(f"Oops! Your balance is ${user.balance}. You don't have enough money to continue. Game Over.")
            return

        continue_playing = input("\nWould you like to continue playing? 'y' or 'n': ")
        if continue_playing.lower() == 'n':
            print(f"You have a balance of ${user.balance}. Please play again soon!\n")
            break
        
        os.system("clear")
        user.reset()
        dealer.reset()
        print(black_jack_logo)


game_start()
