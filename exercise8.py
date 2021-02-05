def run():
    game = ["ROCK", "PAPER", "SCISSORS"]
    while True:
        player1 = str(input("Rock-Paper-Scissors: ")).upper().strip()
        player2 = str(input("Rock-Paper-Scissors: ")).upper().strip()
        if player1 in game and player2 in game:
            if player1 == player2:
                print("That's a TIE!")
            elif player1 == "ROCK" and player2 == "SCISSORS" or player1 == "PAPER" and player2 == "ROCK" or player1 == "SCISSORS" and player2 == "PAPER":
                print("THE WINNER IS THE PLAYER 1!!")
            else:
                print("THE WINNER IS THE PLAYER 2!!")
        else:
            print("ERROR: Please enter a valid option.")
        a = int(input("Would you like a rematch?(1.Yes|2.No): "))
        if a == 2:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    run()