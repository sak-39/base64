import sys
import json

def main():

    f = open("table.json", "r")
    dict = json.loads(f.read())
    f.close()

    argvs = sys.argv

    if len(argvs) != 2:
        sys.exit()
    
    bin_text = ""

    # text to bin
    strlist = [c for c in argvs[1]]
    for item in strlist:
        bin_text += format(ord(item), 'b').zfill(8)
    
    while len(bin_text) % 6 != 0:
        bin_text += "00"

    bin_list = []
    
    # split every 6 digits
    for i in range(int(len(bin_text)/6)):
        n = i*6
        bin_list.append(bin_text[n:n+6])

    # encode text
    enc = ""

    # convert with dictionary
    for buf in bin_list:
        enc += dict[buf]

    if len(enc) % 4 != 0:
        enc += "=="
    
    print("Result: " + enc)

if __name__ == '__main__':
    main()
