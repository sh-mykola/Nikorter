string = """move.up(2);
move.down(1);
move.right(4);
fbf.r"""

print(string + "\n\n")

symbols = ['(', ')', '.', ';', '\n'] # single-char keywords
keywords = ['move', 'up', 'down', 'left', 'right', 'int']
KEYWORDS = symbols + keywords

white_space = ' '
lexeme = ''

for i, char in enumerate(string):
    if char != white_space:
        lexeme += char # adding a char each time
    if (i+1 < len(string)): # prevents error
        if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
            if lexeme != '':
                print(lexeme.replace('\n', '<newline>'))
                lexeme = ''