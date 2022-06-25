############### Blackjack Project #####################

from replit import clear
import random

def deal_card():
  """returns random card from the list"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calulate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
#Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards)==21 and len(cards)==2:
    return 0
  
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score==computer_score:
    return "Draw"
  elif computer_score==0:
    return "Lose, oppent has Blackjack"
  elif user_score==0:
    return "You win with Blackjack"
  elif user_score>21:
    return "you went over, you loose"
  elif computer_score>21:
    return "computer went over, you win"
  elif computer_score<user_score:
      return "you win"
  else:
      return "you lost"

def play_game():
  from art import logo
  print(logo)
  is_game_over= False
  user_cards = []
  computer_cards = []
  
#Deal the user and computer 2 cards each using deal_card() and append().
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  #The score will need to be rechecked with every new card drawn and the checks in calulate_score need to be repeated until the game ends.
  while not is_game_over:
     
#Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    
    user_score=calulate_score(user_cards)
    computer_score=calulate_score(computer_cards)
    print(f"your cards: {user_cards}, your score: {user_score}")
    print(f"computer first card: {computer_cards[0]}")
   
    if user_score==0 or user_score==0 or user_score>21:
      is_game_over= True
    else:
#If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal= input("Type 'y' to get an another card or 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over= True
  
  
  
  
#Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score= sum(computer_cards)
  
  print(f"your final hand: {user_cards}, your final score: {user_score}")
  print(f"computer final hand: {computer_cards}, computer final score: {computer_score}")
  print(compare(user_score,computer_score))
  
  
  
#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
  
while input("Do you want you play game Blackjack? type 'y' or 'n': ") == 'y':
  #clear()
  play_game()
