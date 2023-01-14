def scoreOfParentheses(s: str) -> int:
    stack = []
    for c in s:
        if ord(c) == ord('('):
            stack.append(ord(c))
        else:
            c1 = stack.pop()
            if c1 == ord('('):
                stack.append(ord('1'))
            else:
                c1 = stack.pop()
                count = c1 - ord('0')
                while c1 != ord('('):
                    c1 = stack.pop()
                    count += c1 - ord('0')
                count = count << 1
                stack.append(count + ord('0'))
                chr(count)
    res = 0
    while stack:
        res += stack.pop() - ord('0')
    return res


count = 15
print(ord('0'))
print(count + ord('0'))
print(ord('('))