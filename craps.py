from random import choice,randint

#no need to make side bets. keep it simple

# i will need to have this variable global so it doesn't reset, than once the maximum length
# of rollers is reached. reset and have a new set of rollers go again
player_rolled = []
shooters = []


# bet = int(input("Place a bet: "))
crap_out = [2, 3, 12]
comeout_win = [7, 11]

# simple bets
double_bet = (2/1)

# complex bets
# thr_elv_odds = (16/1)
# sev_pay = (5/1)
# four_and_ten_pay = (2/1)
# five_nine_pay = (3/2)
# six__et_pay = (6/5)
# craps_pay = (8/1)

# trying different ways to incorporate bets
payouts = {
    2: (8/1),
    3: (8/1),
    4: (2/1),
    5: (3/2),
    6: (6/5),
    7: (5/1),
    8: (6/5),
    9: (3/2),
    10: (2/1)
}
players_and_bets= {}
amt = 100
point = 0


def roll_dice():
    dice1 = range(1,7)
    dice2 = range(1,7)
    roll = (choice(dice1) + choice(dice2))
    return roll



def get_info():
    done = False
    count = 0
    global amt
    players_in_game = int(input("How many people would like to play: "))
    while done == False:
        if count < players_in_game:
            name = input("Enter a simple name to play: ").lower()
            buy_in = int(input(f"The amount to buy_in is {amt}, enter the amount to continue: "))
            players_and_bets[name] = buy_in
            count += 1
        else:
            print("Table at capacity")
            done = True


def players_bets():
    bets = []
    for player, amt in players_and_bets.items():
        while True:
            try:
                bet = int(input("How much would you like to bet: "))
                amt -= bet
                players_and_bets[player] = amt
                bets.append(bet)
                break
            except ValueError:
                print("That is not a number, try again.")
    return bets

def point_bets():
    bets = []
    for player, amt in players_and_bets.items():
        while True:
            try:
                bet = int(input("How much would you like to bet: "))
                amt -= bet
                players_and_bets[player] = amt
                bets.append(bet)
                break
            except ValueError:
                print("That is not a number, try again.")
    return bets

def players_pass_bets():
    pass_list = []
    no_pass = []
    for player, amt in players_and_bets.items():
        pass_bet = input("Do you want to bet pass or no(y/n): ").lower()
        if pass_bet == "y":
            pass_list.append(player)
        else:
            no_pass.append(player)
    return pass_list, no_pass


def players_turn():
    global shooters
    for player in players_and_bets.keys():
        shooters.append(player)




def come_out():
    bets = players_bets()
    pass_list, no_pass = players_pass_bets()
    roll = roll_dice()
    done = False
    players_turn_arr = players_turn()
    global point

    # for player in players.keys():
    #     shooters.append(player)
    for player, amt in players_and_bets.items():
        for bet in bets:

            if roll in crap_out:
                print(f"{player} rolled: {roll}")
                if player in no_pass:
                    amt += (bet*double_bet)
                    players_and_bets[player] = amt

            elif roll in comeout_win:
                print(f"{player} rolled: {roll}")
                if player in pass_list:
                    amt += (bet*double_bet)
                    players_and_bets[player] = amt

            else:
                print(f"Point established, point is: {roll}")
                point = roll
                print(players_and_bets)
                point_round()
            break
        break


def point_round():
    global point
    done = False
    dice = roll_dice()
    pass_list, no_pass = players_pass_bets()
    bet_amts = point_bets()

    while done == False:
        dice = roll_dice()
        for player, amt in  players_and_bets.items():
            for payout, value in payouts.items():
                for bet in bet_amts:
                    if dice == 7:
                        print(f"{dice} rolled, you lose.")
                        done = True
                        break
                    if dice == point and point == value:
                        print(f"{dice} is equal to {point}, you win.")
                        # if point == payout and player in pass_list:
                        amt += (bet*value)
                        print(amt)
                        players_and_bets[player] = amt
                        print(players_and_bets)
                        done = True
                    else:
                        print(dice)
                        continue
                    break
                break
            break

# first_run=False
def main():
    start = get_info()

    done = False
    while done == False:
         play_game = come_out()
         print(players_and_bets)

         for player in players_and_bets:
             replay = input("Would you like to keep playing(y/n): ").lower()

             if replay == "y":
                 continue
             else:
                 del player
                 print(players_and_bets)
                 print("Thank you for playing craps, take care")
                 done = True

main()

# if __name__ == "__main__":
#     main(True)
