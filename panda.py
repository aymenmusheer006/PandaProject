import pandas as pd
from datetime import *
from dateutil.parser import parse
df = pd.read_csv('ssss.csv')
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
print(df)
dt1=input("Please Enter First Value(YYYY-MM-DD HH:MM:SS):-")
td1=parse(dt1)
dt2=input("Please Enter Second Value(YYYY-MM-DD HH:MM:SS):-")
td2=parse(dt2)
df['Date'][0]=parse(df['Date'][0])
x=0
dtlen=len(df['Date'])
print("Date & Time\t\tTemprature(C)")
while(x<dtlen):
    if (td1<=df['Date'][x]):
        if (td2>=df['Date'][x]):
            print(final[x]+"\t\t"+str(df['Temprature'][x]))
    x+=1

