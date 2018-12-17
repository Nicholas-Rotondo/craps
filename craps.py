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
thr_elv_odds = (16/1)
sev_pay = (5/1)
four_and_ten_pay = (2/1)
five_nine_pay = (3/2)
six__et_pay = (6/5)
craps_pay = (8/1)

# trying different ways to incorporate bets
# payouts = {
#     2: (8/1),
#     3: (8/1),
#     4: (2/1),
#     5: (3/2),
#     6: (6/5),
#     7: (5/1),
#     8: (6/5),
#     9: (3/2),
#     10: (2/1)
# }
pass_answer = ["yes", "no", "y", "n"]
players_and_bets= {}
duplicates = []
amt = 100
point = 0
rolls = 0


def roll_dice():
    dice1 = range(1,7)
    dice2 = range(1,7)
    roll = (choice(dice1) + choice(dice2))
    return roll


def get_info():
    done = False
    count = 0
    global amt
    # players_in_game = int(input("How many people would like to play: "))
    while done == False:
        if count < 3:
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
    # for player, amt in players_and_bets.items():
    #     pass_bet = input("Do you want to bet point or no(y/n): ").lower()
    #     if pass_bet == "y":
    #         pass_list.append(player)
    #     else:
    #         no_pass.append(player)
    # return pass_list, no_pass
    done = False

    while done == False:
        for player, amt in players_and_bets.items():
            try:
                pass_bet = input("Do you want to bet point or no(y/n): ").lower()
                if pass_bet not in pass_answer:
                    raise ValueError("Input must be (yes/no) or (y/n), try again.")
                else:
                    if pass_bet == "y":
                        pass_list.append(player)
                    else:
                        no_pass.append(player)
            except ValueError as excpt:
                print(excpt)
            done = True


    return pass_list, no_pass



# def players_turn():
#     global shooters
#     for player in players_and_bets.keys():
#         shooters.append(player)


def come_out():
    bets = point_bets()
    pass_list, no_pass = players_pass_bets()
    roll = roll_dice()
    # players_turn_arr = players_turn()
    global point
    for player, amt in players_and_bets.items():
        for bet in bets:

            if roll in crap_out:
                print(f"{roll} was rolled", end=" ")
                if player in no_pass:
                    print(f"{player} wins")
                    amt += (bet*double_bet)
                    players_and_bets[player] = amt
                    print(players_and_bets)
                    done = True
                    break
                else:
                    print(f"{player} loses")
                    print(players_and_bets)
                    done = True
                    break

            elif roll in comeout_win:
                print(f"{roll} was rolled")
                if player in pass_list:
                    print(f"{player} wins")
                    amt += (bet*double_bet)
                    players_and_bets[player] = amt
                    print(players_and_bets)
                    done = True
                    break
                else:
                    print(f"{player} loses")
                    print(players_and_bets)
                    done = True
                    break

            else:
                print(f"Roll is {roll}, point established, ready your bets.")
                point = roll
                point_round()
                return







def point_round():
    global point
    done = False
    dice = roll_dice()
    pass_list, no_pass = players_pass_bets()
    bet_amts = point_bets()
    print(bet_amts)

    while done == False:
        dice = roll_dice()
        for player, amt in  players_and_bets.items():
            # for payout, value in payouts.items():
            for bet in bet_amts:

                if dice == 7:
                    if player in no_pass:
                        print(f"{dice} is equal to {point}, {player} win.")
                        amt += ((bet*2)*double_bet)
                        players_and_bets[player] = amt
                        done = True
                        break
                    else:
                        print(f"{dice} rolled, {player} lose.")
                        print(players_and_bets)
                        done = True
                        break
                elif dice == point:
                    if player in pass_list:
                        print(f"{dice} is equal to {point}, {player} wins.")
                        # amt += (bet*double_bet)
                        # players_and_bets[player] = amt
                        # print(players_and_bets)
                        if point == 4:
                            amt += ((bet*2)*double_bet)
                            players_and_bets[player] = amt
                            print(players_and_bets)
                        if point == 5:
                            amt += ((bet*2)*double_bet)
                            players_and_bets[player] = amt
                            print(players_and_bets)
                        if point == 6:
                            amt += ((bet*2)*double_bet)
                            players_and_bets[player] = amt
                            print(players_and_bets)
                        if point == 8:
                            amt += ((bet*2)*double_bet)
                            players_and_bets[player] = amt
                            print(players_and_bets)
                        if point == 9:
                            amt += ((bet*2)*double_bet)
                            players_and_bets[player] = amt
                            print(players_and_bets)
                        if point == 10:
                            amt += ((bet*2)*double_bet)
                            players_and_bets[player] = amt
                            print(players_and_bets)
                        done = True
                        break
                else:
                    if dice not in duplicates:
                        duplicates.append(dice)
                        no_dups = '\n'.join(str(dups) for dups in duplicates)
                        print(no_dups)
                        break
                    continue
                break


def main():
    start = get_info()

    done = False
    while done == False:
         play_game = come_out()
         print(players_and_bets)

         for player, amt in players_and_bets.items():

             if amt <= 0:
                 print("Insufficient Funds, take care")
                 done = True
             else:
                 replay = input("Would you like to keep playing(y/n): ").lower()

                 if replay == "y":
                     continue
                 else:
                     print("Thank you for playing craps, take care")
                     done = True
                     print(players_and_bets)

if __name__ == "__main__":
    main()
