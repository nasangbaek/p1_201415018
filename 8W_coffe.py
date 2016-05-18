allData=[ ["Coffee","Water","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes","No"],
    ["Affogato","No","No","Yes"]]

data1=allData[1:]


count=0
for i in data1:
    if i[2].upper()=='YES':
        count+=1
print "Number of Coffee adding Milk",count
print "% of coffee with milk: ",100*count/float(len(data1))