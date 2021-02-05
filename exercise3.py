def run():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    c = int(input("Please enter a number: "))
    print([n for n in a if n < c])


if __name__ == "__main__":
    run()