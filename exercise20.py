import random


def binary_search(random_list,number):
    start = 0
    end = len(random_list) - 1
    while True:
        middle = int((end + start)/2)
        if (end - start)/2 < 1: 
            return False
        if random_list[middle] == number: 
            return True
        elif random_list[middle] < number: 
            start = middle
        else: 
            end = middle


def run():
    random_list = sorted([random.randint(0,100) for _ in range(random.randint(0,100))])
    print(random_list)
    number = int(input("Please enter a number in the range 0-99: "))
    print(binary_search(random_list, number))


if __name__=="__main__":
    run()