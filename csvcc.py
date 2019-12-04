import pandas as pd
from datetime import *
import csv
import shutil
from dateutil.parser import parse

dtnow=datetime.now()
fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
dt1=input("Please Enter First Value(YYYY-MM-DD HH:MM:SS):-")
td1=parse(dt1)
dt2=input("Please Enter Second Value(YYYY-MM-DD HH:MM:SS):-")
td2=parse(dt2)
shutil.copy('ssss.csv','temp\ dupliss.csv')
with open(fdt+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date and Time","Temprature(C)"])
df = pd.read_csv('temp\ dupliss.csv')
final= df['Date'] +" "+ df['Time']
a= df['Date'] +" "+ df['Time']
dtlen=len(a)
x=1
new=a
while(x<dtlen):
    new[x]=parse(a[x])
    x+=1
print(type(new[1]))
print(new)
df['Date']=new
df['Date'][0]=parse(df['Date'][0])
x=0
dtlen=len(df['Date'])
while(x<dtlen):
    if (td1<df['Date'][x]):
        if (td2>df['Date'][x]):
            with open(fdt+".csv","a", newline='') as file2:
                writerr=csv.writer(file2)
                writerr.writerow([str(df['Date'][x]),str(df['Temprature'][x])])
    x=x+1
