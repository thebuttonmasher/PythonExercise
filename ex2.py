
if __name__ == '__main__':
    summ = 0
    inp = input("select subExercise 1 or 2")
    if inp == '1':
        while inp != "stop":
            inp = input("enter numbers, type stop to stop \n")
            summ = int(inp) + summ
        print(summ)
    else:
        inp = input("enter list")
        result = [x.strip() for x in inp.split(',')]
        summ = 0
        for x in result:
            summ = summ + int(x)

        print(summ)
# eof