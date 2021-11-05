#sample code about how I plan on making a robot shuffle cards perfectly. 
# This will allow one to move any card in the deck to any prefered location
# Similar to a reverse shuffle
#cards will be separated into 2 piles from the bottom of the deck.
#In Shuffle (1) will be defined as joining the decks such that the top and bottom card changes
#Out Shuffle (0) will be defined as joining the decks such that the top and bottom cards stay the same

import cards

indeck = cards.cards

#move top card QS to anywhere in deck

locDec = int(input("What location to move to the top of the deck? (location 1-52) ")) #0 indexing

binLoc = str(bin(locDec)[2:])
#print(binLoc)

#turn number into 6 bits
while len(binLoc) != 6:
   binLoc =  "0" + binLoc
print(binLoc)


#process:
#Separate the piles starting with bottom cards and swaping pile
#read binary version of the destination location from right to left (LSB to MSB)
# join decks back together in either out or in shuffle

print(cards.PshuffleToTop(indeck,binLoc))

