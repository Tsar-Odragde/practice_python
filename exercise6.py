def run():
    string = str(input("Please enter a word or phrase to evaluate if it is a palindrome: ")).replace(" ", "").replace(",", "").replace(".", "").replace(":", "").replace(";", "").lower().strip()
    if string == string[::-1]:
        print("That's a palindrome.")
    else:
        print("That isn't a palindrome.")


if __name__ == "__main__":
    run()