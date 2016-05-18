
marks=[['Subject','scores'],
    ['English', 100],
    ['Math', 80],
    ['English', 70],
    ['Math', 100],
    ['English', 82.3],
    ['Math', 98.5]]

marks=marks[1:]

# reading and compute average
englishSum=0
mathSum=0
englishCount=0
mathCount=0
for row in marks:
    subj = row[0]
    mark = int(row[1])
    if subj=="English":
        englishSum+=mark
        englishCount+=1
    elif subj=="Math":
        mathSum+=mark
        mathCount+=1
    else:
        pass
print mathSum,englishSum
print float(mathSum/mathCount),float(englishSum/englishCount)