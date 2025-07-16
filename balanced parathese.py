def is_balanced(expr):
    stack = []
    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in"]})":
            if not stack:
                return False
            top  = stack.pop()
            if(ch == ')' and top != '(')or\
              (ch == '}' and top != '{')or\
              (ch == ']' and top != '['):
               return False
    return len(stack) == 0
print(is_balanced("(([]){})"))
print(is_balanced("{[}]"))
    
            