doc=["When I find myself in times of trouble"
,"Mother Mary comes to me"
,"Speaking words of wisdom, let it be"
,"And in my hour of darkness"
,"She is standing right in front of me"
,"Speaking words of wisdom, let it be"

,'Let it be, let it be'
,'Let it be, let it be'
,'Whisper words of wisdom, let it be'

,'And when the broken-hearted people'
,'Living in the world agree'
,'There will be an answer, let it be'
,'For though they may be parted'
,'There is still a chance that they will see'
,'There will be an answer, let it be'

,'Let it be, let it be'
,'Let it be, let it be'
,'Yeah, there will be an answer, let it be'
,'Let it be, let it be'
,'Let it be, let it be'
,'Whisper words of wisdom, let it be'

,'Let it be, let it be'
,'Ah, let it be, yeah, let it be'
,'Whisper words of wisdom, let it be'

,'And when the night is cloudy'
,'There is still a light that shines on me'
,'Shine on until tomorrow, let it be'
,'I wake up to the sound of music'
,'Mother Mary comes to me'
,'Speaking words of wisdom, let it be'

,'Let it be, let it be'
,'Let it be, yeah, let it be'
,'Oh, there will be an answer, let it be'
,'Let it be, let it be'
,'Let it be, yeah, let it be'
,'Whisper words of wisdom, let it be']


def countWords(doc):
    d = {}
    for sentence in doc:
        words=sentence.split()
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
    return d

def getWordsFreqGreater(c,d):
    w=list()
    for k in d:
        if d[k]>c:
            w.append(k)
    return w

wordDict=countWords(doc)
freqWordsList=getWordsFreqGreater(2,wordDict)
print "Frequent words: ",freqWordsList