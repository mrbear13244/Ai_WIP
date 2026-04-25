import V0_1.Main as Version_0_1,V0_1.Tokenizer as Tokenizer

while True:
    UserInput = input("Type the version you want to run the current options are 0.1")

    if UserInput == "0.1":
        Version_0_1.Run()
    else:
        print("Thats not a version current options are 0.1")