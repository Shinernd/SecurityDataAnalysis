import random
import pandas as pd

IndividualList = []
Set = []

member = 1000
exclim = 100

def Intemp():
    in_rand = random.random() # 출근시간 범위
    if in_rand < 0.03: # 3% (7.0~7.5)
        temp = 0
    elif 0.03 <= in_rand < 0.08: # 5% (7.5~8.0)
        temp = 1
    elif 0.08 <= in_rand < 0.2: # 12% (8.0~8.5)
        temp = 2
    elif 0.2 <= in_rand < 0.95: # 75% (8.5~9.0)
        temp = 3
    else: # 5% (9.0~0.5)
        temp = 4
    return temp

def Outtemp():
    out_rand = random.random() # 퇴근시간 범위
    if out_rand <= 0.3: # 30% (18.0~19.0)
        temp = 0
    elif 0.3 < out_rand <= 0.65: # 35% (19.0~20.0)
        temp = 1
    elif 0.65 < out_rand <= 0.85: # 20% (20.0~21.0)
        temp = 2
    else: # 15% (21.0~22.0)
        temp = 3
    return temp
    
            
class Individual:
    def __init__(self, index, flag):
        self.index = index
        self.flag = flag
        self.Intime()
        self.Outtime()

    def Intime(self):
        temp = Intemp()
        rand_tm = random.random()/2
        self.in_last = '%.3f' %(7.0 + temp * 0.5 + rand_tm)
        if self.flag:
            rand_tm = random.random()/2
            self.in_new = '%.3f' %(7.0 + temp * 0.5 + rand_tm)
        else:
            temp = Intemp()
            rand_tm = random.random()/2
            self.in_new = '%.3f' %(7.0 + temp * 0.5 + rand_tm)
            
    def Outtime(self):
        temp = Outtemp()
        rand_tm = random.random()
        self.out_last = '%.3f' %(18.0 + temp + rand_tm)
        if self.flag:
            rand_tm = random.random()
            self.out_new = '%.3f' %(18.0 + temp + rand_tm)
        else:
            temp = Outtemp()
            rand_tm = random.random()
            self.out_new = '%.3f' %(18.0 + temp + rand_tm)

cnt = 0
for i in range(member):
    flag = 1
    while cnt < exclim:
        rand_exc = random.random()
        if rand_exc < 0.1:
            flag = 0
            cnt += 1
        else:
            break
    ind = Individual(i+1, flag)
    IndividualList.append(i+1)
    IndividualList.append(ind.in_last)
    IndividualList.append(ind.out_last)
    IndividualList.append(ind.in_new)
    IndividualList.append(ind.out_new)
    Set.append(IndividualList)
    IndividualList = []

df = pd.DataFrame.from_records(Set, columns=['ID', 'In(Last)', 'Out(Last)', 'In(New)', 'Out(New)'])
print(df)
writer = pd.ExcelWriter('commute.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
