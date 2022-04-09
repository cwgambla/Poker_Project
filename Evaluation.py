# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:19:54 2021

@author: Cadmin
"""

myComparisonList = []

#determine if pair
#test1 = [('Ten', 'Clubs'), ('Ace', 'Hearts'), ('King', 'Diamonds'), ('King', 'Hearts'), ('Four', 'Diamonds')]
#test2 = [('Six', 'Spades'), ('Deuce', 'Spades'), ('King', 'Clubs'), ('Five', 'Diamonds'), ('Ten', 'Spades')]

#each set determines of fucntions determines if the flowing hand does indeed exists
#and if it does, what rank, respectively

#Is Pair
def determineIsPair(hand):
    tempCompareList = []
    
    number = 1
    for x in range(5):
        index = 0 + number
        while index < len(hand):
            if hand[x][0] == hand[index][0]:
                
                tempCompareList.append(hand[x])
                tempCompareList.append(hand[index])
                
                if len(tempCompareList) == 2:
                    for x in tempCompareList:
                        myComparisonList.append(x)
                        
                return True
            index +=1
        number += 1
    
    
    
    return False
    
#returns the hands pair


#Is Three
def determineIsThree(hand):
    
    tempCompareList = []
    number = 1
    count = 0
    
    for x in range(5):
        index = 0 + number
        while index < len(hand):
            
            if hand[x][0] == hand[index][0]:
                tempCompareList.append(hand[x])
                tempCompareList.append(hand[index])
                
                count += 1
            index +=1
        number += 1
    
   
    if len(tempCompareList) == 3:
        myComparisonList = []
        for x in range(len(tempCompareList)):
            myComparisonList.append(x)
            
        return True
    
    
    return False



#Is Four
def determineIsFour(hand):
    
    tempCompareList = []
    number = 1
    count = 0
    for x in range(5):
        index = 0 + number
        while index < len(hand):
            if hand[x][0] == hand[index][0]:
                tempCompareList.append(hand[x])
                tempCompareList.append(hand[index])
                count += 1
            index +=1
        number += 1
    
    if count == 4:
        myComparisonList = []
        for x in range(len(tempCompareList)):
            myComparisonList.append(x)
        return True
    return False



#IsTwoPair
def determineIsTwoPair(hand):
    
    tempCompareList = []
    myList = []
    for x in range(5):
        number = x+1
        for y in range(len(hand) - number):
            
            
            if hand[x][0] == hand[number][0]:
                
                #determines if the pair is already in the list
                #if it is, the pair is not added to the list
                condition = True
                for z in range(len(myList)):
                    if hand[x][0] == myList[z]:
                        condition = False
                
                if condition:
                    tempCompareList.append(hand[x])
                    tempCompareList.append(hand[number])
                    myList.append(hand[x])
            number += 1
    if len(myList) == 2:
        myComparisonList = []
        for x in range(len(tempCompareList)):
            myComparisonList.append(x)
        
        return True
    return False
            
      
   
#IsFlush
def determineIsFlush(hand):
    for x in range(len(hand)-1):
        
        if hand[x][1] != hand[x+1][1]:
            return False
        
    myComparisonList = []
    for x in range(len(hand)):
        myComparisonList.append(x)
    return True

#IsStraight
def determineIsStraight(hand):
    myNewList = []
    
    for x in range(len(hand)):
        
        myNewList.append(convertFaceToNumber(hand[x][0]))
    
    myNewList.sort()
    
    for x in range(len(hand)-1):
        if myNewList[x+1]-myNewList[x] != 1:
            return False
    
    myComparisonList = []
    for x in range(len(hand)):
        myComparisonList.append(x)
    return True
   
#Determines if the hand is a straight flush    
def determineIsStraightFlush(hand):
    
    if determineIsStraight(hand) and determineIsFlush(hand):
        myComparisonList = []
        for x in range(len(hand)):
            myComparisonList.append(x)
        return True
    
    return False
#converts a face value into a number
def convertFaceToNumber(card):
    
    if card == "Ace":
        return 1
    if card == "Deuce":
        return 2
    if card == "Three":
        return 3
    if card == "Four":
        return 4
    if card == "Five":
        return 5
    if card == "Six":
        return 6
    if card == "Seven":
        return 7
    if card == "Eight":
        return 8
    if card == "Nine":
        return 9
    if card == "Ten":
        return 10
    if card == "Jack":
        return 11
    if card == "Queen":
        return 12
    if card == "King":
        return 13

#gives a correlating rank to a face value
def rank(card):
    
    if card == "Ace":
        return 14
    if card == "Deuce":
        return 2
    if card == "Three":
        return 3
    if card == "Four":
        return 4
    if card == "Five":
        return 5
    if card == "Six":
        return 6
    if card == "Seven":
        return 7
    if card == "Eight":
        return 8
    if card == "Nine":
        return 9
    if card == "Ten":
        return 10
    if card == "Jack":
        return 11
    if card == "Queen":
        return 12
    if card == "King":
        return 13

#gives a correlating rank to a symbol    
def rankSymbol(card):
    
    if card == "Spades":
        return 4
    if card == "Hearts":
        return 3
    if card == "Diamonds":
        return 2
    if card == "Clubs":
        return 1

def determineIsFullHouse(hand):
    element = hand[0][0]
    hand = [x for x in hand if x[0] != element]
    
    if len(hand) != 2 and len(hand) != 3:
        return False
    
    element = hand[0][0]
    hand = [x for x in hand if x[0] != element]
    if len(hand) != 0:
        return False
    
    return True

#True is player 2 win
#False is player 1 win
def highCard(hand1,hand2):
    
    myList1 = []
    myList2 = []
    
    myList1Sym = []
    myList2Sym = []
    for x in range(len(hand1)):
        
        myList1.append(rank(hand1[x][0]))
        myList2.append(rank(hand2[x][0]))
        myList1Sym.append(rankSymbol(hand1[x][1]))
        myList2Sym.append(rankSymbol(hand2[x][1]))
    
    myList1.sort(reverse = True)
    myList2.sort(reverse = True)
    myList1Sym.sort(reverse = True)
    myList2Sym.sort(reverse = True)
    
    #only uncomment for troubleshooting purposes
    #print(myList1)
    #print(myList2)
    #print(myList1Sym)
    #print(myList2Sym)
    
    for x in range(len(myList1)):
        if myList1[x] > myList2[x]:
            #print("1:",myList1[x],"2:",myList2[x])
            return False
        if myList1[x] < myList2[x]:
            #print("1:",myList1[x],"2:",myList2[x])
            return True
    
    for x in range(len(myList1Sym)):
        if myList1Sym[x] > myList2Sym[x]:
            return False
        if myList1Sym[x] < myList2Sym[x]:
            return True
    
    return True

"""
Highest to Lowest Value

