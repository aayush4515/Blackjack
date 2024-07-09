import random
#from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#user cards and computer cards //declaration
user_cards = []
comp_cards = []

#keep track of sum of cards
# sum_user = 0
# sum_comp = 0

#check for ace
# 1 if False, 11 if true
def check_ace(curr_card, curr_sum):
  if curr_card == 11:
    if (curr_card + curr_sum) > 21:
      return False
  else:
    return True


#function to check winner
def check_winner(user_score, comp_score):
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")

  if user_score <= 21:
    if comp_score < user_score:
      print("You Win!")
    elif comp_score == user_score:
      print("Draw!")
    elif comp_score > 21:
      print("You Win because computer went over 21!")
    else:
      print("You Lose!")
  elif user_score > 21:
    print("You Lose because you went over 21!")


#function to get a card
def get_card():
  return cards[random.randint(0, 12)]


#function to deal two cards in the beginning
def deal_cards():
  #user
  global sum_user
  for i in range(0, 2):
    user_card = get_card()
    if not check_ace(user_card, sum_user):
      user_card = 1

    sum_user += user_card
    user_cards.append(user_card)

  #computer
  global sum_comp
  for i in range(0, 2):
    comp_card = get_card()
    if not check_ace(comp_card, sum_comp):
      comp_card = 1

    sum_comp += comp_card
    comp_cards.append(comp_card)


#start the game
def start():
  deal_cards()

  #print user's cards
  print(f"\tYour cards: {user_cards}, current score: {sum_user}")
  print(f"\tComputer's first card: {comp_cards[0]}")


def play_helper(sum_user, sum_comp):
  get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

  while get_another_card == 'y' and (sum_user <= 21):
    curr_card = get_card()
    user_cards.append(curr_card)

    if not check_ace(curr_card, sum_user):
      curr_card = 1

    sum_user += curr_card
    print(f"Your cards: {user_cards}, current score: {sum_user} ")
    print(f"\tComputer's first card: {comp_cards[0]}")

    if sum_user > 21:
      check_winner(sum_user, sum_comp)
      return

    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

  while sum_comp <= 16:
    curr_comp_card = get_card()
    if not check_ace(curr_comp_card, sum_comp):
      curr_comp_card = 1

    comp_cards.append(curr_comp_card)
    sum_comp += curr_comp_card

  check_winner(sum_user, sum_comp)


def play():
  print(logo)
  sum_user = 0
  sum_comp = 0
  start()
  play_helper(sum_user, sum_comp)




while True:

  play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play_again == 'y':
    #clear()
    play()
  else:
    break