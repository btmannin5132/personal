import random
import math
betInc = 1.5
def threes(inc,trials,bet):
    orgBet = bet
    wins = 0
    loose = 0
    breaks = 0
    totiteration = 0
    profit = 0
    totbet = 0
    #avggain = 0
    maxGain = 0
    maxLoss = 0
    #change this value


    for x in range(0,trials):
        bet = orgBet
        inpool = 1000
        pool = inpool
        end = 10000000 #"break the casino"
        iteration = 0
        # 3s  
        # if you win: 2:1 return
        # if you loose, you loose...
        gamble = 0
        while bet < pool and pool < end:
            totbet += bet
            if random.randint(0,2) == 0: #win
                #print("pool: " + str(pool) + "-- Bet: " + str(bet))
                pool += 2*bet
            else:
                pool -= bet
                bet *= inc
            iteration += 1
            if pool > inpool: #remove this if you want to see if you can break the casino.
                break
            #print("pool: " + str(pool) + "-- Bet: " + str(bet))
        #print(iteration)
        if pool < inpool:
            #  print("loose")
            loose +=1
        else:
            #print("Win!")
            wins +=1
            profit += (pool - inpool)
        if pool >= end:
            print("Time at table to break: " + str(iteration))
            breaks +=1
        totiteration += iteration
        
        if (pool - inpool) > maxGain:
            maxGain = (pool - inpool)
        if (pool - inpool) < maxLoss:
            maxLoss = (pool - inpool)

    """       
    print("wins: " + str(wins))
    print("losses: " + str(loose))
    #print("breaks: " + str(breaks))
    print("total profit after " + str(trials) + " trials: $"  + str(profit))
    print("Average profit per trial: " + str((profit/trials)))
    print("max Gain: " + str(maxGain))
    print("max loss: " + str(maxLoss))
    print("Average turns on table: " + str(int(totiteration/trials)))
    """
    return wins/trials,abs(profit/wins),totbet/trials



