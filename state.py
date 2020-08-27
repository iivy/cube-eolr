from color import Color
from cube import Cube
from functools import reduce, wraps

# 预定义集合
顶面索引 = [1, 3, 5, 7]
底面索引 = [46, 52]
色向正确颜色 = [Color.RED, Color.ORANGE]
色向错误颜色 = [Color.WHITE, Color.YELLOW, Color.BLUE, Color.GREEN]
LR颜色 = [Color.WHITE, Color.YELLOW]

DEBUG_NOT_FOUND = False


def 对面索引(index):
    if index == 1:
        return 7
    if index == 7:
        return 1
    if index == 3:
        return 5
    if index == 5:
        return 3
    if index == 46:
        return 52
    if index == 52:
        return 46
    if DEBUG_NOT_FOUND:
        print("Not found opposite of " + str(index))
    return -1


def 相邻索引(index):
    if index == 1:
        return [3, 5]
    if index == 3:
        return [1, 7]
    if index == 7:
        return [3, 5]
    if index == 5:
        return [1, 7]
    if DEBUG_NOT_FOUND:
        print("Not found adjacent of " + str(index))
    return -1


def 同块另一个索引(index):
    if index == 1:
        return 19
    if index == 3:
        return 10
    if index == 7:
        return 13
    if index == 5:
        return 16
    if index == 46:
        return 37
    if index == 52:
        return 43
    if index == 19:
        return 1
    if index == 10:
        return 3
    if index == 13:
        return 7
    if index == 16:
        return 5
    if index == 37:
        return 46
    if index == 43:
        return 52
    if DEBUG_NOT_FOUND:
        print("Error to find the other index: " + str(index))
    return -1


def 顶面色向正确个数(cube):
    return 属于颜色集的个数(顶面索引, cube, 色向正确颜色)


def 底面色向正确个数(cube):
    return 属于颜色集的个数(底面索引, cube, 色向正确颜色)


def 顶面LR颜色个数(cube):
    return 属于颜色集的个数(顶面索引, cube, LR颜色)


def 底面LR颜色个数(cube):
    return 属于颜色集的个数(底面索引, cube, LR颜色)


def 属于颜色集的个数(候选索引, cube, 颜色集):
    return sum(map(
        lambda x: 1 if x in 颜色集 else 0,
        map(lambda x: cube.colors[x], filter(lambda x: x >= 0, 候选索引)),
    ))


def 首个索引(候选索引, cube, 颜色集):
    for i in 候选索引:
        if cube.colors[i] in 颜色集:
            return i
    return -1


def 顶面色向正确索引(cube):
    return 首个索引(顶面索引, cube, 色向正确颜色)


def 顶面色向错误索引(cube):
    return 首个索引(顶面索引, cube, 色向错误颜色)


def 底面色向正确索引(cube):
    return 首个索引(底面索引, cube, 色向正确颜色)


def 底面色向错误索引(cube):
    return 首个索引(底面索引, cube, 色向错误颜色)


def 顶面LR错误索引(cube):
    return 首个索引(顶面索引, cube, LR颜色)


def 底面LR错误索引(cube):
    return 首个索引(底面索引, cube, LR颜色)


# ---------- 四棱翻_ 3/1, 共5种 -----------

def 确保四棱翻_3_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 1 or 底面色向正确个数(cube) != 1:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保四棱翻_3_1
def four_3_1_stacked(cube):
    顶面情况 = False
    底面情况 = False
    # 判断顶面的LR是不是在箭头上
    if cube.colors[对面索引(顶面色向正确索引(cube))] in LR颜色:
        顶面情况 = True
    # 判断顶面的LR是不是在箭头上
    if cube.colors[对面索引(底面色向正确索引(cube))] in LR颜色:
        底面情况 = True
    return 顶面情况 and 底面情况


@确保四棱翻_3_1
def four_3_1_good(cube):
    index = 顶面色向正确索引(cube)
    if cube.colors[同块另一个索引(index)] not in LR颜色:
        return False
    if 属于颜色集的个数(相邻索引(index), cube, LR颜色) != 1:
        return False
    return True


@确保四棱翻_3_1
def four_3_1_bottom(cube):
    index = 底面色向正确索引(cube)
    if cube.colors[同块另一个索引(index)] not in LR颜色:
        return False
    if cube.colors[对面索引(index)] not in LR颜色:
        return False
    return True


