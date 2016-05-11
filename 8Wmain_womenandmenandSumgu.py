
data=[
    [74425, 76326],
    [61164, 61636],
    [109688, 115744],
    [144796, 146776],
    [174996, 181676],
    [177841, 177434],
    [204630, 205980],
    [223373, 232245],
    [161055, 166130],
    [171576, 176735],
    [279169, 293772],
    [239450, 251066],
    [148690, 156510],
    [182977, 196992],
    [237792, 242641],
    [283869, 296762],
    [209344, 210282],
    [118965, 114441],
    [186503, 186856],
    [195734, 203014],
    [254381, 249472],
    [212401, 229111],
    [271654, 295354],
    [319197, 335045],
    [229829, 231671]
]
print data

sumM=0
sumF=0
for gu in data:
    sumM+=gu[0]
    sumF+=gu[1]
print sumM,sumF
print "men average=",float(sumM)/len(data)
print "women average=",float(sumF)/len(data)

sumGu=list()
for gu in data:
    sumGu.append(gu[0]+gu[1])

print sumGu

%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
# 2단계로 나누어 그림
plt.bar(range(len(sumGu)), sumGu, align='center')
#plt.xticks(range(len(d)), list(d.keys()))
plt.show()
