import random

wins = 0
loose = 0
breaks = 0
totiteration = 0
profit = 0
trials = 1000000
#change this value
betInc = 1.5
for x in range(0,trials):
    inpool = 1000
    pool = inpool
    bet = 5
    end = 10000000 #"break the casino"
    iteration = 0
    # 3s  
    # if you win: 2:1 return
    # if you loose, you loose...
    gamble = 0
    while bet < pool and pool < end:
        if random.randint(0,2) == 0: #win
            #print("pool: " + str(pool) + "-- Bet: " + str(bet))
            pool += 2*bet
        else:
            pool -= bet
            bet *= betInc
        iteration += 1
        if pool > inpool:
            break
        #print("pool: " + str(pool) + "-- Bet: " + str(bet))
    #print(iteration)
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
    
print("wins: " + str(wins))
print("losses: " + str(loose))
print("breaks: " + str(breaks))
print("Average turns on table: " + str(int(totiteration/trials)))
print("total profit after " + str(trials) + " trials:"  + str(profit))