@确保四棱翻_3_1
def four_3_1_adjacent(cube):
    if 顶面LR颜色个数(cube) != 2:
        return False
    if cube.colors[对面索引(顶面色向正确索引(cube))] not in LR颜色:
        return False
    return True


@确保四棱翻_3_1
def four_3_1_bad(cube):
    if four_3_1_stacked(cube):
        return False
    if four_3_1_good(cube):
        return False
    if four_3_1_bottom(cube):
        return False
    if four_3_1_adjacent(cube):
        return False
    return True


# ---------- 四棱翻_ 4/0，共4种 -----------

def 确保四棱翻_4_0(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 0 or 底面色向正确个数(cube) != 2:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保四棱翻_4_0
def four_4_0_opposite(cube):
    if 顶面LR颜色个数(cube) != 2:
        return False
    index = 顶面LR错误索引(cube)
    if cube.colors[对面索引(index)] not in LR颜色:
        return False
    return True


@确保四棱翻_4_0
def four_4_0_good(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    return True


@确保四棱翻_4_0
def four_4_0_adjacent(cube):
    if 顶面LR颜色个数(cube) != 2:
        return False
    index = 顶面LR错误索引(cube)
    if cube.colors[对面索引(index)] in LR颜色:
        return False
    return True


@确保四棱翻_4_0
def four_4_0_bottom(cube):
    if 顶面LR颜色个数(cube) != 0:
        return False
    return True


# ---------- 四棱翻_ 2o/2，共6种 -----------

def 确保四棱翻_2o_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 2 or 底面色向正确个数(cube) != 0:
            return False
        index = 顶面色向正确索引(cube)
        if cube.colors[对面索引(index)] not in 色向正确颜色:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保四棱翻_2o_2
def four_2o_2_bottom(cube):
    if 底面LR颜色个数(cube) != 2:
        return False
    return True


@确保四棱翻_2o_2
def four_2o_2_adjacent(cube):
    if 底面LR颜色个数(cube) != 0:
        return False
    if 顶面LR颜色个数(cube) != 1:
        return False
    index = 顶面色向正确索引(cube)
    if cube.colors[对面索引(index)] in LR颜色:
        return False
    return True


@确保四棱翻_2o_2
def four_2o_2_decent(cube):
    if 底面LR颜色个数(cube) != 1:
        return False
    if 顶面LR颜色个数(cube) != 1:
        return False
    return True


@确保四棱翻_2o_2
def four_2o_2_misoriented_opposite(cube):
    if 顶面LR颜色个数(cube) != 2:
        return False
    index = 顶面LR错误索引(cube)
    if cube.colors[对面索引(index)] not in LR颜色:
        return False
    return True


@确保四棱翻_2o_2
def four_2o_2_stacked(cube):
    if 底面LR颜色个数(cube) != 1:
        return False
    if 顶面LR颜色个数(cube) != 0:
        return False
    return True


@确保四棱翻_2o_2
def four_2o_2_oriented_opposite(cube):
    if 底面LR颜色个数(cube) != 0:
        return False
    if 顶面LR颜色个数(cube) != 0:
        return False
    return True


# ---------- 四棱翻_ 2a/2，共7种 -----------

def 确保四棱翻_2a_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 2 or 底面色向正确个数(cube) != 0:
            return False
        index = 顶面色向正确索引(cube)
        if cube.colors[对面索引(index)] in 色向正确颜色:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保四棱翻_2a_2
def four_2a_2_best(cube):
    if 顶面LR颜色个数(cube) != 2:
        return False
    return True


@确保四棱翻_2a_2
def four_2a_2_great(cube):
    if 顶面LR颜色个数(cube) != 0:
        return False
    if 底面LR颜色个数(cube) != 1:
        return False
    return True


@确保四棱翻_2a_2
def four_2a_2_opposite(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    index = 顶面LR错误索引(cube)
    if cube.colors[同块另一个索引(对面索引(index))] not in LR颜色:
        return False
    return True


@确保四棱翻_2a_2
def four_2a_2_stacked(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    if 底面LR颜色个数(cube) != 1:
        return False
    return True


@确保四棱翻_2a_2
def four_2a_2_bottom(cube):
    if 底面LR颜色个数(cube) != 2:
        return False
    return True


@确保四棱翻_2a_2
def four_2a_2_mixed_adjacent(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    if 底面LR颜色个数(cube) != 0:
        return False
    index = 顶面LR错误索引(cube)
    if cube.colors[同块另一个索引(对面索引(index))] in LR颜色:
        return False
    return True


@确保四棱翻_2a_2
def four_2a_2_oriented_adjacent(cube):
    if 顶面LR颜色个数(cube) != 0:
        return False
    if 底面LR颜色个数(cube) != 0:
        return False
    return True


# ---------- 二棱翻_ 1/1，共9种 -----------

def 确保二棱翻_1_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 3 or 底面色向正确个数(cube) != 1:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保二棱翻_1_1
def two_1_1_best(cube):
    if 顶面LR颜色个数(cube) != 0:
        return False
    if 底面LR颜色个数(cube) != 0:
        return False
    侧面索引 = map(lambda x: 同块另一个索引(x), 相邻索引(顶面色向错误索引(cube)))
    if 属于颜色集的个数(侧面索引, cube, LR颜色) != 1:
        return False
    return True


@确保二棱翻_1_1
def two_1_1_stacked(cube):
    if 底面色向错误索引(cube) != 底面LR错误索引(cube):
        return False
    return cube.colors[同块另一个索引(对面索引(顶面色向错误索引(cube)))] in LR颜色


@确保二棱翻_1_1
def two_1_1_good(cube):
    if 底面色向错误索引(cube) != 底面LR错误索引(cube):
        return False
    if cube.colors[同块另一个索引(底面色向正确索引(cube))] in LR颜色:
        return False
    if cube.colors[同块另一个索引(对面索引(顶面色向错误索引(cube)))] in LR颜色:
        return False
    return True


@确保二棱翻_1_1
def two_1_1_uf_adjacent(cube):
    index = 顶面色向错误索引(cube)
    if cube.colors[index] not in LR颜色:
        return False
    if 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 相邻索引(index)), cube, LR颜色) != 1:
        return False
    return True


@确保二棱翻_1_1
def two_1_1_uf_separated(cube):
    if 顶面色向错误索引(cube) != 顶面LR错误索引(cube):
        return False
    return cube.colors[同块另一个索引(底面色向正确索引(cube))] in LR颜色


@确保二棱翻_1_1
def two_1_1_sides(cube):
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 相邻索引(顶面色向错误索引(cube))), cube, LR颜色) == 2


@确保二棱翻_1_1
def two_1_1_uf_opposite(cube):
    if 顶面色向错误索引(cube) != 顶面LR错误索引(cube):
        return False
    return cube.colors[同块另一个索引(对面索引(顶面色向错误索引(cube)))] in LR颜色


@确保二棱翻_1_1
def two_1_1_bottom(cube):
    index = 底面色向正确索引(cube)
    if cube.colors[同块另一个索引(index)] not in LR颜色:
        return False
    if cube.colors[对面索引(index)] not in LR颜色:
        return False
    return True


@确保二棱翻_1_1
def two_1_1_bad(cube):
    if cube.colors[同块另一个索引(底面色向正确索引(cube))] not in LR颜色:
        return False
    if cube.colors[同块另一个索引(对面索引(顶面色向错误索引(cube)))] not in LR颜色:
        return False
    return True


# ---------- 二棱翻_ 2o/0，共6种 -----------

def 确保二棱翻_2o_0(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 2 or 底面色向正确个数(cube) != 2:
            return False
        index = 顶面色向正确索引(cube)
        if cube.colors[对面索引(index)] not in 色向正确颜色:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保二棱翻_2o_0
def two_2o_0_best(cube):
    if 顶面LR颜色个数(cube) != 0:
        return False
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 底面索引), cube, LR颜色) == 1


