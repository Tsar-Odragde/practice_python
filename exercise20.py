import random


def run():
    a = sorted([random.randint(0,100) for _ in range(random.randint(0,100))])
    b = int(input("Please enter a number in the range 0-99: "))
    bol = b in a
    if bol: print(True)
    else: print(False)


if __name__=="__main__":
    run()