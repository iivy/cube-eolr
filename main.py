from cube import Cube
from state import 真假值检验, 校验字典, 判断setup完后的case, two_1_1_bad
from random import randint
import time


def 随机六棱打乱序列(length=100):
    随机动作集合 = ["M", "M'", "U", "U'"]
    seq = []
    for i in range(length):
        seq.append(随机动作集合[randint(0, 3)])
    return ' '.join(seq)


def EOLR概率统计():
    统计次数 = {}
    for func in 校验字典:
        统计次数[func] = 0

    number = 1000 * 1
    for i in range(number):
        setup = 随机六棱打乱序列(100)
        # 对于每个setup，必须判定成唯一的一种情况，如果是0或者大于1，都说明是有问题的
        当前归属情况 = None
        for func in 统计次数:
            if 判断setup完后的case(func, setup):
                统计次数[func] += 1
                if 当前归属情况 is None:
                    当前归属情况 = func
                    break
                else:
                    print("重复判定！", setup)
                    print(当前归属情况, func.__name__)
        if 当前归属情况 is None:
            print("无法判定情况！", setup)

    total = 0
    for func in 统计次数:
        print("%s,%d,%d" % (
            func.__name__,
            统计次数[func],
            number,
        ))
        total += 统计次数[func]

    if total != number:
        print("情况判断有问题，请检查判定逻辑！total: %d, number: %d" % (total, number))


if __name__ == '__main__':

    # setup = "M U' M U' M U2 M U' M' U' M U U"
    # print(判断setup完后的case(two_1_1_bad, setup))

    # 真假值检验()

    start = time.time()
    EOLR概率统计()
    elapsed = time.time() - start
    print("Time used:", elapsed)



