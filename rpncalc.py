import sys
import operator

def is_numeric(x):

    try:
        float(x)
        return True
    except:
        return False

operand_stack = []
inp = raw_input("> ")
inp_list = inp.split(' ')

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.div,
       '^': pow}

for i in inp_list:

    if is_numeric(i):
        operand_stack.append(float(i))

    elif i in {'+', '-', '*','/','^'}:

        if len(operand_stack) < 2: 
            print "Error: Not enough operands."
            exit()   

        else:
            right = operand_stack.pop()
            left = operand_stack.pop()
            operand_stack.append(ops[i](left, right))

    else:
        print "Error: %s is not a valid argument." % i
        exit()

if len(operand_stack) != 1:
    print "Error: not enough operators"
    sys.exit()

print operand_stack[0]
