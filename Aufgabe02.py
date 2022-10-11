from random import randint

def get_random_six(startValue, endValue, rangeD):
    list_return = []
    for item in range(startValue, endValue+1):
        list_return.append(item)
    print(list_return)

    for el in range(endValue):
        lastPos = len(list_return)-el-1
        ran = randint(startValue, endValue)
        list_return[ran], list_return[-lastPos] = list_return[-lastPos], list_return[ran]
    print(list_return)
    return list_return[:-rangeD]

def get_statistic(list):
    for element in list:
        list_start[element+startValueZ] = list_start[element+startValueZ] +1


def print_list(list):
    counter = 0
    for element in list:
        print("Zahl", counter, ":", element)
        counter = counter +1

endValueZ = 45
startValueZ = 1
rangeZ = 6
list_start = [0] * (endValueZ-startValueZ)

for index in range(0, 1001):
    rand = get_random_six(startValueZ, endValueZ, rangeZ)
    print(rand)
    get_statistic(rand)



