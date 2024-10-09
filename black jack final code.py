import random
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    game = True

    while game:
        start = input("Do you want to play the black jack game? say 'Y' or 'N': ").lower()

        if start == "y":
            print("\n" * 20, logo)
        elif start == "n":
            print("Thank you for playing, have a Good Day")
            break
        else:
            print("You typed something rong")
            break


        player1 = []
        totalp1 = 0
        player2 = []
        totalp2 = 0

        #player 1
        for i in range(2):
            card = (random.choice(cards))
            player1.append(card)
            if player1 == [11, 11]:
                player1[1] = 1
        print(f"your cards: {player1}, current score {sum(player1)}")
        totalp1 = sum(player1)

        # player 2
        for i in range(2):
            card = (random.choice(cards))
            player2.append(card)
        print(f"computer's first card {player2[0]}")

        # player 2 conditions for it to be running if its under 17
        while sum(player2) < 17:
            card = (random.choice(cards))
            player2.append(card)
            if sum(player2) > 21: # player 2 conditions for 11 to be set to 1 if it exceeds 21.
                if 11 in player2:
                    player2.remove(11)
                    player2.append(1)
        totalp2 = sum(player2)



        # asking user to pick a card or pass
        start2 = input("Type 'y' to get another card, type 'n' to pass:")

        # if user chooses to pick the card and total is < 22 i will add a random card.
        while start2 == "y":
            if sum(player1) <= 21:
                card = (random.choice(cards))
                player1.append(card)
                print(f"your cards: {player1}, current score {sum(player1)}")
                totalp1 = sum(player1)
                if totalp1 > 21: # if its greater and there's 11 in it it will be changed to 1.
                    if 11 in player1:
                        player1.remove(11)
                        player1.append(1)
                        totalp1 = sum(player1)
                        print(f"your cards: {player1}, current score {totalp1}")
            if totalp1 > 21: # if total is greater than 21 the loop will break
                break

            start2 = input("Type 'y' to get another card, type 'n' to pass:")


        # if user choose to pass this will trigger or totalp1 gets more than 21.
        # next it will check all the conditions and judge winner or loser based on the total points
        if start2 == "n" or totalp1 >= 21:
            print(f"your final hand is: {player1}, final score is: {totalp1}")
            print(f"computer hand is: {player2}, final score is: {totalp2}")
            if totalp2 < totalp1 <= 21 or totalp2 > 21 >= totalp1:
                print("You win 😃")
            elif totalp1 == totalp2:
                print("Draw 🙃")
            elif totalp1 < totalp2 <= 21 or totalp1 > 21:
                print("You lose 😭")

blackjack()














