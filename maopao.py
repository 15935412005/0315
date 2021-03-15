'''冒泡算法'''
def maopao(list):
    for n in  range(len(list)-1):
        for i in range(len(list)-1-n):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
        return list

list=[1,-95,69,45,21,-222,36,66,88,89,54]
max=maopao(list)[-1]
print(max)

list=[1,-95,69,45,21,-222,36,66,88,89,54]
print(sorted(list)[-1])