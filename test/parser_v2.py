def parser(toks):
    if toks[0] == "Error!":
        raise ValueError("Something bad in parser!")

    global tree
    global tree_last
    global final_code
    global last_commands

    command_list = []

    looping = False

    main_range = len(toks) - 1
    loop_times = 0
    tree_id = 1
    i = 0

    for a in range(main_range):
        if a < main_range:
            if toks[a] == toks[a + 1]:
                raise ValueError('Repeated code!')

    while i < main_range:
        if toks[i] == "MOVE":
            if toks[i + 1] != "DOT":
                raise ValueError('Bad code!')

            current_dir = ""
            current_num = ""

            command_list.append("move")
            tree += "\nroot move.{}".format(tree_id)

            if toks[i + 2] == "UP":
                current_dir = "up"

                command_list.append("up")
                if looping:
                    tree += "loop.{} move.{}\nmove.{} up".format(tree_id, tree_id, tree_id)
                else:
                    tree += "\nmove.{} up".format(tree_id)
                i += 1
            elif toks[i + 2] == "DOWN":
                current_dir = "down"

                command_list.append("down")
                tree += "\nmove.{} down".format(tree_id)
                i += 1
            elif toks[i + 2] == "RIGHT":
                current_dir = "right"

                command_list.append("right")
                tree += "\nmove.{} right".format(tree_id)
                i += 1
            elif toks[i + 2] == "LEFT":
                current_dir = "left"

                command_list.append("left")
                tree += "\nmove.{} left".format(tree_id)
                i += 1
            else:
                raise ValueError('Bad code!')

            if toks[i + 3][0:7] != "NUMBER:":
                raise ValueError('Bad code!')

            number = toks[i + 3][7:]
            current_num = number
            if number == "":
                raise ValueError('Missing number!')
            command_list.append(number)
            if looping:
                number = str(int(number) * loop_times) + "_with_loop"
                current_num = number

            tree += "\n{} {}".format(current_dir, current_num)
            i += 2

            try:
                if toks[i + 3] + " " + toks[i + 4] == "DOT ANIMATION":
                    if toks[i + 6][0:7] != "NUMBER:":
                        raise ValueError('Bad code!')

                    number = toks[i + 6][7:]
                    if number == "":
                        raise ValueError('Missing number!')

                    command_list.append(number)
                    tree += "\n{} animation\nanimation {}".format(current_num, number)

                    try:
                        if toks[i + 8] == "DOT":
                            raise ValueError('Bad code!')
                    except IndexError:
                        pass
            except IndexError:
                pass

            print(command_list)
            final_code.append(build_command(command_list))

            command_list = []
            looping = False
            tree_id += 1
            i += 2