import sys

def is_numeric(x):
    try:
        float(x)
        return True
    except:
        return False

def apply_operand(left, right, op):

    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        return left / right
    if op == '^':
        return left ** right

operand_stack = []
inp = raw_input("> ")
inp_list = inp.split(' ')

for i in inp_list:

    if is_numeric(i):
        operand_stack.append(float(i))

    elif i == '+' or '-' or '*' or '/' or '^':

        if len(operand_stack) < 2: 
            print "Error: Too many operands."
            exit()   

        else:
            right = operand_stack.pop()
            left = operand_stack.pop()
            operand_stack.append(apply_operand(left, right, i))

    else:
        print "Error: %s is not a valid argument." % i
        exit()

if len(operand_stack) != 1:
    print "Error: not enough opearators"
    sys.exit()

print operand_stack[0]
