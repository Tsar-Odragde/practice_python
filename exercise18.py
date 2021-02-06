import random


def cows_bulls_checker(cows_bulls, g_number):
    c = 0
    while cows_bulls[0] != 4:
        cows_bulls = [0,0]
        u_number = input("Enter a 4 digit number: ")
        if u_number == "exit": return False, c
        elif len(u_number) != 4:
            print(f"ERROR: {u_number} not a valid input.\n")
            u_number = input("Please enter a 4 digit number: ")
        for i in range(0,4):
            if u_number[i] == g_number[i]:
                cows_bulls[0] +=1
            elif g_number[i] in u_number:
                cows_bulls[1] +=1
        print(f"{cows_bulls[0]} cows and {cows_bulls[1]} bulls")
        c +=1
    return True, c


def run(): 
    g_number = str(random.randint(1000,9999))
    cows_bulls = [0,0]
    game, c = cows_bulls_checker(cows_bulls, g_number)
    if game:
        print(f"You win! {g_number} was the number, and it only took you {c} attempts.")
    else:
        print(f"Too bad!, the number was {g_number}")


if __name__=="__main__":
    run()