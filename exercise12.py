import random


def run():
    a = sorted([random.randint(0,100) for _ in range(random.randint(0,100))])
    b = ([a[0], a[len(a)-1]]) #We can replace 'len(a)-1' for '-1'
    print(f"a = {a}")
    print(f"b = {b}")


if __name__=="__main__":
    run()