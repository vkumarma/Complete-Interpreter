import re
import sys


class Lexer:
    def __init__(self, inp_str):
        self.index = 0
        self.s = inp_str

    def get_char(self):
        if self.index < len(self.s):
            var = self.s[self.index]
            self.index += 1
            return var


input_file = open(str(sys.argv[1]), 'r')  # Open file for reading
line = input_file.read()
# "if z then while x * 4 - 2 do skip endwhile else x := 7 endif; y := 1"
input_string = line.strip("\n")
lexer = Lexer(input_string)

hashtable = {}
tokens_list = []
def token_check(input):
    if re.fullmatch("if|then|else|endif|while|do|endwhile|skip", input):
        hashtable[input] = "KEYWORD"
        tokens_list.append(input)
    elif re.search("([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*", input):
        hashtable[input] = "IDENTIFIER"
        tokens_list.append(input)
    elif re.search("[0-9]+", input):
        hashtable[input] = "NUMBER"
        tokens_list.append(input)
    elif re.fullmatch("\+|\-|\*|/|\(|\)|:=|;", input):
        hashtable[input] = "SYMBOL"
        tokens_list.append(input)
    else:
        hashtable[input] = "ERROR READING"


def digit(curr_char, lexer):
    sub = ""
    while (curr_char.isdigit()):
        sub += curr_char
        curr_char = lexer.get_char()
        if curr_char == None:
            break
    new.append(curr_char)
    return sub


def longest_sub_string(curr_char, lexer):
    sub = ""
    while (curr_char.isalpha() or curr_char.isdigit()):
        sub += curr_char
        curr_char = lexer.get_char()
        if curr_char == None:
            break

    new.append(curr_char)
    return sub


def symbol(curr_char, lexer):
    # print(curr_char)
    sym = curr_char
    curr_char = lexer.get_char()
    new.append(curr_char)
    return sym


def assignment(curr_char, lexer):
    sub = curr_char
    next_char = lexer.get_char()
    if next_char == "=":
        sub += next_char
        new.append(next_char)
        return sub
    new.append(lexer.get_char())
    return sub


new = []  # keeping track of current char.
curr_char = lexer.get_char()
while (curr_char != None):

    while (curr_char == ' ' or curr_char == ''):
        curr_char = lexer.get_char()

    if (curr_char.isdigit()):
        token_check(digit(curr_char, lexer))
        curr_char = new.pop()

    elif (curr_char.isalpha()):
        token_check(longest_sub_string(curr_char, lexer))
        curr_char = new.pop()

    elif curr_char in "+-/*();":
        token_check(symbol(curr_char, lexer))
        curr_char = new.pop()

    elif curr_char == ":":
        token_check(assignment(curr_char, lexer))
        curr_char = new.pop()
        if curr_char == "=":
            curr_char = lexer.get_char()

    else:
        token_check(curr_char)
        curr_char = lexer.get_char()


def tokens():
    return hashtable

# print(tokens_list)
# print(tokens())
