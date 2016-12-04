import re

def choosestory():
    madlibs = open('madlibs.txt')
    files = madlibs.readlines()
    for i, f in enumerate(files):
        print(str(i+1) + ': ' + f.strip())
    c = input('choose a file number: ')
    madlibs.close()
    return files[int(c)-1].strip() 

def readstory(s):
    f = open(s)
    story = f.read()
    f.close()
    return story

def getresponses(story):
    prog = re.compile('<.*?>')
    m = prog.search(story)
    while m != None:
        print(m.string[m.start()+1:m.end()-1])
        m = prog.search(story, m.end())

print('welcome to mad libs')
name = input('what is your name? ')
print ('let\'s make a story, ' + name)
storyname = choosestory()
print('let\'s start ' + storyname)
story = readstory(storyname)
getresponses(story)