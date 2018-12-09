import random
import pandas as pd

IndividualList = []
Set = []

member = 1000
exclim = 100

def Prttemp():
    prt_rand = random.random() # 프린터 사용 횟수 범위
    if prt_rand < 0.3: # 30% (0~20)
        temp = 0
    elif 0.3 <= prt_rand < 0.8: # 50% (20~40)
        temp = 1
    else: # 20% (40~60)
        temp = 2
    return temp

def Emltemp():
    eml_rand = random.random() # 이메일 전송 횟수 범위
    if eml_rand <= 0.5: # 50% (0~4)
        temp = 0
    elif 0.5 < eml_rand <= 0.8: # 30% (5~8)
        temp = 1
    else: # 20% (9~12)
        temp = 2
    return temp

def Cldtemp():
    cld_rand = random.random() # 클라우드 이용 횟수 범위
    if cld_rand <= 0.5: # 50% (0~3)
        temp = 0
    elif 0.5 < cld_rand <= 0.8: # 30% (4~6)
        temp = 1
    else: # 20% (7~9)
        temp = 2
    return temp
            
class Individual:
    def __init__(self, index, flag):
        self.index = index
        self.flag = flag
        self.Prtuse()
        self.Emlsend()
        self.Clduse()

    def Prtuse(self):
        temp = Prttemp()
        rand_use = int(random.random() * 20)
        self.printer_last = temp * 20 + rand_use
        if self.flag:
            rand_use = int(random.random() * 20)
            self.printer_new = temp * 20 + rand_use
        else:
            temp = Prttemp()
            rand_use = int(random.random() * 20)
            self.printer_new = temp * 20 + rand_use

    def Emlsend(self):
        temp = Emltemp()
        rand_send = int(random.random() * 4)
        self.email_last = temp * 4 + rand_send
        if self.flag:
            rand_send = int(random.random() * 4)
            self.email_new = temp * 4+ rand_send
        else:
            temp = Emltemp()
            rand_send = int(random.random() * 4)
            self.email_new = temp * 4 + rand_send

    def Clduse(self):
        temp = Cldtemp()
        rand_use = int(random.random() * 3)
        self.cloud_last = temp * 3 + rand_use
        if self.flag:
            rand_use = int(random.random() * 3)
            self.cloud_new = temp * 3 + rand_use
        else:
            temp = Cldtemp()
            rand_use = int(random.random() * 3)
            self.cloud_new = temp * 3 + rand_use

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
    IndividualList.append(ind.printer_last)
    IndividualList.append(ind.email_last)
    IndividualList.append(ind.cloud_last)
    IndividualList.append(ind.printer_new)
    IndividualList.append(ind.email_new)
    IndividualList.append(ind.cloud_last)
    Set.append(IndividualList)
    IndividualList = []
    print(flag)

df = pd.DataFrame.from_records(Set, columns=['ID', 'Printer(Last)', 'Email(Last)', 'Cloud(Last)', 'Printer(New)', 'Email(New)', 'Cloud(New)'])
print(df)
writer = pd.ExcelWriter('system.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
