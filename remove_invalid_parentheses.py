from collections import Counter


def is_balanced(str):
    stack = []
    for i in str:
        if i == '(':
            stack.append(')')
        else:
            if stack:
                stack.pop()
            else:
                return False

    if not stack:
        return True
    else:
        return False


str = input("Enter the string:")
possible_str = set()
for i in range(len(str)):
    new_str = ""
    new_str = str[:i]+str[i+1:]
    if is_balanced(new_str):
        possible_str.add(new_str)

print(list(possible_str))
