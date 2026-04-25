from . import Vocabulary
TokenizationErrored = False
def Tokenize(UserInput):
    global TokenizationErrored # this is so main.py knows that it errored and doesnt keep going and cause crashes
    TokenizationErrored = False
    Output = ""
    UnknownWords = []
    try:
        UserInput = str(UserInput)
        SplitUserInput = UserInput.split()
    except:
        TokenizationErrored = True
        Output = "Failed to convert input to str"
    
    
    for CurrentWord in SplitUserInput:
        if not CurrentWord.lower() in Vocabulary.Vocab:
            UnknownWords.append(CurrentWord)
    
    if len(UnknownWords) >= 1:
        TokenizationErrored = True
        Output = "Some word(s) are not my database: ",UnknownWords

    else:
        Output = []
        for CurrentWord in range(len(SplitUserInput)):# for every word the user inputs start the second loop to find the token for that word

            if len(Output) >= len(SplitUserInput): #check if the current amount of tokens is the same as the amount of words so it doesnt do more checks than needed
                return Output

            for CurrentVocab in range(len(Vocabulary.Vocab)):
                CurrentToken = ""

                if str(SplitUserInput[CurrentWord]) == str(Vocabulary.Vocab[CurrentVocab]):#if the current word i am looking for is in the vocab append its id
                    Output.append(CurrentVocab)

        return Output

    if TokenizationErrored:
        return Output
        