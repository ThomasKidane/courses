list=[[1,0]]
for i in range(int(1e7)):
    list.append([(5*list[-1][0]-12*list[-1][1])/13,(12*list[-1][0]+5*list[-1][1])/13])

from typing import List

def calc(ls: List):
    print(ls[0]**2+ls[1]**2)


calc(list[int(1e2)])
calc(list[int(1e3)])
calc(list[int(1e4)])
calc(list[int(1e5)])
calc(list[int(1e6)])
calc(list[int(1e7)])