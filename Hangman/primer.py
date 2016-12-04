# Read phrases from a file
#    So that we can add easily
#    Choose a phrase at random
# Show user prompt
#    Give the number of misses left, and the letters that were misses
#    If the letter is in the phrase, fill in blank(s)
#       If the phrase is complete, the player wins
#    If not, add a body part to the gallows
#       Head, body, arm, arm, leg, leg
#    If there are no more body parts, the player loses

def getphrase():
    return 'i love programming'

def updateguess(phrase, guess, resp):
    i = phrase.find(resp)
    while (i != -1):
        guess = guess[0:i] + resp + guess[i+1:]
        i = phrase.find(resp, i+1)
    return guess

print('welcome to hangman')
response = input('what is your name? ')
print ('good luck in hangman, ' + response)
phrase = getphrase()
print('the phrase is: ' + phrase)
guess = ''
for c in phrase:
    if (c.isalpha()):
        guess = guess + '?'
    else:
        guess = guess + c
print('current guess: ' + guess)

attempts = set()
while len(attempts) < 6 and guess != phrase:
    resp = input('what is your guess? ')
    if phrase.find(resp) == -1:
        attempts.add(resp)
    else:
        guess = updateguess(phrase, guess, resp)
    print('current guess: ' + guess)

if guess == phrase:
    print('Winner!')
else:
    print('Sorry, you lose')