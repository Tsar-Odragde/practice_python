import random


def cows_bulls_checker(cows_bulls, g_number, u_number):
    for i in range(0,4):
        if u_number[i] == g_number[i]:
            cows_bulls[0] +=1
        elif g_number[i] in u_number:
            cows_bulls[1] +=1
    return cows_bulls


def run(): 
    g_number = str(random.randint(1000,9999))
    cows_bulls = [0,0]
    c = 1
    while cows_bulls[0] != 4:
        cows_bulls = [0,0]
        u_number = input("Enter a 4 digit number: ")
        cows_bulls = cows_bulls_checker(cows_bulls, g_number, u_number)
        print(f"{cows_bulls[0]} cows and {cows_bulls[1]} bulls")
        c +=1
    if cows_bulls[0] == 4:
        print(f"You win! {g_number} was the number, and it only took you {c} attempts.")


if __name__=="__main__":
    run()