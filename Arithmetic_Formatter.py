
from typing import List


class Error(Exception):
    def __str__(self):
        return "Error: Too many problems."


class DigitError(Error):
    def __str__(self):
        return ("Error: Operator must be '+' or '-'.")


class DigitCount(Error):
    def __str__(self):
        return "Error: Numbers cannot be more than four digits."


class Digit(Error):
    def __str__(self):
        return "Error: Numbers must only contain digits."


def addtostr(string: str, a: str):
    return a + string


def fit(a: str):
    a = str(a)
    if a.isnumeric:
        a = a.strip()
        if len(a) > 4:
            print(a)
            raise DigitCount
        else:
            return a
    else:
        raise Digit


def arithmetic_arranger(calculations: List, Calculate=False):
    if len(calculations) > 5:
        raise Error
    for index, problem in enumerate(calculations):
        if problem.find("+") != -1:
            calculations[index] = problem.split("+")
            calculations[index].append("+")
        elif problem.find("-") != -1:
            calculations[index] = problem.split("-")
            calculations[index].append("-")
        else:
            raise DigitError
    l1 = ""
    l2 = ""
    l3 = ""

    for a in range(len(calculations)):
        x = fit(calculations[3-a][0])
        y = fit(calculations[3-a][1])

        if len(x) > len(y):
            l3 = addtostr(l3, "-"*len(x))
            while 1:
                if len(y) % len(x) != 0:
                    y = addtostr(y, " ")
                else:
                    break

        else:
            l3 = addtostr(l3, "-"*len(y))
            while 1:
                if len(x) % len(y) != 0:
                    x = addtostr(x, " ")
                else:
                    break

        l1 = addtostr(l1, x)
        l2 = addtostr(l2, y)

        if a+1 != len(calculations):
            l1 = addtostr(l1, "    ")
            l2 = addtostr(l2, "  {} ".format(calculations[3-a][2]))
            l3 = addtostr(l3, "  --")
        else:
            l1 = addtostr(l1, "  ")
            l2 = addtostr(l2, "{} ".format(calculations[3-a][2]))
            l3 = addtostr(l3, "--")

    print(l1)
    print(l2)
    print(l3)
    ref = l3.split()
    if Calculate:
        l4 = ""
        for a, b in enumerate(ref):
            if calculations[3-a][2] == "+":
                result = int(calculations[3-a][0]) + int(calculations[3-a][1])
            else:
                result = int(calculations[3-a][0]) - int(calculations[3-a][1])
            l4 = addtostr(l4, str(result))
            while not len(ref[3-a]) == len(str(result)):
                l4 = addtostr(l4, " ")
                result = result*10

            if a+1 != len(ref[3-a]):
                l4 = addtostr(l4, "  ")
        print(l4)

