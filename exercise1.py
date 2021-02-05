def run():
    current_year = int(input("Enter the current year: "))
    name = str.title(input("What's your name: "))
    age = int(input("How old are you: "))
    iterations = int(input("Enter a number: "))
    century_year = current_year - age + 100
    print(f"You, {name} will turn 100 years old in {century_year}\n" * iterations)


if __name__ == "__main__":
    run()