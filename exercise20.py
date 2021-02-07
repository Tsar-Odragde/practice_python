import random


def binary_search(a,b):
    s_i = 0
    e_i = len(a) - 1
    c = 0
    while True:
        m_i = int((e_i + s_i)/2)
        if m_i < s_i or m_i > e_i or m_i < 1 or c > 99: return False
        m_e = a[m_i]
        if m_e == b: return True
        elif b > m_e: s_i = m_i
        else: e_i = m_i
        c +=1


def run():
    a = sorted([random.randint(0,100) for _ in range(random.randint(0,100))])
    b = int(input("Please enter a number in the range 0-99: "))
    print(binary_search(a,b))
    print(a)


if __name__=="__main__":
    run()