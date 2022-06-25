import random
  
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
game= input("Do you want play BlackJack game? type 'y' or 'n': ").lower()
def blackjack():
  ycards=random.choices(cards,k=2)
  ccards=random.choices(cards,k=2)
  if game=='y':
    from art import logo
    print(logo)
    check=True
    while check:
      print(f"your cards: {ycards}")
      yscore=sum(ycards)
      print(f"current score: {yscore}")
      print(f"computer's first card: {ccards[0]}")
      
      def ace():
        for i in range(len(ycards)):
          if ycards[i]==11:
            ycards[i]=1
      if yscore>21:
        ace()
        yscore=sum(ycards)
        check= True
        if yscore>21:
          print(f"current score: {yscore}")
          print("you loose \U0001F62D")
          check = False
      elif yscore==21:
        print(f"current score: {yscore}")
        print("you win \U0001f600")
        check=False
      if check:
        check = input("type 'y' to get another card or type 'n' to pass: ").lower()
      if check =='y':
        a_card=random.choice(cards)
        ycards.append(a_card)
        yscore=sum(ycards)
        if yscore>21:
          ace()
          yscore=sum(ycards)
      elif check== 'n':
        check= False
      
    cscore=sum(ccards)
    while cscore<17:
      c_card=random.choice(cards)
      ccards.append(c_card)
      cscore=sum(ccards)
    if cscore<yscore<21:
      print(f"your cards: {ycards}, your score: {yscore}")
      print(f"computer cards: {ccards}, computer score: {cscore}")
      print(f"you win \U0001f600")
    if cscore>21:
      for j in range(len(ccards)):
        if ccards[j]==11:
          ccards[j]=1
          cscore= sum(ccards)
          
    elif yscore<cscore<21:
      print(f"your cards: {ycards}, your score: {yscore}")
      print(f"computer cards: {ccards}, computer score: {cscore}")
      print("you loose \U0001F62D")
call= True
while call:
  blackjack()
  cl= input("Do you want to continue playing? type 'y' or 'n': ").lower()
  if cl=='n':
    call = False