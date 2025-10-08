TEXT = "2.0 -4.5 1.7\n0.3 1.6 9.0\n"

def main():

    # row = "0.3 1.6 9.0 "

    # print(row.split())
    # print(row.split(" "))

    ret = 0
    print(TEXT.split("\n"))
    for row in TEXT.split('\n'):
        v = row.split()
        ret = ret + float(v[1])
        print("v är", v)
    print("ret är", ret)

main()