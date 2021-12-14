
from typing import List





def addtostr(string: str, a: str):
    return a + string


def fit(a: str):
    a = str(a)
    a = a.strip()
    if a.isnumeric():
        if len(a) > 4:
            print(a)
            return -1
        else:
            return a
    else:
        return -2


def arithmetic_arranger(calculations: List, Calculate=False):
    if len(calculations) > 5:
        return "Error: Too many problems."
    for index, problem in enumerate(calculations):
        if problem.find("+") != -1:
            calculations[index] = problem.split("+")
            calculations[index].append("+")
        elif problem.find("-") != -1:
            calculations[index] = problem.split("-")
            calculations[index].append("-")
        else:
            return "Error: Operator must be '+' or '-'."
    l1 = ""
    l2 = ""
    l3 = ""

    for a in range(len(calculations)):
        x = fit(calculations[len(calculations)-1-a][0])
        y = fit(calculations[len(calculations)-1-a][1])

        if x == -1 or y  == -1:
          return "Error: Numbers cannot be more than four digits."
        elif x == -2 or y == -2:
          return "Error: Numbers must only contain digits."

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
            l1 = addtostr(l1, "      ")
            l2 = addtostr(l2, "    {} ".format(calculations[len(calculations)-1-a][2]))
            l3 = addtostr(l3, "    --")
        else:
            l1 = addtostr(l1, "  ")
            l2 = addtostr(l2, "{} ".format(calculations[len(calculations)-1-a][2]))
            l3 = addtostr(l3, "--")

    
    ref = l3.split()
    if Calculate:
        l4 = ""
        for a, b in enumerate(ref):
            if calculations[len(calculations)-1-a][2] == "+":
                result = int(calculations[len(calculations)-1-a][0]) + int(calculations[len(calculations)-1-a][1])
            else:
                result = int(calculations[len(calculations)-1-a][0]) - int(calculations[len(calculations)-1-a][1])
            l4 = addtostr(l4, str(result))
            while not len(ref[len(calculations)-1-a]) == len(str(result)):
                l4 = addtostr(l4, " ")
                result = result*10

            if a+1 != len(calculations):
                l4 = addtostr(l4, "    ")
        result = l1+"\n"+l2+"\n"+l3+"\n"+l4
        print(result)
        return result
    else:
      result = l1+"\n"+l2+"\n"+l3
      print(result)
      return result

