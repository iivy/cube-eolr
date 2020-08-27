from operator import methodcaller
from color import Color


class Cube:
    """
    魔方的显示：

                UUU                       0  1  2
                UUU                       3  4  5
                UUU                       6  7  8
            LLL FFF RRR BBB      9 10 11 12 13 14 15 16 17 18 19 20
            LLL FFF RRR BBB     21 22 23 24 25 26 27 28 29 30 31 32
            LLL FFF RRR BBB     33 34 35 36 37 38 39 40 41 42 43 44
                DDD                      45 46 47
                DDD                      48 49 50
                DDD                      51 52 53

    这个和DCTimer里面的显示是一样的。
    """

    def __init__(self):

        self.colors = [
            Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE,
            Color.WHITE,
            Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED,
            Color.RED, Color.BLUE, Color.BLUE, Color.BLUE,
            Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED,
            Color.RED, Color.BLUE, Color.BLUE, Color.BLUE,
            Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED,
            Color.RED, Color.BLUE, Color.BLUE, Color.BLUE,
            Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW,
            Color.YELLOW, Color.YELLOW,
        ]

        # def __str__(self):

    #     template = ("       {}{}{}\n"
    #                 "       {}{}{}\n"
    #                 "       {}{}{}\n"
    #                 "{}{}{} {}{}{} {}{}{} {}{}{}\n"
    #                 "{}{}{} {}{}{} {}{}{} {}{}{}\n"
    #                 "{}{}{} {}{}{} {}{}{} {}{}{}\n"
    #                 "       {}{}{}\n"
    #                 "       {}{}{}\n"
    #                 "       {}{}{}")

    #     return "       " + template.format(*(x.value for x in self.colors)).strip() 

    def __str__(self):
        template = ("    {}{}{}\n"
                    "    {}{}{}\n"
                    "    {}{}{}\n"
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"
                    "    {}{}{}\n"
                    "    {}{}{}\n"
                    "    {}{}{}")

        return "\n    " + template.format(*(x.value for x in self.colors)).strip() + "\n"

    def L(self):
        pre = self.colors[:]
        self.colors[0] = pre[44]
        self.colors[3] = pre[32]
        self.colors[6] = pre[20]
        self.colors[12] = pre[0]
        self.colors[24] = pre[3]
        self.colors[36] = pre[6]
        self.colors[45] = pre[12]
        self.colors[48] = pre[24]
        self.colors[51] = pre[36]
        self.colors[44] = pre[45]
        self.colors[32] = pre[48]
        self.colors[20] = pre[51]

        self.colors[9] = pre[33]
        self.colors[10] = pre[21]
        self.colors[11] = pre[9]
        self.colors[21] = pre[34]
        self.colors[22] = pre[22]
        self.colors[23] = pre[10]
        self.colors[33] = pre[35]
        self.colors[34] = pre[23]
        self.colors[35] = pre[11]

    def Li(self):
        pre = self.colors[:]
        self.colors[0] = pre[12]
        self.colors[3] = pre[24]
        self.colors[6] = pre[36]
        self.colors[12] = pre[45]
        self.colors[24] = pre[48]
        self.colors[36] = pre[51]
        self.colors[45] = pre[44]
        self.colors[48] = pre[32]
        self.colors[51] = pre[20]
        self.colors[44] = pre[0]
        self.colors[32] = pre[3]
        self.colors[20] = pre[6]

        self.colors[9] = pre[11]
        self.colors[10] = pre[23]
        self.colors[11] = pre[35]
        self.colors[21] = pre[10]
        self.colors[22] = pre[22]
        self.colors[23] = pre[34]
        self.colors[33] = pre[9]
        self.colors[34] = pre[21]
        self.colors[35] = pre[33]

    def R(self):
        pre = self.colors[:]
        self.colors[2] = pre[14]
        self.colors[5] = pre[26]
        self.colors[8] = pre[38]
        self.colors[14] = pre[47]
        self.colors[26] = pre[50]
        self.colors[38] = pre[53]
        self.colors[47] = pre[42]
        self.colors[50] = pre[30]
        self.colors[53] = pre[18]
        self.colors[42] = pre[2]
        self.colors[30] = pre[5]
        self.colors[18] = pre[8]

        self.colors[15] = pre[39]
        self.colors[16] = pre[27]
        self.colors[17] = pre[15]
        self.colors[27] = pre[40]
        self.colors[28] = pre[28]
        self.colors[29] = pre[16]
        self.colors[39] = pre[41]
        self.colors[40] = pre[29]
        self.colors[41] = pre[17]

    def Ri(self):
        pre = self.colors[:]
        self.colors[2] = pre[42]
        self.colors[5] = pre[30]
        self.colors[8] = pre[18]
        self.colors[14] = pre[2]
        self.colors[26] = pre[5]
        self.colors[38] = pre[8]
        self.colors[47] = pre[14]
        self.colors[50] = pre[26]
        self.colors[53] = pre[38]
        self.colors[42] = pre[47]
        self.colors[30] = pre[50]
        self.colors[18] = pre[53]

        self.colors[15] = pre[17]
        self.colors[16] = pre[29]
        self.colors[17] = pre[41]
        self.colors[27] = pre[16]
        self.colors[28] = pre[28]
        self.colors[29] = pre[40]
        self.colors[39] = pre[15]
        self.colors[40] = pre[27]
        self.colors[41] = pre[39]

    def U(self):
        pre = self.colors[:]
        self.colors[9] = pre[12]
        self.colors[10] = pre[13]
        self.colors[11] = pre[14]
        self.colors[12] = pre[15]
        self.colors[13] = pre[16]
        self.colors[14] = pre[17]
        self.colors[15] = pre[18]
        self.colors[16] = pre[19]
        self.colors[17] = pre[20]
        self.colors[18] = pre[9]
        self.colors[19] = pre[10]
        self.colors[20] = pre[11]

        self.colors[0] = pre[6]
        self.colors[1] = pre[3]
        self.colors[2] = pre[0]
        self.colors[3] = pre[7]
        self.colors[4] = pre[4]
        self.colors[5] = pre[1]
        self.colors[6] = pre[8]
        self.colors[7] = pre[5]
        self.colors[8] = pre[2]

    def Ui(self):
        pre = self.colors[:]
        self.colors[9] = pre[18]
        self.colors[10] = pre[19]
        self.colors[11] = pre[20]
        self.colors[12] = pre[9]
        self.colors[13] = pre[10]
        self.colors[14] = pre[11]
        self.colors[15] = pre[12]
        self.colors[16] = pre[13]
        self.colors[17] = pre[14]
        self.colors[18] = pre[15]
        self.colors[19] = pre[16]
        self.colors[20] = pre[17]

        self.colors[0] = pre[2]
        self.colors[1] = pre[5]
        self.colors[2] = pre[8]
        self.colors[3] = pre[1]
        self.colors[4] = pre[4]
        self.colors[5] = pre[7]
        self.colors[6] = pre[0]
        self.colors[7] = pre[3]
        self.colors[8] = pre[6]

    def D(self):
        pre = self.colors[:]
        self.colors[33] = pre[42]
        self.colors[34] = pre[43]
        self.colors[35] = pre[44]
        self.colors[36] = pre[33]
        self.colors[37] = pre[34]
        self.colors[38] = pre[35]
        self.colors[39] = pre[36]
        self.colors[40] = pre[37]
        self.colors[41] = pre[38]
        self.colors[42] = pre[39]
        self.colors[43] = pre[40]
        self.colors[44] = pre[41]

        self.colors[45] = pre[51]
        self.colors[46] = pre[48]
        self.colors[47] = pre[45]
        self.colors[48] = pre[52]
        self.colors[49] = pre[49]
        self.colors[50] = pre[46]
        self.colors[51] = pre[53]
        self.colors[52] = pre[50]
        self.colors[53] = pre[47]

    def Di(self):
        pre = self.colors[:]
        self.colors[33] = pre[36]
        self.colors[34] = pre[37]
        self.colors[35] = pre[38]
        self.colors[36] = pre[39]
        self.colors[37] = pre[40]
        self.colors[38] = pre[41]
        self.colors[39] = pre[42]
        self.colors[40] = pre[43]
        self.colors[41] = pre[44]
        self.colors[42] = pre[33]
        self.colors[43] = pre[34]
        self.colors[44] = pre[35]

        self.colors[45] = pre[47]
        self.colors[46] = pre[50]
        self.colors[47] = pre[53]
        self.colors[48] = pre[46]
        self.colors[49] = pre[49]
        self.colors[50] = pre[52]
        self.colors[51] = pre[45]
        self.colors[52] = pre[48]
        self.colors[53] = pre[51]

    def F(self):
        pre = self.colors[:]
        self.colors[6] = pre[35]
        self.colors[7] = pre[23]
        self.colors[8] = pre[11]
        self.colors[15] = pre[6]
        self.colors[27] = pre[7]
        self.colors[39] = pre[8]
        self.colors[47] = pre[15]
        self.colors[46] = pre[27]
        self.colors[45] = pre[39]
        self.colors[35] = pre[47]
        self.colors[23] = pre[46]
        self.colors[11] = pre[45]

        self.colors[12] = pre[36]
        self.colors[13] = pre[24]
        self.colors[14] = pre[12]
        self.colors[24] = pre[37]
        self.colors[25] = pre[25]
        self.colors[26] = pre[13]
        self.colors[36] = pre[38]
        self.colors[37] = pre[26]
        self.colors[38] = pre[14]

    def Fi(self):
        pre = self.colors[:]
        self.colors[6] = pre[15]
        self.colors[7] = pre[27]
        self.colors[8] = pre[39]
        self.colors[15] = pre[47]
        self.colors[27] = pre[46]
        self.colors[39] = pre[45]
        self.colors[47] = pre[35]
        self.colors[46] = pre[23]
        self.colors[45] = pre[11]
        self.colors[35] = pre[6]
        self.colors[23] = pre[7]
        self.colors[11] = pre[8]

        self.colors[12] = pre[14]
        self.colors[13] = pre[26]
        self.colors[14] = pre[38]
        self.colors[24] = pre[13]
        self.colors[25] = pre[25]
        self.colors[26] = pre[37]
        self.colors[36] = pre[12]
        self.colors[37] = pre[24]
        self.colors[38] = pre[36]

    def B(self):
        pre = self.colors[:]
        self.colors[2] = pre[41]
        self.colors[1] = pre[29]
        self.colors[0] = pre[17]
        self.colors[9] = pre[2]
        self.colors[21] = pre[1]
        self.colors[33] = pre[0]
        self.colors[51] = pre[9]
        self.colors[52] = pre[21]
        self.colors[53] = pre[33]
        self.colors[41] = pre[51]
        self.colors[29] = pre[52]
        self.colors[17] = pre[53]

        self.colors[18] = pre[42]
        self.colors[19] = pre[30]
        self.colors[20] = pre[18]
        self.colors[30] = pre[43]
        self.colors[31] = pre[31]
        self.colors[32] = pre[19]
        self.colors[42] = pre[44]
        self.colors[43] = pre[32]
        self.colors[44] = pre[20]

    def Bi(self):
        pre = self.colors[:]
        self.colors[2] = pre[9]
        self.colors[1] = pre[21]
        self.colors[0] = pre[33]
        self.colors[9] = pre[51]
        self.colors[21] = pre[52]
        self.colors[33] = pre[53]
        self.colors[51] = pre[41]
        self.colors[52] = pre[29]
        self.colors[53] = pre[17]
        self.colors[41] = pre[2]
        self.colors[29] = pre[1]
        self.colors[17] = pre[0]

        self.colors[18] = pre[20]
        self.colors[19] = pre[32]
        self.colors[20] = pre[44]
        self.colors[30] = pre[19]
        self.colors[31] = pre[31]
        self.colors[32] = pre[43]
        self.colors[42] = pre[18]
        self.colors[43] = pre[30]
        self.colors[44] = pre[42]

    def M(self):
        pre = self.colors[:]
        self.colors[1] = pre[43]
        self.colors[4] = pre[31]
        self.colors[7] = pre[19]
        self.colors[13] = pre[1]
        self.colors[25] = pre[4]
        self.colors[37] = pre[7]
        self.colors[46] = pre[13]
        self.colors[49] = pre[25]
        self.colors[52] = pre[37]
        self.colors[43] = pre[46]
        self.colors[31] = pre[49]
        self.colors[19] = pre[52]

    def Mi(self):
        pre = self.colors[:]
        self.colors[1] = pre[13]
        self.colors[4] = pre[25]
        self.colors[7] = pre[37]
        self.colors[13] = pre[46]
        self.colors[25] = pre[49]
        self.colors[37] = pre[52]
        self.colors[46] = pre[43]
        self.colors[49] = pre[31]
        self.colors[52] = pre[19]
        self.colors[43] = pre[1]
        self.colors[31] = pre[4]
        self.colors[19] = pre[7]

    def E(self):
        pre = self.colors[:]
        self.colors[21] = pre[30]
        self.colors[22] = pre[31]
        self.colors[23] = pre[32]
        self.colors[24] = pre[21]
        self.colors[25] = pre[22]
        self.colors[26] = pre[23]
        self.colors[27] = pre[24]
        self.colors[28] = pre[25]
        self.colors[29] = pre[26]
        self.colors[30] = pre[27]
        self.colors[31] = pre[28]
        self.colors[32] = pre[29]

    def Ei(self):
        pre = self.colors[:]
        self.colors[21] = pre[24]
        self.colors[22] = pre[25]
        self.colors[23] = pre[26]
        self.colors[24] = pre[27]
        self.colors[25] = pre[28]
        self.colors[26] = pre[29]
        self.colors[27] = pre[30]
        self.colors[28] = pre[31]
        self.colors[29] = pre[32]
        self.colors[30] = pre[21]
        self.colors[31] = pre[22]
        self.colors[32] = pre[23]

    def S(self):
        pre = self.colors[:]
        self.colors[3] = pre[34]
        self.colors[4] = pre[22]
        self.colors[5] = pre[10]
        self.colors[16] = pre[3]
        self.colors[28] = pre[4]
        self.colors[40] = pre[5]
        self.colors[50] = pre[16]
        self.colors[49] = pre[28]
        self.colors[48] = pre[40]
        self.colors[34] = pre[50]
        self.colors[22] = pre[49]
        self.colors[10] = pre[48]

    def Si(self):
        pre = self.colors[:]
        self.colors[3] = pre[16]
        self.colors[4] = pre[28]
        self.colors[5] = pre[40]
        self.colors[16] = pre[50]
        self.colors[28] = pre[49]
        self.colors[40] = pre[48]
        self.colors[50] = pre[34]
        self.colors[49] = pre[22]
        self.colors[48] = pre[10]
        self.colors[34] = pre[3]
        self.colors[22] = pre[4]
        self.colors[10] = pre[5]

    def X(self):
        self.Li()
        self.Mi()
        self.R()

    def Xi(self):
        self.L()
        self.M()
        self.Ri()

    def Y(self):
        self.U()
        self.Ei()
        self.Di()

    def Yi(self):
        self.Ui()
        self.E()
        self.D()

    def Z(self):
        self.F()
        self.S()
        self.Bi()

    def Zi(self):
        self.Fi()
        self.Si()
        self.B()

    def Rotate(self, seq):
        """
        按照输入的seq进行转动。这里的seq是常用的魔方标记，比如 (R U R' U')M2' U'2
        """

        start = 0
        debug_str = ""
        while True:
            action, clockwise, double, start = self.nextop(seq, start)

            if len(action) == 0:
                break

            method = action
            if not clockwise:
                method += 'i'

            debug_str += method

            methodcaller(method)(self)
            if double:
                methodcaller(method)(self)
                debug_str += '2'

            debug_str += ' '

        # print(debug_str)

    def nextop(self, seq, pos):
        """
        提取从seq的pos位置开始的，下一个动作，返回四个结果
        1. 动作的名称
        2. 动作的方向是否顺时针
        3. 是否是两次操作
        4. 移位后的pos
        """

        action = ''
        clockwise = True
        double = False
        start = pos

        skip_chars = [' ', '\t', '(', ')', '（', '）']
        action_chars = ['R', 'L', 'U', 'D', 'F', 'B', 'E', 'M', 'S', 'X', 'Y', 'Z']

        while True:

            if len(seq) == start:
                break

            cur = seq[start]

            if len(action) == 0:
                if cur in skip_chars:
                    start += 1
                    continue
                if cur in action_chars:
                    action = cur
                    start += 1
                    continue
                print("Unexpected symbol: " + cur)
                start += 1
            else:
                if cur in skip_chars:
                    start += 1
                    break
                if cur in action_chars:
                    break
                if cur == '\'':
                    clockwise = False
                    start += 1
                elif cur == '2':
                    double = True
                    start += 1
                else:
                    print("Unknown symbol: " + cur)
                    start += 1

        return action, clockwise, double, start


if __name__ == '__main__':
    c = Cube()

    # c.R()
    # c.U()
    # c.Ri()
    # c.Ui()

    # c.D()
    # c.R()
    # c.Di()
    # c.Ri()

    # c.Ri()
    # c.F()
    # c.R()
    # c.Fi()

    # c.Bi()
    # c.D()
    # c.B()
    # c.Di()

    print(c)

    c.Rotate("R U R' U'")
    c.Rotate("R U R' U'")
    c.Rotate("R U R' U'")
    c.Rotate("R U R' U'")
    c.Rotate("R U R' U'")
    c.Rotate("R U R' U'")

    print(c)
