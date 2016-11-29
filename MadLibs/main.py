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
    rs = list()
    prog = re.compile('<.*?>')
    m = prog.search(story)
    while m != None:
        rs.append(input(m.string[m.start()+1:m.end()-1] + ': '))
        m = prog.search(story, m.end())
    return rs

def tellstory(story, responses):
    prog = re.compile('<.*?>')
    last = 0
    r = 0
    m = prog.search(story)
    while m != None:
        print(story[last:m.start()-1], end='')
        print(' '+responses[r]+' ', end='')
        r=r+1
        last = m.end() + 1
        m = prog.search(story, m.end())
    print(story[last:])

def __main():
    s = choosestory()
    story = readstory(s)
    responses = getresponses(story)
    tellstory(story, responses)

__main()