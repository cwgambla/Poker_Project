# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:24:28 2021

@author: Cadmin
"""

import random
from Evaluation import*
#Creates Standard 52 Card Deck
deck = [
        #Spades
        ('Ace','Spades'),('Deuce','Spades'),('Three','Spades'),('Four','Spades'),('Five','Spades'),
        ('Six','Spades'),('Seven','Spades'),('Eight','Spades'),('Nine','Spades'),('Ten','Spades'),
        ('Jack','Spades'),('Queen','Spades'),('King','Spades'),
        
        #Hearts
        ('Ace','Hearts'),('Deuce','Hearts'),('Three','Hearts'),('Four','Hearts'),('Five','Hearts'),
        ('Six','Hearts'),('Seven','Hearts'),('Eight','Hearts'),('Nine','Hearts'),('Ten','Hearts'),
        ('Jack','Hearts'),('Queen','Hearts'),('King','Hearts'),
        
        #Clubs
        ('Ace','Clubs'),('Deuce','Clubs'),('Three','Clubs'),('Four','Clubs'),('Five','Clubs'),
        ('Six','Clubs'),('Seven','Clubs'),('Eight','Clubs'),('Nine','Clubs'),('Ten','Clubs'),
        ('Jack','Clubs'),('Queen','Clubs'),('King','Clubs'),
        
        #Diamonds
        ('Ace','Diamonds'),('Deuce','Diamonds'),('Three','Diamonds'),('Four','Diamonds'),('Five','Diamonds'),
        ('Six','Diamonds'),('Seven','Diamonds'),('Eight','Diamonds'),('Nine','Diamonds'),('Ten','Diamonds'),
        ('Jack','Diamonds'),('Queen','Diamonds'),('King','Diamonds') ]


#shuffles deck

#test1 = [('Nine', 'Clubs'), ('Eight', 'Hearts'), ('Jack', 'Spades'), ('Seven', 'Spades'), ('Ten', 'Hearts')]
#test2 = [('Deuce', 'Clubs'), ('Ace', 'Clubs'), ('Five', 'Diamonds'), ('Three', 'Spades'), ('Deuce', 'Diamonds')]
random.shuffle(deck)

#creates hands
hand1 = []
hand2 = []

#fill in hand 1
for x in range(5):
    index = random.randint(0,len(deck)-1)
    hand1.append(deck[index])
    
    #removes card from deck
    del deck[index]

#fill in hand 2
for x in range(5):
    index = random.randint(0,len(deck)-1)
    hand2.append(deck[index])
    
    #removes card from deck
    del deck[index]
 

condition = True

myList1 = []
myList2 = []

rank1 = rankHand(hand1)
for x in range(len(getCompareList())):
    myList1.append(getCompareList()[x])

#These lines of code is to "clear" the comparison list, since I have been having problems
#with said variable retaining old information
length = len(myList1)



rank2 = rankHand(hand2)


for x in range(len(getCompareList())):
    myList2.append(getCompareList()[x])
    
for x in range(length):
    del myList2[0]
#for x in range(length):
    




condition = True

if rank1 > rank2:
    condition = False

if rank1 == rank2 & rank1 != 0:
    condition = highCard(myList1,myList2)

if rank1 == rank2 & len(myList1) == 0:
    
    condition = highCard(hand1,hand2)
    
 
print("Player1:",hand1)
print("Player2:",hand2)
print()   
if condition:
    print("Player 2 wins")
else:
    print("Player 1 wins")

#compares the two hands

