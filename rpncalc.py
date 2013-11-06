import sys

def is_numeric(x):
    try:
        float(x)
        return True
    except:
        return False

def operand_err():
    print "Too many operands"
    sys.exit()

operand_stack = []
inp = raw_input("> ")
inp_list = inp.split(' ')

for i in inp_list:

    if is_numeric(i):
        operand_stack.append(float(i))

    elif i == '+':
        if len(operand_stack) == 0: operand_err()
        right_operand = operand_stack.pop()
        if len(operand_stack) == 0: operand_error()
        left_operand = operand_stack.pop()
        operand_stack.append(left_operand + right_operand)

    elif i == '-':
        if len(operand_stack) == 0: operand_err()
        right_operand = operand_stack.pop()
        if len(operand_stack) == 0: operand_err()
        left_operand = operand_stack.pop()
        operand_stack.append(left_operand - right_operand)

    elif i == '*':
        if len(operand_stack) == 0: operand_err()
        right_operand = operand_stack.pop()
        if len(operand_stack) == 0: operand_err()
        left_operand = operand_stack.pop()
        operand_stack.append(left_operand * right_operand)

    elif i == '/':
        if len(operand_stack) == 0: operand_err()
        right_operand = operand_stack.pop()
        if len(operand_stack) == 0: operand_err()
        left_operand = operand_stack.pop()
        operand_stack.append(left_operand / right_operand)

    elif i == '^':
        if len(operand_stack) == 0: operand_err()
        right_operand = operand_stack.pop()
        if len(operand_stack) == 0: operand_err()
        left_operand = operand_stack.pop()
        operand_stack.push(left_operand ** right_operand)

    else:
        print "Invalid input."
        exit()


if len(operand_stack) != 1:
    print "Invalid input, not enough opearators"
    sys.exit()

print operand_stack[0]
