def basic_op(op,n1,n2):
    total = 0
    if op == '+':
        total = n1 + n2
    elif op == '-':
        total = n1 - n2
    elif op == '/':
        total = n1 / n2
    elif op == '*':
        total = n1 * n2
    return total
    
print(basic_op('*',10,2))