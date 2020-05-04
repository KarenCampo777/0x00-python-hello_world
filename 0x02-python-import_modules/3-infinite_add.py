#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = len(sys.argv) - 1
    sum = 0
    if res == 0:
        print("{}".format("0"))
    else:
        for num in range(1, res + 1):
            sum = sum + int(sys.argv[num])
        print(sum)  
