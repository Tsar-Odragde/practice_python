def gen_fib(n):
    a = [1, 1]
    [a.append(a[-1] + a[-2]) for _ in range(1,n+1)]
    return a[0:-2]


def run():
    n_fib = int(input("How many Fibonacci numbers you want to generate?: "))
    print(gen_fib(n_fib))


if __name__=="__main__":
    run()