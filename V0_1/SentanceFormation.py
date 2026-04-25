from . import Vocabulary
import os
def GetPromptType(TokenizedInput):
    PromptTypeIndicators = {#not used in this version
        "What":"Question",
        "?":"Question"
    }

    for CurrentWord in range(len(TokenizedInput)):#loop through all the tokenized words
        UnTokenizedWord = Vocabulary.Vocab[TokenizedInput[CurrentWord]]
        if PromptTypeIndicators.get(UnTokenizedWord):
            pass
# new way data works is i feed it answers only and it picks the best fitting one and responds with that

def Start(TokenizedInput):
    PromptData = {#not used in this version yet
        "Type":""
    }
    PromptType = GetPromptType(TokenizedInput)

    BestLine = None
    BestLineAmountOfMatchingWords = 0

    CurrentAmountOfMatchingWords = 0
    for CurrentWord in range(len(TokenizedInput)):#loop through all the tokenized words
        UnTokenizedWord = Vocabulary.Vocab[TokenizedInput[CurrentWord]]
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, "Data.txt"), "r") as f:
            for line in f:
                line = line.strip()  # removes \n
                LineList = line.split()
                for i in range(len(LineList)):#starts looping through the current line of data
                    if LineList[i] == UnTokenizedWord:
                        CurrentAmountOfMatchingWords +=1

                if CurrentAmountOfMatchingWords > BestLineAmountOfMatchingWords:
                    BestLine = line
                    BestLineAmountOfMatchingWords = CurrentAmountOfMatchingWords
                    CurrentAmountOfMatchingWords = 0
                elif BestLine == None:
                    BestLine = line
                    BestLineAmountOfMatchingWords = CurrentAmountOfMatchingWords
                    CurrentAmountOfMatchingWords = 0
                else:
                    CurrentAmountOfMatchingWords = 0
                    pass
                    
    return BestLine