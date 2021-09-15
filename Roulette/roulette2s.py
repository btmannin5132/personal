import random


wins = 0
loose = 0
breaks = 0
totiteration = 0
trials = 1000000
profit = 0
avgGain = 0
avgLoss = 0
maxGain = 0
maxLoss = 0
for x in range(0,trials):
    inpool = 10000
    pool = inpool
    bet = 5
    end = 10000000 #"break the casino"
    iteration = 0
    # 2s  
    # if you win: 1:1 return
    # if you loose, you loose...
    gamble = 0
    while bet < pool and pool < end:
        if random.randint(0,1) == 0: #loose
            pool -= bet
            bet *=2
            #print("pool: " + str(pool) + "-- Bet: " + str(bet))
        else:
            pool += bet
        iteration += 1
        #print("pool: " + str(pool) + "-- Bet: " + str(bet))
        #print(iteration)
        if pool > inpool:  #remove this if you want to be greedy and see if you can break the casino.
            break
    if pool < inpool:
        #  print("loose")
        loose +=1

    else:
        #print("Win!")
        wins +=1
    if pool >= end:
        print("Time at table to break: " + str(iteration))
        breaks +=1
    totiteration += iteration
    profit += (pool - inpool)
    if (pool - inpool) > maxGain:
        maxGain = (pool - inpool)
        avgGain += (pool - inpool)
    if (pool - inpool) < maxLoss:
        maxLoss = (pool - inpool)
        avgLoss += (pool - inpool)
    
print("wins: " + str(wins))
print("losses: " + str(loose))
#print("breaks: " + str(breaks))
print("total profit after " + str(trials) + " trials: $"  + str(profit))
print("Average profit per trial: " + str((profit/trials)))
print("max Gain: " + str(maxGain))
print("avg Gain: " + str(avgGain/wins))
print("max loss: " + str(maxLoss))
print("avg Loss: " + str(avgLoss/loose))
print("Average turns on table: " + str(int(totiteration/trials)))