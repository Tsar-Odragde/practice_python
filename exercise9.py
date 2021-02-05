import random


def run():
    answer = random.randint(1,9)
    guess = int(input("Guess the number from 1 to 9: "))
    i = 0
    while guess != answer:
        if guess > answer:
            print("Too high, try again.")
            i+=1
        else:
            print("Too low, try again.")
            i+=1
        guess = input("Guess the number from 1 to 9, type "'exit'" to exit:").lower()
        if guess == "exit":
            print(f"Too bad you can't guess it in {i} attempts, the number was {answer}")
            break
        else:
            guess = int(guess)
    if guess == answer:
        print(f"You win! {guess} is the number, you guess it in {i} attempts!")


if __name__ == "__main__":
    run()