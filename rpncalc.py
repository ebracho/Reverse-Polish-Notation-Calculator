import sys
import operator

print "Reverse Polish Notation Calculator. Type 'quit' to exit."

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.div,
       '^': pow}

def calculate(inp_list, operand_stack):

    for i in inp_list:

        try: operand_stack.append(float(i))

        except ValueError: 
            if i in ops:
                if len(operand_stack) < 2: 
                    print "Error: Too many operators. Resetting."
                    return ['reset']
                else:
                    right = operand_stack.pop()
                    left = operand_stack.pop()
                    operand_stack.append(ops[i](left, right))
            elif i == '':
                return operand_stack
            elif i == 'quit':
                exit()
            else:
                print "Error: %r is not a valid argument. Resetting." % i
                return ['reset']

    return operand_stack

operand_stack = []
prompt = "> "

while(True):
    inp_list = []
    inp_list.extend(raw_input(prompt).split(' '))

    operand_stack = calculate(inp_list, operand_stack)               

    if operand_stack[0] == 'reset':
        operand_stack[:] = []
        prompt = "> "

    elif len(operand_stack) != 1:
        print "Error: Not enough operators. Resetting."
        operand_stack[:] = []
        prompt = "> "
        continue
        

    else :prompt = str(operand_stack[0]) + ' '
