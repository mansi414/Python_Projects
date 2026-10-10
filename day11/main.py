from art import logo
import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # a score of blackjack has happened
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, opponent_score):
    if player_score == opponent_score:
        return "Draw"
    elif opponent_score == 0:
        return "Computer wins!"
    elif player_score == 0:
        return "You win!"
    elif player_score > 21:
        return "You went over 21 you loose with a blackjack"
    elif opponent_score > 21:
        return "opponent went over 21 you win !"
    elif player_score > opponent_score:
        return "You win!"
    else:
        return "You lose!"


print(logo)

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

player_cards = []
comp_cards = []
comp_score = -1
user_score = -1

if start == 'y':
    player_cards.append(deal_cards())
    player_cards.append(deal_cards())
    comp_cards.append(deal_cards())

print(f"Your cards:[{player_cards[0]},{player_cards[1]}] , current score: {sum(player_cards)}")
print(f"computer's first card {comp_cards[0]}")

is_game_over = False

while not is_game_over:
    user_score = calculate_score(player_cards)
    comp_score = calculate_score(comp_cards)

    if user_score == 0 or comp_score == 0 or user_score > 21:
        is_game_over = True

    else:
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if hit == 'y':
            player_cards.append(deal_cards())
        else:
            is_game_over = True

while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_cards())
    comp_score = calculate_score(comp_cards)


print(f"your final cards {player_cards} and your final score is {user_score}")
print(f"computers final cards {comp_cards} and computer's final score is {comp_score}")

print(compare(user_score,comp_score))