# main function
def main():
    # input file name
    file_name = input("Enter file name: ")

    # open file
    global program_file
    try:
        program_file = open(file_name, 'r')
    except:
        print('File not found')
        y = input("Press enter to close")
        return

    # declare variables
    global line_num, char_num, current_pos, keywords, letters, digits, all_lines, lexeme, line, special_symbols
    global improper_char
    line_num = 1 # tracks line number
    char_num = 1 # tracks char number in line
    current_pos = 0 # tracks index in line
    lexeme = '' # current lexeme
    line = '' # current line
    improper_char = False # checks if an unknown char has been encountered
    keywords = {"program", "end", "bool", "int", "while", "do", "od", "print", "or",
        "and", "false", "true", "if", "fi", "then"}
    special_symbols = {":", ";", ":=", "!=", "+", "-", "or", "*", "<", ">", "=", "=<", ">=", "/", "(", ")",}
    letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    # get all lines
    all_lines = program_file.readlines()

    # see if file is empty
    if len(all_lines) == 0:
        pass
    elif len(all_lines) == 1:
        # tokenize the only token
        next()
        print(position(), end=' ')
        print(kind(), end=' ')
        print(value())
    else:
        # begin with first token
        next()
        print(position(), end=' ')
        print(kind(), end=' ')
        print(value())
        # if more tokens exist or if there are more unread characters on the current line, continue loop
        while (improper_char == False) and (current_pos + 1 != len(line) or line != all_lines[-1] and line_num + 1 != len(all_lines)):
            next()
            print(position(), end=' ')
            print(kind(), end=' ')
            print(value())

    # check if unknown char was found
    if improper_char == False:
        # once file has been fully read, create 'end-of-text' lexeme
        lexeme = 'end-of-text'
        line_num += 1
        current_pos = 0
        char_num = current_pos + 1
        print(position(), end=' ')
        print(kind(), end=' ')
        print(value())
    else:
        print("\"" + line[current_pos] + "\"" + " found at position " + str(current_pos) + " on line " + str(line_num))
    
    x = input("Press enter to close")
    program_file.close()

# read next token
def next():
    global line_num, char_num, current_pos, keywords, letters, digits, all_lines, lexeme, line, special_symbols
    global improper_char
    endline = False # records if we are at the end of the line

    token = ''
    try:
        line = all_lines[line_num - 1]
    except:
        return

    # check if char is newline
    if line[current_pos] == '\n':
        current_pos = 0
        line_num += 1
        line = all_lines[line_num - 1]
    
    # check if next char is newline
    if current_pos + 1 == len(line):
        endline = True

    # update char_num
    char_num = current_pos + 1
    
    # move to start of next token
    while line[current_pos] == ' ':
        current_pos += 1
        char_num = current_pos + 1

    # check if comment
    if endline == False and line[current_pos] == '/' and line[current_pos + 1] == '/':
        current_pos = 0
        char_num = current_pos + 1
        line_num += 1
        token = None
        lexeme = ''
        if all_lines[-1] == line:
            return
        next()
        return

    # begin constructing token
    for i in range(current_pos, len(line)):
        # check if first char is a letter
        if line[i] in letters:
            token += line[i]
            # iterate through all letters and digits
            for j in range(current_pos + 1, len(line)):
                if line[j] in letters or line[j] in digits or line[j] == '_':
                    token += line[j]
                    current_pos = j
                else:
                    current_pos = j
                    break
            break # once token is written, break

        # check if first char is a digit
        if line[i] in digits:
            token += line[i]
            # iterate through all digits
            for j in range(current_pos + 1, len(line)):
                if line[j] in digits:
                    token += line[j]
                else:
                    current_pos = j
                    break
            break # once token is written, break

        # check if relational operator
        if line[i] == '<':
            token += line[i]
            current_pos += 1
            break
        elif line[i] == '>':
            if line[i + 1] == '=':
                token += line[i] + line[i + 1]
                current_pos += 2
                break
            else:
                token += line[i]
                current_pos += 1
                break
        elif line[i] == '=':
            if line[i] == '<':
                token += line[i] + line[i + 1]
                current_pos += 2
                break
            else:
                token += line[i]
                current_pos += 1
                break
        elif line[i] == '!' and line[i + 1] == '=':
            token += line[i] + line[i + 1]
            current_pos += 2
            break

        # check if ':' or ':='
        if line[i] == ':':
            if line[i + 1] == '=':
                token += line[i] + line[i + 1]
                current_pos += 2
                break
            else:
                token += line[i]
                current_pos += 1
                break

        # check if ';'
        if line[i] == ';':
            token += line[i]
            current_pos += 1
            break

        # check if '(' or ')'
        if line[i] == '(' or line[i] == ')':
            token += line[i]
            current_pos += 1
            break

        # check if mathematical operators
        if line[i] == '+' or line[i] == '-' or line[i] == '*' or line[i] == '/':
            token += line[i]
            current_pos += 1
            break

        # if none of the above, must be an improper character
        improper_char = True
        break
    
    lexeme = token

# returns position of current token
def position():
    # only applies if comment found
    if lexeme == '':
        return ''

    # if anything else, return line_num and char_num
    return '(Line: ' + str(line_num) + ', Character: ' + str(char_num) + ')'

# returns kind
def kind():
    global lexeme, keywords, special_symbols

    # only applies if comment found
    if lexeme == '':
        return ''

    # check if keyword or special symbol
    if lexeme in special_symbols or lexeme in keywords:
        return "\"" + lexeme + "\""

    # check if end-of-text
    if lexeme == 'end-of-text':
        return "\"end-of-text\""
    
    # check if int
    try:
        lexeme = int(lexeme)
        return "\"NUM\""
    except:
        # if not an int or anything else, must be id
        return "\"ID\""

# returns value
def value():
    global lexeme, keywords, special_symbols

    # only applies if comment found
    if lexeme == '':
        return ''

    # check if 'end-of-text'
    if lexeme == 'end-of-text':
        return ''

    # check if keyword
    if lexeme in keywords:
        return ''

    # check if special symbol
    if lexeme in special_symbols:
        return ''
    
    # check if num or id
    try:
        lexeme = int(lexeme) # if successfully turned into an int, return value
        return str(lexeme)
    except:
        # if not an integer, must be an ID
        return lexeme

# Take us to main function at top of screen
if __name__ == '__main__':
    main()