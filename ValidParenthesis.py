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
    flag = True
    if len(s) % 2 == 1:
        flag = False
    elif 1 <= len(s) <= 104:
        for i in range(len(s)-1):
            if s[i] in d.keys():
                flag = False
                if s[i+1] == d[s[i]]:
                    flag = True
    else:
        flag = False
    return flag


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