@确保二棱翻_2o_0
def two_2o_0_misoriented(cube):
    return 顶面LR颜色个数(cube) == 2


@确保二棱翻_2o_0
def two_2o_0_stacked(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 底面索引), cube, LR颜色) == 1


@确保二棱翻_2o_0
def two_2o_0_adjacent(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 底面索引), cube, LR颜色) == 0


@确保二棱翻_2o_0
def two_2o_0_opposite(cube):
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 相邻索引(顶面色向错误索引(cube))), cube, LR颜色) == 2


@确保二棱翻_2o_0
def two_2o_0_bottom(cube):
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 底面索引), cube, LR颜色) == 2


# ----------  二棱翻_ 2a/0，共7种 -----------

def 确保二棱翻_2a_0(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 2 or 底面色向正确个数(cube) != 2:
            return False
        index = 顶面色向正确索引(cube)
        if cube.colors[对面索引(index)] in 色向正确颜色:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保二棱翻_2a_0
def two_2a_0_best(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 相邻索引(顶面LR错误索引(cube))), cube, LR颜色) == 1


@确保二棱翻_2a_0
def two_2a_0_stacked(cube):
    if 顶面LR颜色个数(cube) != 0:
        return False
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 底面索引), cube, LR颜色) == 1


@确保二棱翻_2a_0
def two_2a_0_good(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 底面索引), cube, LR颜色) == 1


