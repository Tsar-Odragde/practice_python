import string
import random

def run():
    char_list = list(string.printable)[0:94]
    password_lenght = int(input("How many characters you want in your password?: "))
    print("".join(random.sample(char_list, password_lenght)))


if __name__=="__main__":
    run()