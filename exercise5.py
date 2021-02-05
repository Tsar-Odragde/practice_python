import random


def run():
    a = [random.randint(0,100) for _ in range(0,random.randint(0,51))]
    b = random.sample(range(101),random.randint(0,50))
    c = list(dict.fromkeys([n for n in a if n in b])) #This whole line can be replaced by: [n for n in set(a) if n in b]
    print(f"a = {sorted(a)}")
    print(f"b = {sorted(b)}")
    print(f"c = {sorted(c)}")


if __name__ == "__main__":
    run()