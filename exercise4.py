def run():
    a = int(input("Please enter a number to divide: "))
    for i in range(1, a+1):
        if a%i == 0:
            print(i)


if __name__ == "__main__":
    run()
