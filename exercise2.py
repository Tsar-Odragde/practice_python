def run():
    num = int(input("Enter a number: "))
    check = int(input("Enter another number: "))
    if (num%4) == 0:
        print(f"{num} is a multiple of 4.")
    elif (num%2) == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
    if num%check == 0:
        print(f"{num} can be divided evenly by {check}")
    else:
        print(f"{num} can NOT be divided evenly by {check}")
    


if __name__ == "__main__":
    run()