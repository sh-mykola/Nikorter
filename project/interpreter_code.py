import logging

logger = logging.Logger('catch_all')
tokens = []

final_code = []
last_commands = []
tree = ""
tree_last = ""

code = """move.up(22)
move.down(22)"""


# print(code + "-" * 20)


def lexer(plain_code):
    tok = ""
    open_br = False
    temp_number = ""

    global tokens

    plain_code = list(plain_code)
    print(plain_code)

    for char in plain_code:
        tok += char
        if tok == " ":
            tok = ""
        elif tok.lower() == "move":
            tokens.append("MOVE")
            tok = ""
        elif tok.lower() == "last":
            tokens.append("LAST")
            tok = ""
        elif tok == ".":
            tokens.append("DOT")
            tok = ""
        elif tok.lower() == "up":
            tokens.append("UP")
            tok = ""
        elif tok.lower() == "down":
            tokens.append("DOWN")
            tok = ""
        elif tok.lower() == "right":
            tokens.append("RIGHT")
            tok = ""
        elif tok.lower() == "left":
            tokens.append("LEFT")
            tok = ""
        elif tok == "(":
            tokens.append("OPEN_BRACKET")
            open_br = True
            tok = ""
        elif tok == ")":
            """print(temp_number)
            print("FOUND CLOSE_BRACKET")"""
            tokens.append("NUMBER:" + temp_number)
            tokens.append("CLOSE_BRACKET")
            open_br = False
            temp_number = ""
            tok = ""
        elif open_br:
            if tok in "1234567890":
                temp_number += char
            else:
                tokens = ["Error!"]
                return tokens
            tok = ""
        elif tok == "\n":
            tok = ""
        else:
            if tok not in "move.updownrightleft(0987654321)last":
                tokens = ["Error!"]
                return tokens

    print(tokens)
    return tokens


def parser(toks):
    if toks[0] == "Error!":
        print(toks[0])
        return

    i = 0
    global tree
    global tree_last
    global final_code
    global last_commands
    command_list = []
    while i < len(toks) - 1:
        if toks[i] + " " + toks[i + 1] == "MOVE DOT":
            command_list.append("move")
            tree += "move\n"
            # print("FOUND ENTRY")
            if toks[i + 2] == "UP":
                # print("FOUND UP")
                command_list.append("up")
                tree += "\tup\n"
                i += 1
            elif toks[i + 2] == "DOWN":
                # print("FOUND DOWN")
                command_list.append("down")
                tree += "\tdown\n"
                i += 1
            elif toks[i + 2] == "RIGHT":
                # print("FOUND RIGHT")
                command_list.append("right")
                tree += "\tright\n"
                i += 1
            elif toks[i + 2] == "LEFT":
                # print("FOUND LEFT")
                command_list.append("left")
                tree += "\tleft\n"
                i += 1
            if toks[i + 3][0:7] == "NUMBER:":
                number = toks[i + 3][7:]
                command_list.append(number)
                tree += "\t\t{}\n".format(number)
                i += 2
            i += 2
            final_code.append(build_command(command_list))
            command_list = []

        elif toks[i] + " " + toks[i + 1] + " " + toks[i + 2] + " " + toks[i + 3] == "LAST DOT MOVE DOT":
            command_list.append("move")
            tree_last += "last\n"
            tree_last += "\tmove\n"
            # print("FOUND ENTRY")
            if toks[i + 4] == "UP":
                # print("FOUND UP")
                command_list.append("up")
                tree_last += "\t\tup\n"
                i += 1
            elif toks[i + 4] == "DOWN":
                # print("FOUND DOWN")
                command_list.append("down")
                tree_last += "\t\tdown\n"
                i += 1
            elif toks[i + 4] == "RIGHT":
                # print("FOUND RIGHT")
                command_list.append("right")
                tree_last += "\t\tright\n"
                i += 1
            elif toks[i + 4] == "LEFT":
                # print("FOUND LEFT")
                command_list.append("left")
                tree_last += "\t\tleft\n"
                i += 1
            if toks[i + 5][0:7] == "NUMBER:":
                number = toks[i + 5][7:]
                command_list.append(number)
                tree_last += "\t\t\t{}\n".format(number)
                i += 2
            i += 4
            last_commands.append(build_command(command_list))
            command_list = []

        i += 1


def build_command(element_list):
    string = ""
    # move_up(self, 2, timer())
    if element_list[0] == "move":
        string += element_list[0] + "_" + element_list[1] + "(self, " + element_list[2] + ", timer())"
    return string


def run(input_code):
    global final_code, last_commands, tree
    errors = False

    toks = lexer(input_code)

    try:
        parser(toks)
    except BaseException as e:
        logger.error("Something wrong!")
        errors = True

    data = [final_code + last_commands, tree + tree_last, errors]
    print(data)
    return data
