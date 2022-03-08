import parser
import main
import operator
import sys

tokens = main.tokens_list
tokens_dict = main.tokens()
tree = parser.parse_tree()

def scanned_tokens(): # printing scanned tokens
    for token in tokens:
        output_file.write(token + ":" + tokens_dict[token] + "\n")
    output_file.write("\n")


def preorder(tree, indent): # printing parse tree.
    if tree != None:
        write_string = indent + tree.root + ":" + tokens_dict[tree.root] + "\n"
        output_file.write(write_string)
        # print(indent, tree.root, ":", tokens_dict[tree.root])
        indent += "         "
        preorder(tree.left, indent)
        if tree.center != None:
            preorder(tree.center, indent)
        preorder(tree.right, indent)



###################################################################################


def memory(data,memoryMap):
    if data in memoryMap:
        return str(memoryMap[data])
    return data

def check_pattern(stack):
    operators = { "+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.truediv}

    size = len(stack)
    map = {'+': 1,'-': 1,'/': 1,'*': 1}
    if size >= 3:
        if stack[size-1].isdigit() and stack[size-2].isdigit():
            if stack[size-3] in map:
                try:
                    var = str(int(operators[stack[size-3]](int(stack[size-2]),int(stack[size-1]))))
                except:
                    print("Divsion by Zero not allowed")
                    output_file.write("Division by Zero not allowed")
                    quit(5)
                for i in range(3):
                    stack.pop()
                stack.append(var) if int(var) >= 0 else stack.append('0')
                return stack

    return stack


def evaluate(node,stack,memoryMap):
    if node != None:

        stack.append(memory(node.root,memoryMap))
        stack = check_pattern(stack)

        evaluate(node.left,stack,memoryMap)
        stack = check_pattern(stack)

        evaluate(node.right,stack,memoryMap)
        stack = check_pattern(stack)

    stack = check_pattern(stack)
    return stack


def assign(node,memoryMap):
    #print(node.left.data,node.right.data)
    if node.root == ':=':
        x = int(evaluate(node.right,[],memoryMap)[0])
        memoryMap[node.left.root] = x
        return node

def mapping(node,memoryMap):

    if node is not None:
        if node.root == 'if':
            if int(evaluate(node.left,[],memoryMap)[0]) > 0:
                return mapping(node.center,memoryMap)
            else:
                return mapping(node.right,memoryMap)

        if node.root =='while':
            if int(evaluate(node.left,[],memoryMap)[0]) > 0:
                temp = parser.Node(";",None,None,None)
                temp.right = node
                temp.left = node.right
                try:
                     mapping(temp,memoryMap)
                except RecursionError as re:
                    print("While loop is infinite ")
                    output_file.write('\nOutput: Stuck in loop\n')
                    quit(7)
            else:
                return None

        if node.root == ';':
            node.left = mapping(node.left,memoryMap)
            node = node.right
            return mapping(node,memoryMap)

        return assign(node,memoryMap)


    return node









##################################################### Functions called #########
output_file = open(str(sys.argv[2]), 'w')
output_file.write("Tokens: \n")
output_file.write("\n")
scanned_tokens()
output_file.write("AST: \n")
output_file.write("\n")
preorder(tree, "")
output_file.write("\n")

# output_file.write("\n")
# output_file.write("Output: " + str(output))
memoryMap = {}
mapping(tree,memoryMap)



write = "\nOutput: \n"

for key in memoryMap:
    write = write + str(key) + ' = ' + str(memoryMap[key]) + '\n'
print(memoryMap)
output_file.write(write)