@确保二棱翻_2a_0
def two_2a_0_bottom(cube):
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 底面索引), cube, LR颜色) == 2


@确保二棱翻_2a_0
def two_2a_0_oriented_adjacent(cube):
    if 顶面LR颜色个数(cube) != 0:
        return False
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), 底面索引), cube, LR颜色) == 0


@确保二棱翻_2a_0
def two_2a_0_opposite(cube):
    if 顶面LR颜色个数(cube) != 1:
        return False
    return cube.colors[同块另一个索引(对面索引(顶面LR错误索引(cube)))] in LR颜色


@确保二棱翻_2a_0
def two_2a_0_misoriented_adjacent(cube):
    return 顶面LR颜色个数(cube) == 2


# ----------  二棱翻_ 0/2，共4种 -----------

def 确保二棱翻_0_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 4 or 底面色向正确个数(cube) != 0:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保二棱翻_0_2
def two_0_2_adjacent(cube):
    if 底面LR颜色个数(cube) != 0:
        return False
    indices = [顶面色向正确索引(cube), 对面索引(顶面色向正确索引(cube))]
    return 属于颜色集的个数(map(lambda x: 同块另一个索引(x), indices), cube, LR颜色) == 1


@确保二棱翻_0_2
def two_0_2_bottom(cube):
    return 底面LR颜色个数(cube) == 2


@确保二棱翻_0_2
def two_0_2_good(cube):
    return 底面LR颜色个数(cube) == 1


@确保二棱翻_0_2
def two_0_2_opposite(cube):
    if 底面LR颜色个数(cube) != 0:
        return False
    indices = [顶面色向正确索引(cube), 对面索引(顶面色向正确索引(cube))]
    count = 属于颜色集的个数(map(lambda x: 同块另一个索引(x), indices), cube, LR颜色)
    return count == 0 or count == 2


# ----------  六棱翻_ 4/2，共3种 -----------

def 确保六棱翻_4_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cube = args[0]
        if 顶面色向正确个数(cube) != 0 or 底面色向正确个数(cube) != 0:
            return False
        return func(*args, **kwargs)
    return wrapper


@确保六棱翻_4_2
def six_4_2_adjacent(cube):
    if 顶面LR颜色个数(cube) == 1 or 底面LR颜色个数(cube) == 1:
        return True
    if 顶面LR颜色个数(cube) != 2:
        return False
    return cube.colors[对面索引(顶面LR错误索引(cube))] not in LR颜色


@确保六棱翻_4_2
def six_4_2_opposite(cube):
    if 顶面LR颜色个数(cube) != 2:
        return False
    return cube.colors[对面索引(顶面LR错误索引(cube))] in LR颜色


@确保六棱翻_4_2
def six_4_2_bottom(cube):
    return 底面LR颜色个数(cube) == 2


def solved(cube):
    return 顶面色向正确个数(cube) == 4 and 底面色向正确个数(cube) == 2

# -----------------------------------------


def 判断setup完后的case(func, setup):
    c = Cube()
    c.Rotate("X2 Z")
    c.Rotate(setup)
    if c.colors[4] not in 色向正确颜色:
        c.Rotate("M")
    return func(c)


