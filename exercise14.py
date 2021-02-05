import random

def run():
    a = sorted([random.randint(0,20) for _ in range(1,random.randint(1,20))])
    a_without_dupes1 = []
    [a_without_dupes1.append(n) for n in a if n not in a_without_dupes1]
    a_without_dupes2 = list(set(a))
    a_without_dupes3 = list(dict.fromkeys(a))
    print(a)
    print(a_without_dupes1)
    print(a_without_dupes2)
    print(a_without_dupes3)


if __name__=="__main__":
    run()