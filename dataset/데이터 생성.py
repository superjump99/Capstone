import random
import pandas as pd
import numpy as np
df = pd.read_csv('MergeDate.csv')
total = len(df)

numOfData = len(df) * 0.2

Q_value_count = df['Quantity'].value_counts().sort_index()
D_value_count = df['Discount'].value_counts().sort_values()



qmin, qmax = df['Quantity'].min(), df['Quantity'].max()
smin, smax = df['Sales'].min(), df['Sales'].max()
dmin, dmax = df['Discount'].min(), df['Discount'].max()
pmin, pmax = df['Profit'].min(), df['Profit'].max()

weights = (np.array(Q_value_count) / sum(Q_value_count)) * 100


Salesinter = [ 161, 743, 599, 199, 96, 50, 39, 18, 16, 11, 9, 47]
Profitinter = [ 23, 22, 61, 537, 411, 418, 226, 116, 75, 32, 28, 16, 23]

Sprob,Pprob = [],[]
for i in Salesinter:
    prob = i / total
    Sprob.append(prob)
print(Sprob)
for i in Profitinter:
    prob = i / total
    Pprob.append(prob)
print(Pprob)


def makeSales(prob):
    if prob == 0:
        Sales = random.uniform(1.7,50)
    elif prob == 1:
        Sales = random.uniform(50,150)
    elif prob == 2:
        Sales = random.uniform(150,250)
    elif prob == 3:
        Sales = random.uniform(250,350)
    elif prob == 4:
        Sales = random.uniform(350,450)
    elif prob == 5:
        Sales = random.uniform(450,550)
    elif prob == 6:
        Sales = random.uniform(550,650)
    elif prob == 7:
        Sales = random.uniform(750,850)
    elif prob == 8:
        Sales = random.uniform(850,950)
    elif prob == 9:
        Sales = random.uniform(950,1050)
    elif prob == 10:
        Sales = random.uniform(1050,1150)
    else:
        Sales = random.uniform(1150,smax)
    return Sales

def makeProfits(prob):
    if prob == 0:
        Profit = random.uniform(pmin,-250)
    elif prob == 1:
        Profit = random.uniform(-250,-150)
    elif prob == 2:
        Profit = random.uniform(-150, -50)
    elif prob == 3:
        Profit = random.uniform(-50, 50)
    elif prob == 4:
        Profit = random.uniform(50, 150)
    elif prob == 5:
        Profit = random.uniform(150, 250)
    elif prob == 6:
        Profit = random.uniform(250, 350)
    elif prob == 7:
        Profit = random.uniform(350, 450)
    elif prob == 8:
        Profit = random.uniform(450, 550)
    elif prob == 9:
        Profit = random.uniform(550, 650)
    elif prob == 10:
        Profit = random.uniform(650, 750)
    elif prob == 11:
        Profit = random.uniform(750, 850)
    else:
        Profit = random.uniform(850, qmax)
    return Profit


# print(len(weights))
# print(range(0,9))
# print(qmin,qmax, smax, smin, dmax ,dmin,pmax,pmin)
# print(range(qmin, len(weights)+1))

# Quantity Sales Discount Profit
Q, S, D, P = [], [], [], []
for _ in range(int(numOfData)):
    Quantity = random.choices(range(qmin, len(weights)+1), weights = weights)
    sprob = random.choices(range(0, 12), weights=Sprob)[0]
    Sales = makeSales(sprob)
    Discount = random.choices(range(0, 9), weights=[0.89, 0.27, 0.75, 0.57, 0.40, 0.33, 0.27, 0.24, 0.1])
    pprob = random.choices(range(len(Profitinter)), weights=Pprob)[0]
    Profit = makeProfits(pprob)
    Q.append(Quantity[0])
    S.append(Sales)
    D.append(Discount[0] * 0.1)
    P.append(Profit)

data = {'Quantity' : Q,
        'Sales' : S,
        'Discount' : D,
        'Profit' : P}
vData = pd.DataFrame(data)
# print(vData.head())
vData.to_csv("weak_test3.csv")