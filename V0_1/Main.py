from . import Tokenizer, SentanceFormation#this is so version selector works

IsProcessing = False
SeeThoughtProcess = True
################
# How this works
# tokenizes the input
# gets the most fitting data from a data set
# adds some formating like uppercase first letter and add periods(may not be needed once full data set is in)
IsRunning = False
def Run():
    global IsProcessing, IsRunning
    IsRunning = True
    while IsRunning:# loop so the ai works more than once
            if not IsProcessing:# if the ai is not currently proccessing a message then start processing a message
                IsProcessing = True # set it so it doesnt try to get inputs while its procces the previous input
                UserInput = input("Type here")#ask for an input
                TokenizedOutput = Tokenizer.Tokenize(UserInput)# get the tokenized version of the input

                if Tokenizer.TokenizationErrored:#if the tokenizer errored than print the error
                    print(TokenizedOutput)
                else:# if the tokenizer didnt error start working on the next part
                    print(SentanceFormation.Start(TokenizedOutput))
                IsProcessing = False#set is process to false so it starts the process again