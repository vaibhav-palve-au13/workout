def sol(s):
    stack=[]
    for c in s:
        if stack and stack[-1]==c.swapcase():
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
if __name__ == "__main__":
    a=sol("vaiiIbhav")
    print(a)
