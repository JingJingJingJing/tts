import sys
import addition
import compare
import synctags

def main():
    args = sys.argv[1:]
    if len(args) >= 1:
        if args[0] == "tts":
            func = args[1]
            if func == "synca":
                synctags.main()
            elif func == "add":
                addition.main()
            elif func == "compare":
                compare.main()
        else:
            print("please enter tts synca/add/compare")

if __name__ == '__main__':
    main()