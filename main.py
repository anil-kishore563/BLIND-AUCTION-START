from replit import clear
from art import logo
print(logo)

dict={}
highest_bid=0
highest_bidder=[]
loop=True
while loop:
  name=input('Enter your name :')
  your_bid=int(input('Enter your bid value $'))
  def silent_bid(name,your_bid):
      global highest_bid
      dict[name]=your_bid
      if dict[name]>highest_bid :
        highest_bid=dict[name]
        highest_bidder.append(name)
  silent_bid(name,your_bid)
  ask=input('Is there anyone next to you to bid? y/n :').lower()
  clear()
  if ask!='y':
    loop=False
print(logo)    
print(f'Highest bid was ${highest_bid}, by {highest_bidder[-1]}.') 
      

