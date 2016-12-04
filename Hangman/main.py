import random

def getphrase():
    f = open('phrases.txt', 'r')
    ps = f.readlines()
    i = int(len(ps) * random.random())
    f.close()

    return ps[i]

def checkguess(phrase, guess, g):
    l = list(guess)
    i = phrase.find(g)
    while (i != -1 and i < len(phrase)):
        l[i] = g
        i = phrase.find(g, i+1)
    return "".join(l)

def prompt(phrase, guess, attempts):
    print('current answer: ' + guess)
    left = 7 - len(attempts)
    paren = ''
    if (len(attempts) != 0):
        paren = ' (' + ','.join(attempts) + ')'
    g = input(str(left) + ' attempts left' + paren + '. what is your guess? ')
    if (g not in attempts and guess.find(g) == -1):
        guess = checkguess(phrase, guess, g)
        if (guess.find(g) == -1):
            attempts.add(g)
    return guess

def __main():
    phrase = getphrase()
    guess = ''.join(map(lambda c: '?' if c.isalpha() else c, phrase))

    print('Welcome to Hangman.')
    attempts = set()

    while (phrase != guess and len(attempts) < 7):
        guess = prompt(phrase, guess, attempts)

    if (phrase == guess):
        print('you won: "' + phrase + '"!')
    else:
        print('sorry, you were hung')

__main()