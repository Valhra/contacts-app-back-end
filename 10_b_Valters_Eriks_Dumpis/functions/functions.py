def SumTwoNumbers(a, b):
    return a+b

def JoinStings(text1, text2, delimiter):
    return f"{text1}{delimiter}{text2}"

result = JoinStings('One', 'Two', '-')
print(result)