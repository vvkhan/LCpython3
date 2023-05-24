#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#Constrains:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def isValid(s):
    d = {"(": ")", "{": "}", "[": "]"}
    stack = []
    if len(s) % 2 == 1 or s[0] in d.values() or s[len(s)-1] in d.keys() or 1 > len(s) > 104:
        return False
    else:
        for i in s:
            if i in d.keys():
                stack.append(d[i])
            if i in d.values():
                if len(stack) != 0 and i != stack.pop():
                    return False

    if len(stack) == 0:
        return True
    else:
        return False

r1 = isValid("()")
print(r1)
r2 = isValid("()[]{}")
print(r2)
r3 = isValid("(]")
print(r3)
r4 = isValid("[")
print(r4)
r5 = isValid("((")
print(r5)
r6 = isValid("){")
print(r6)
r7 = isValid("({{{{}}}))")
print(r7)
r8 = isValid("[[[]")
print(r8)
r9 = isValid("()))")
print(r9)