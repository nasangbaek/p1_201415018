

def finddict(word):
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d

def lab7():
    word='sangmyung university'
    finddict(word)

lab7()