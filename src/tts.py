import sys
import addition
import compare
import synctags
import txt2json
import pickone
import fillup

def main():
    args = sys.argv[1:]
    if len(args) >= 1:
        func = args[0]
        if func == "synca":
            synctags.main()
        elif func == "add":
            addition.main()
        elif func == "compare":
            compare.main()
        elif func == "txt2json":
            txt2json.main()
        elif func == "pickone":
            pickone.main()
        elif func == "fillup":
            fillup.main()

    else:
        print("please enter synca/add/compare/txt2json/pickone")

if __name__ == '__main__':
    main()