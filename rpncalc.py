import sys
import operator

operand_stack = []
inp = raw_input("> ")
inp_list = inp.split(' ')

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.div,
       '^': pow}

for i in inp_list:

    try: operand_stack.append(float(i))

    except: 

        if i in {'+', '-', '*','/','^'}:

            if len(operand_stack) < 2: 
                print "Error: Too many operators."
                exit()   

            else:
                right = operand_stack.pop()
                left = operand_stack.pop()
                operand_stack.append(ops[i](left, right))

        else:
            print "Error: %r is not a valid argument." % i
            exit()

if len(operand_stack) != 1:
    print "Error: Not enough operators"
    sys.exit()

print operand_stack[0]
