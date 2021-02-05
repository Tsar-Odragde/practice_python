def run():
    s = input("Please write a sentence: ")
    print(" ".join(s.split()[::-1]))


if __name__=="__main__":
    run()