import random
list1=['普通','稀有','传说']
name=list1[random.randint(0,len(list1)-1)]
print(name)
num=50
num2=40
if name=='普通':
    while True:
        i=0
        list2=[]
        while i<3:
            i=i+1
            a=random.randint(30,70)
            list2.append(a)
        print(list2)
        num1=list2[random.randint(0,len(list2)-1)]
        print(num1)
        list3=[1,2]
        name1=list3[random.randint(0,len(list3)-1)]
        if name1==1:
            num=num1+num
            print(num)
        elif name1==2:
            num=num1-num
            print(num)
        if num>100:
            print('任务成功你的分数为',num)
            break
        elif num <= 0:
            print('任务失败你的分数为',num)
            break
if name=='稀有':
    while True:
        i=0
        list2=[]
        while i<3:
            i=i+1
            a=random.randint(30,70)
            list2.append(a)
        print(list2)
        num1=list2[random.randint(0,len(list2)-1)]
        print(num1)
        list3=[1,2]
        name1=list3[random.randint(0,len(list3)-1)]
        if name1==1:
            num=num1+num2
            print(num)
        elif name1==2:
            num=num1-num2
            print(num)
        if num>100:
            print('任务成功你的分数为',num)
            break
        elif num <= 0:
            print('任务失败你的分数为',num)
            break
if name=='传说':
    while True:
        i=0
        list2=[]
        while i<3:
            i=i+1
            a=random.randint(30,70)
            list2.append(a)
        print(list2)
        num1=list2[random.randint(0,len(list2)-1)]
        print(num1)
        list3=[1,2]
        name1=list3[random.randint(0,len(list3)-1)]
        if name1==1:
            num=num1+num
            print(num)
        elif name1==2:
            num=num1+num
            print(num)
        if num>100:
            print('任务成功你的分数为',num)
            break
        elif num <= 0:
            print('任务失败你的分数为',num)
            break