校验字典 = {
    # 3/1,
    four_3_1_stacked: "M U M",
    four_3_1_good: "U M' U M",
    four_3_1_bottom: "M' U M U M U M' U",
    four_3_1_adjacent: "M' U M U M2 U M U2 M U'",
    four_3_1_bad: "M' U M' U' M U2 M U' M2 U",
    # 4/0,
    four_4_0_opposite: "M' U M2 U M' U2 M U2 M",
    four_4_0_good: "U M U' M U2 M U2 M",
    four_4_0_adjacent: "M' U M U' M' U2 M U M' U2 M U",
    four_4_0_bottom: "U M' U2 M U2 M U M U2 M U2 M",
    # 2o/2,
    four_2o_2_bottom: "M' U M2 U M U2 M U2 M",
    four_2o_2_adjacent: "U M' U' M' U2 M U2 M",
    four_2o_2_decent: "U M' U' M' U M U M U' M' U' M",
    four_2o_2_misoriented_opposite: "M' U M U2 M U2 M U M2",
    four_2o_2_stacked: "M' U M' U' M' U' M U M U2 M U2",
    four_2o_2_oriented_opposite: "U M U M' U M U M U M' U M",
    # 2a/2,
    four_2a_2_best: "M' U M U M2",
    four_2a_2_great: "U M U' M' U' M2 U",
    four_2a_2_opposite: "M' U M' U M' U M' U",
    four_2a_2_stacked: "M' U M' U' M U2 M U2",
    four_2a_2_bottom: "U M' U' M U' M U' M",
    four_2a_2_mixed_adjacent: "U M U' M U' M2 U M U2 M",
    four_2a_2_oriented_adjacent: "M' U M' U M' U2 M U2 M U M' U",
    # 1/1,
    two_1_1_best: "U M' U' M' U M U M",
    two_1_1_stacked: "U M' U' M' U' M U' M",
    two_1_1_good: "U M U M' U M U M'",
    two_1_1_uf_adjacent: "U M U M' U M U M",
    two_1_1_uf_separated: "U M' U M' U M U M'",
    two_1_1_sides: "U M' U' M' U2 M U' M U",
    two_1_1_uf_opposite: "M' U M' U' M U' M' U2 M U M' U2",
    two_1_1_bottom: "M' U M U M' U M U M' U M' U",
    two_1_1_bad: "M U' M U' M U2 M U' M' U' M U",
    # 2o/0,
    two_2o_0_best: "U M' U M' U' M U M'",
    two_2o_0_misoriented: "U M' U M U' M' U M",
    two_2o_0_stacked: "U M' U' M' U' M U M'",
    two_2o_0_adjacent: "U M' U M U M' U' M",
    two_2o_0_opposite: "M' U M' U M' U2 M U M U M",
    two_2o_0_bottom: "U' M U' M' U' M' U2 M U' M U' M",
    # 2a/0,
    two_2a_0_best: "M' U M' U2 M U' M2 U M U",
    two_2a_0_stacked: "M' U M U' M' U' M' U' M2",
    two_2a_0_good: "U M2 U M' U' M U2 M U' M",
    two_2a_0_bottom: "U M' U M' U2 M U M' U",
    two_2a_0_oriented_adjacent: "M' U M U M' U M U M U2 M",
    two_2a_0_opposite: "M' U M U' M' U' M U' M' U' M U",
    two_2a_0_misoriented_adjacent: "M' U M' U M U M' U' M U M U",
    # 0/2,
    two_0_2_adjacent: "M' U M' U' M U M U",
    two_0_2_bottom: "U M U M' U' M U M",
    two_0_2_good: "U M U' M' U' M U M",
    two_0_2_opposite: "M' U M' U' M U2 M U M' U M",
    # 4/2,
    six_4_2_adjacent: "M' U M U' M' U' M U2 M U M",
    six_4_2_opposite: "U M' U' M' U2 M' U' M U' M' U' M",
    six_4_2_bottom: "U M' U' M' U2 M' U' M U' M' U' M'",
    # 复原的情况
    solved: "U",
}


def 真假值检验():
    """
    判断每个真值是否被判定正确，并且判断错误值是否被正确判错

    每个函数对于后面的setup都必须判定为正确；
    每个函数对于其他的setup都必须判断为错误；
    """
    正例检验总次数 = 0
    正例检验成功次数 = 0
    负例检验总次数 = 0
    负例检验成功次数 = 0
    for func in 校验字典:
        setup = 校验字典[func]
        正例检验总次数 += 2

        if not 判断setup完后的case(func, setup):
            print("正例判错", func.__name__)
        else:
            正例检验成功次数 += 1

        # 为每个setup加U，然后再test
        if not 判断setup完后的case(func, setup + ' U'):
            print("正例判错 +U", func.__name__)
        else:
            正例检验成功次数 += 1

        for s in 校验字典.values():
            if s != setup:
                负例检验总次数 += 2
                if 判断setup完后的case(func, s):
                    print("负例判对", func.__name__, s)
                else:
                    负例检验成功次数 += 1
                if not 判断setup完后的case(func, setup + ' U'):
                    print("负例判对 +U", func.__name__)
                else:
                    负例检验成功次数 += 1

    print("正例检验：通过{}，总计{}".format(正例检验成功次数, 正例检验总次数))
    print("负例检验：通过{}，总计{}".format(负例检验成功次数, 负例检验总次数))
