import math

def Probability(rating1, rating2): 
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

def printLB(lb):
    s = ''
    for n,e in lb.items():
        s+=f'{n} - {e}\n'
    print(s)

def EloRating(Ra, Rb, K, d):
    Pb = Probability(Ra, Rb)
    Pa = Probability(Rb, Ra)

    Ra += K * (d - Pa)
    Rb += K * (1-d - Pb)
    return [Ra, Rb]

def main():
    # loop trough input until a blank line is found, to load old leaderboard
    old = {}
    print('Paste the current ELO leaderboard and press enter:')
    while True:
        line = input()
        if line:
            old.update({ line.split(' - ')[0] : float(line.split(' - ')[1]) })
        else:
            break
    # figure out who participated, who won, and if any new players were in the race
    winner = input('Input the username of the player who won: ')
    participants = input('Input the usernames of players who participated in the race, separated by a comma and a space (, ): ').split(', ')
    new = old.copy()
    for p in participants:
        if p in new:
            continue
        else:
            new.update({p : 5000})

    # failsafe in case user includes winner with participants
    if winner in participants:
        participants.remove(winner)
    new.pop(winner) # also remove the winner from the "new" list

    # Get multipliers
    g = 2 if input(f'Was this a Gemskip race? (y/n): ') == 'y' else 1
    h = 2 if input(f'Was this a Hundo race? (y/n): ') == 'y' else 1

    # Get all players' SRC ranks and run EloRating() comparing the winner against every other player, updating/adding-to the old leaderboard as we go
    w = int(input(f'Input {winner}\'s SRC rank: '))
    for name, elo in new.items():
        if name in participants:
            Ra = old[winner]
            Rb = elo
            l = int(input(f'Input {name}\'s SRC rank: ' ))
            hs = (g*h)*5
            K = abs((w-l)*hs)

            n = EloRating(Ra, Rb, K, 1)
            old.update({winner : round(n[0],2)})
            old.update({name : round(n[1],2)})

    # pretty-print final results ready to be inputed back into the script for the next race
    print('\nUpdated Results: ')
    printLB(old)

if __name__ == '__main__':
    main()
