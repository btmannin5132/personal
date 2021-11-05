cards = ['AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','KC','QC','JC','10C','9C','8C','7C','6C','5C','4C','3C','2C','AC','KD','QD','JD','10D','9D','8D','7D','6D','5D','4D','3D','2D','AD']
sample = ['QS','AS','2S','3S','4S','5S','6S','7S']
nums = list(range(0,52))


def shuffle(deck,inOut):
    d1 = []
    d0 = []
    d = 0
    for card in deck:
        if d == 1:
            d1.append(card)
        else:
            d0.append(card)
        d^=1
        if inOut == 0:
            deck = d0 + d1
        else:
            deck = d1 + d0
    return deck


def PshuffleToTop(deck,loc):
    d1 = []
    d0 = []
    shuff = 1
    d = 0
    for l in range(len(loc)-1,-1,-1):
        deck = shuffle(deck,int(loc[l]))
        #print(binLoc[l])
        
        #print("shuffle " + str(shuff) + ": " + str(loc[l]))
        #print(str(d0) + "  " + str(d1))
        shuff +=1
        #print(deck) 
        #print("")

    return deck



def PshuffleTopToSpot(deck,loc):

    shuff = 1
    for l in range(0,len(loc)):
        deck = shuffle(deck,int(loc[l])^1)
        #print(binLoc[l])
        
        #print("shuffle " + str(shuff) + ": " + str(loc[l]))
        #print(str(d0) + "  " + str(d1))
        shuff +=1
        #print(deck) 


    return deck

if __name__ == '__main__':

    myDeck = nums
    orgTop = myDeck[0]
    while 1==1:
        x = int(input("In (1) or Out (0) shuffle? (2 to try again) "))
        if x == 2:
            myDeck = nums
        else:
            myDeck = shuffle(myDeck,x)
            print("Location of " + str(orgTop) + ": " + str(myDeck.index(orgTop)))
            print(nums)
            print(myDeck)
            print("")