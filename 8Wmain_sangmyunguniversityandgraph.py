word='sangmyung university'
def countChars(word):
    d = dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    return d


print countChars(word)

import matplotlib
import matplotlib.pyplot as plt
plt.bar(range(len(countChars(word))), countChars(word).values(), align='center')
plt.xticks(range(len(countChars(word))), list(countChars(word).keys()))
plt.show()


def lab7():
    countChars(word)

def main():
    lab7()
    word='sangmyung university'

if __name__=="__main__":
	main()