1) Straight Flush
2) Four of a Kind
3) Full House
4) Flush
5) Straight
6) Three of a Kind
7) Two Pair
8) One Pair
"""
def rankHand(hand):
    
    rank = 0
    if determineIsPair(hand):
        #print("Rank1")
        #print(getCompareList())
        rank = 1
    if determineIsTwoPair(hand):
        #print("Rank2")
        #print(getCompareList())
        rank = 2
    if determineIsThree(hand):
        #print("Rank3")
        #print(getCompareList())
        rank = 3
    if determineIsStraight(hand):
        #print("Rank4")
        #print(getCompareList())
        rank = 4
    if determineIsFlush(hand):
        #print("Rank5")
        #print(getCompareList())
        rank = 5
    if determineIsFullHouse(hand):
        #print("Rank6")
        #print(getCompareList())
        rank = 6
    if determineIsFour(hand):
        #print("Rank7")
        #print(getCompareList())
        rank = 7
    if determineIsStraightFlush(hand):
        #print("Rank")
        #print(getCompareList())
        rank = 8
    
    
    #if rank == 1:
       # print("Pair")
    #if rank == 2:
       # print("Two Pairs")
    #if rank == 3:
        #print("Three of a Kind")
    #if rank == 4:
       # print("Straight")
    #if rank == 5:
    #    print("Flush")
    #if rank == 6:
        #print("Full House")
    #if rank == 7:
        #print("Four of a Kind")
    #if rank == 8:
        #print("Straight Flush")
    return rank


def getCompareList():
    return myComparisonList
    
def makeListEmpty():
    myComparisonList = []


#Test Ground          
#print(determineIsPair(hand1))
#print(findPair(hand1))

#print(determineIsThree(hand3))
#print(findThree(hand3))

#print(determineIsFour(hand2))
#print(findFour(hand2))

#print(determineIsTwoPair(testIsTwoPair))
#print(findTwoPair(testIsTwoPair))
# input list


#spades, hearts, diamonds, clubs ranking
#print(highCard(test1,test2))
