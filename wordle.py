from random import randint
from colorama import init as color_text
from termcolor import colored

def fillWordList(wordlist_file):
    with open(wordlist_file, "r") as f:
        g = f.readlines()
        f.seek(0)
        t=[]
        for i in g:
            t.append(i[:-1])
    return(t)

def pickWord(word_list):
    random_range = randint(1,len(word_list)-1)    
    word = word_list[random_range]
    return(word)

def verifyWord(word,guess):
    pos = ""
    for j in range (0,len(word)):
        if guess[j] == word[j]:
            pos = (pos + colored(guess[j],"green"))
        elif guess[j] in word:
            pos = (pos + colored(guess[j],"yellow"))
        else:
            pos = (pos + colored(guess[j],"red"))
    return(pos,word==guess)

color_text()
wordlist = fillWordList("wordlist.txt")
word = pickWord(wordlist)
#print(word)
print("Try guessing the word")
k = 0
tries = 6
while True:
    tries = tries-1
    k = k + 1
    while True:
        guess = str(input("You have "+str(tries)+" chance(s) left to do so:   "))
        if (len(guess) == 5 and guess in wordlist):
            break
        elif (len(guess) != 5):
            print(colored("Invalid word! must have 5 letters","red"))
        elif (guess not in wordlist):
            print(colored("Word not in word list!","red"))
    ton = verifyWord(word,guess)
    if (ton[1]==True):
        print ("Correct!\nIt took you "+str(k)+" tries.")
        break
    if (k == 5):
        print("You Failed.")
        print("It's " + '"' + word + '"')
        break
    print(ton[0])