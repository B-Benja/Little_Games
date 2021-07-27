import random
import os

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## Ace equals 11, if score > 11, Ace equals 1

cards = {
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "Jack": 10,
  "Queen": 10,
  "King": 10,
  "Ace": 11,
}

# assign random number of cards to either computer or player
def random_card(player,number_drawn_cards):
  """add a given number of random cards to the hand - either to computer or player"""
  for x in range(0,number_drawn_cards):
    drawn_card = random.choice(list(cards))
    player.append({drawn_card: cards[drawn_card]})
  return player

# sum score of the cards
def sum_of_cards(player,score):
  """sum the score of all cards in player or computer hand"""
  score = 0
  ace_count = 0
  for dict in player:
    for element in dict:
      score += dict[element]
      if element == 'Ace':
        ace_count += 1
  # if score is > 10, count Aces as 1 not as 11
  if score > 21 and ace_count > 0:
    score = score - 10 * ace_count
  return score

# get all name of the cards - keys in the dictionaries
def name_of_cards(player,card_names):
  """get the keys from the dcitionary and store in list"""
  card_names.clear()
  for dicts in player:
      for names in dicts:
        card_names.append(names)
  return card_names

# clear all stats
def cleaning():
  """reset all stats for a new game"""
  player_cards.clear()
  computer_cards.clear()
  player_names.clear()
  computer_names.clear()
  player_score = 0
  computer_score = 0
    
# just to not have so much text, basically the input & print as function
def stats():
    print(f"""Your cards: {name_of_cards(player_cards,player_names)}, current score: {sum_of_cards(player_cards,player_score)}\n
    Cards of computer: {name_of_cards(computer_cards,computer_names)}
    """)

# if player wins
def player_win():
  print(f"!!!!!!!!!!!!!!!!!!!!!\nYEAH! You won\nComputer: {name_of_cards(computer_cards,computer_names)} - Player: {name_of_cards(player_cards,player_names)}\nComputer: {sum_of_cards(computer_cards, computer_score)} - Player {sum_of_cards(player_cards,player_score)}\n!!!!!!!!!!!!!!!!!!!!!")

# if computer wins
def computer_win():
  print(f"!!!!!!!!!!!!!!!!!!!!!\nOh no. You loose\nComputer: {name_of_cards(computer_cards,computer_names)} - Player: {name_of_cards(player_cards,player_names)}\nComputer: {sum_of_cards(computer_cards, computer_score)} - Player {sum_of_cards(player_cards,player_score)}\n!!!!!!!!!!!!!!!!!!!!!")


player_cards = []
computer_cards = []
player_score = 0
computer_score = 0
player_names = []
computer_names = []

playing_game = True

while playing_game:
  game_active = True
  cleaning()
  if input("Do you you want to play a game of Blackjack? Typ 'y' or 'n'") == 'y':
    os.system('cls')
    print(logo)
    # give player 2 starting cards
    random_card(player_cards, 2)
    # give computer 1 starting card
    random_card(computer_cards, 1)
    stats()
    while game_active: 
      if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
        random_card(player_cards, 1)
        # if statement to check if player has more than 21 (and loses the game)
        if sum_of_cards(player_cards,player_score) > 21:
          stats()
          print("!!!!!!!!!!!!!!!!!!!!!\nOh no, you went over. You loose\n!!!!!!!!!!!!!!!!!!!!!")
          game_active = False
        else:
          stats()
      else:
        # player finished her turn; computer now draws cards; draws card if below 15 OR below 17 AND one card is an ace
        computer_turn = True
        random_card(computer_cards, 1)
        while computer_turn:
          if sum_of_cards(computer_cards, computer_score) > 21:
            stats()
            player_win()
            computer_turn = False
            game_active = False
          elif sum_of_cards(computer_cards, computer_score) >= sum_of_cards(player_cards,player_score):
            computer_win()
            computer_turn = False    
            game_active = False
          # if computer score below 15, draw another card
          elif sum_of_cards(computer_cards, computer_score) <= 15:
            random_card(computer_cards, 1)
          # if computer scores below 16 AND player above 16: computer tries another card
          elif sum_of_cards(computer_cards, computer_score) <= 16 and sum_of_cards(player_cards,player_score) > 16:
            random_card(computer_cards, 1)
          else:
            stats()
            if sum_of_cards(computer_cards, computer_score) >= sum_of_cards(player_cards,player_score):
              computer_win()
              computer_turn = False    
              game_active = False
            else:
              player_win()
              computer_turn = False    
              game_active = False
  else:
    print("You don't want to play BlackJack? You came to the wrong neighbourhood then! Anyway, have a great day!")
    playing_game = False
