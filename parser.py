import main


def ppreorder(tree, indent): # printing parse tree.
    if tree != None:
        write_string = indent + tree.root + ":" + tokens_dict[tree.root] + "\n"
        print(write_string)
        # print(indent, tree.root, ":", tokens_dict[tree.root])
        indent += "         "
        ppreorder(tree.left, indent)
        if tree.center != None:
            ppreorder(tree.center, indent)
        ppreorder(tree.right, indent)

class Node:
    def __init__(self, root, left, center, right):
        self.root = root
        self.left = left
        self.center = center  # middle node
        self.right = right


class Parser:
    def __init__(self, scanned_tokens, tokens_dict):
        self.index = 0
        self.tokens = scanned_tokens
        self.tokens_dict = tokens_dict

    def next_token(self):
        if self.index < len(self.tokens):
            var = list(self.tokens)[self.index]
            return var

    def token_type(self):
        if self.index < len(self.tokens):
            return self.tokens_dict[self.next_token()]

    def consume_token(self):
        self.index += 1


scanned = main.tokens_list
tokens_dict = main.tokens()
parser = Parser(scanned, tokens_dict)


def parse_statement():
    tree = parse_base_statement()
    while parser.next_token() == ";":
        parser.consume_token()
        tree = Node(";", tree, None, parse_base_statement())

    return tree


def parse_base_statement():
    if parser.next_token() is None:
        return None
    else:
        if parser.token_type() == "IDENTIFIER":
            return parse_assignment()

        elif parser.next_token() == "if":
            return parse_if_statement()

        elif parser.next_token() == "while":
            return parse_while_statement()

        elif parser.next_token() == "skip":
            return Node("skip", None, None, None)

        else:
            return parse_expression()


def parse_assignment():
    if parser.token_type() == "IDENTIFIER":
        temp = Node(parser.next_token(), None, None, None)
        parser.consume_token()
        if parser.next_token() == ":=":
            parser.consume_token()
            tree = parse_expression()
            return Node(":=", temp, None, tree)

    try:
        raise Exception
    except:
        print("Syntax Error")


def parse_while_statement():
    print("while")
    if parser.next_token() == "while":
        print("w")
        parser.consume_token()
        tree1 = parse_expression()
        if parser.next_token() == "do":
            parser.consume_token()
            tree2 = parse_statement()
            parser.consume_token()
            print(parser.next_token())
            if parser.next_token() == "endwhile" or parser.next_token() == None:
                parser.consume_token()
                return Node("while", tree1, None, tree2)



def parse_if_statement():
    if parser.next_token() == "if":
        parser.consume_token()
        tree1 = parse_expression()
        if parser.next_token() == "then":
            parser.consume_token()
            tree2 = parse_statement()
            if parser.next_token() == "else":
                parser.consume_token()
                tree3 = parse_statement()
                if parser.next_token() == "endif":
                    parser.consume_token()
                    return Node("if", tree1, tree2, tree3)

    # try:
    #     raise Exception
    # except:
    #     print("Syntax Error")

def parse_expression():
    tree = parse_term()
    while parser.next_token() == "+":
        parser.consume_token()
        tree = Node("+", tree, None, parse_term())

    return tree


def parse_term():
    tree = parse_factor()
    while parser.next_token() == "-":
        parser.consume_token()
        tree = Node("-", tree, None, parse_factor())

    return tree


def parse_factor():
    tree = parse_piece()
    while parser.next_token() == "/":
        parser.consume_token()
        tree = Node("/", tree, None, parse_piece())

    return tree


def parse_piece():
    tree = parse_element()
    while parser.next_token() == "*":
        parser.consume_token()
        tree = Node("*", tree, None, parse_element())

    return tree


def parse_element():
    if parser.next_token() == "(":
        parser.consume_token()
        tree = parse_expression()
        if parser.next_token() == ")":
            parser.consume_token()
            return tree
        else:
            try:
                raise Exception
            except:
                print("Syntax Error")

    else:
        if parser.token_type() == "NUMBER":
            temp = parser.next_token()
            parser.consume_token()
            return Node(temp, None, None, None)

        elif parser.token_type() == "IDENTIFIER":
            temp = parser.next_token()
            parser.consume_token()
            return Node(temp, None, None, None)



tree = parse_statement()  # returns the complete tree

def parse_tree():
    return tree

