def countstr(str2):
    out = ""
    for x in str2:
        if x not in out:
            out = out + x + str(str2.count(x))
    return out


if __name__ == '__main__':
    str2 = input("enter string")
    print(countstr(str2))