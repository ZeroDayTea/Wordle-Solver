#!/usr/bin/env python3

#if a 1 was input for accuracy add it to the list of yellow characters
def generateYellow(word, accuracy):
    for i in range(0, len(accuracy)):
        if accuracy[i] == '1' and word[i] not in yellowLetters:
            yellowLetters.append(word[i])
#if a 2 was input for accuracy change the known characters list accordingly
def generateGreen(word, accuracy):
    for i in range(0, len(accuracy)):
        if accuracy[i] == '2':
            greenLetters[i] = word[i]
#if a 0 was input for accuracy add it to the list of not allowed characters
def generateGrey(word, accuracy):
    lettersincurrentword = []
    for i in range(0, len(accuracy)):
        if accuracy[i] == '0' and word[i] not in lettersincurrentword:
            greyLetters.append(word[i])
        lettersincurrentword.append(word[i])

#run through all possible word guesses and remove the ones that are impossible
def updatePossibleWords():
    wordstoremove = []
    for word in possibleWords:
        matches = True
        
        #if word has a grey letter, doesn't contain one of the yellows, or does not have a green in the right spot then it isn't possible
        for letter in greyLetters:
            if letter in word:
                matches = False
        for letter in yellowLetters:
            if letter not in word:
                matches = False
        for i in range(len(greenLetters)):
            letterExact = greenLetters[i]
            if letterExact != word[i] and letterExact != '0':
                matches = False
        
        if matches == False:
            wordstoremove.append(word)
    #append words to removal list and remove them afterwards to prevent hopscotch errors in list traversal
    for removeword in wordstoremove:
        possibleWords.remove(removeword)

def main():    
    for iteration in range(1, 6):
        #first iteration is different and allows the user to input their first guess
        if iteration == 1:
            firstWord = input("Enter your first guess (adieu, aeris, etc): ").strip() #adieu and aeris are good suggestions
            if len(firstWord) != 5: #first word cannot be longer than 5 chars
                print("Not a valid 5 letter word")
            firstAccuracy = input("Enter the accuracy of your first word as a string of 0s, 1s, and 2s (0 grey, 1 yellow, 2 green) e.g. '01201': ").strip()
            if len(firstAccuracy) != 5: #accuracy string must be length of wordle word
                print("Not a valid 5 letter accuracy")
            elif firstAccuracy == '22222': #win case
                print("Congratulations!")
                exit()
            else:
                #update all letter dictionaries and asses them to remove impossible words
                generateYellow(firstWord, firstAccuracy)
                generateGreen(firstWord, firstAccuracy)
                generateGrey(firstWord, firstAccuracy)
                updatePossibleWords()
                currentGuess = possibleWords[0]
                possibleWords.remove(currentGuess)
                print("Input {} as your next guess".format(currentGuess))
        else:
            #all other iterations 
            accuracy = input("Enter the accuracy of '{}' as a string of 0s, 1s, and 2s (0 grey, 1 yellow, 2 green) e.g. '01201': ".format(currentGuess)).strip()
            if len(accuracy) != 5: #accuracy string must be length of wordle word
                print("Not a valid 5 letter accuracy")
            elif accuracy == '22222': #win case
                print("Congratulations!")
                exit()
            else:
                #update all letter dictionaries and asses them to remove impossible words
                generateYellow(currentGuess, accuracy)
                generateGreen(currentGuess, accuracy)
                generateGrey(currentGuess, accuracy)
                updatePossibleWords()
                currentGuess = possibleWords[0]
                possibleWords.remove(currentGuess)
                print("Input {} as your next guess".format(currentGuess))
    print("Ran out of guesses :(") #theoretically impossible with this bot

if __name__ == "__main__":
    #initialize all variables including list of all word guesses and variables used to rule out guesses
    with open('sortedwordlist.txt', 'r') as f:
        possibleWords = [line.rstrip() for line in f.readlines()]

    yellowLetters = []
    greenLetters = ['0','0','0','0','0']
    greyLetters = []
    currentGuess = ""
    main()
