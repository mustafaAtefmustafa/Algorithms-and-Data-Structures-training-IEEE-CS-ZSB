"""Jabber ID"""
import re

def main():
    s = input()
    reg = re.compile(r'^\w{1,16}@(\w{1,16}\.)*\w{1,16}(/\w{1,16})?$')
    
    if reg.match(s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()