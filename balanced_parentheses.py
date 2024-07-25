import sys
string = input()
stack = []
for i in string:
    if i == '(':
        stack.append(')')
    elif i == ')':
        if stack:
            stack.pop()
        else:
            print("No")
            sys.exit()

if not stack:
    print("Yes")
else:
    print("No")
