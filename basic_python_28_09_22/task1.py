def is_correct(text):
    leftBrackets = ('(', '{', '[')
    rightBrackets = (')', '}', ']')
    stack = list()

    for symb in text:
        if symb in leftBrackets:
            stack.append(symb)

        if symb in rightBrackets:    
            bracketType = rightBrackets.index(symb)

            if len(stack) and (stack[-1] == leftBrackets[bracketType]):
                stack.pop()
            else: 
                return False  

    return (not stack)
    

if __name__ == '__main__':
    print("Please enter a line: ")
    s = input()

    print(is_correct(s))
