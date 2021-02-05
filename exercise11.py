def check_primality(number):
    if number in range(2,number+1):
        a = [n for n in range(1,number+1) if (number%n == 0)]
        if len(a) == 2:
            return True


def run():
    num = int(input("Enter the integer you want to check: "))
    if check_primality(num):
        print(f"\n{num} is a prime number.")
    else:
        print(f"\n{num} isn't a prime number")


if __name__ == "__main__":
    run()