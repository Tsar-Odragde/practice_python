import random


def run(): 
    a = str(random.randint(1000,9999))
    r_num = []
    c = 1
    for i in a:
        r_num.append(int(i))
    user = input("Enter a 4 digit number: ")
    while user != a:
        c +=1
        user_num = []
        bulls = 0
        cows = 0
        for i in user:
            user_num.append(int(i))
        for k in range(0,4):
            if user_num[k] == r_num[k]:
                cows +=1
                continue
            else:
                for i in user_num:
                    if i == r_num[k]:
                        bulls += 1
        if user_num == r_num: break
        print(f"{cows} cows and {bulls} bulls")
        user = input("Enter a 4 digit number: ")
    print(f"You win!, and only took you {c} attempts.")


if __name__=="__main__":
    run()