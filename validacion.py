import sys

def validator(str):
    try:
        if int(str):
            str = int(str)
            return str
    except ValueError:
        try:
            if float(str):
                str = float(str)
                return str
        except ValueError:
            print ("ERROR")

def main():
    leng = len(sys.argv)
    if leng == 2:
        str = sys.argv[1]
        validator(str)
    else:
        print("ERROR")

if __name__ == "__main__":
    main()