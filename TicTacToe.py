import random

def main():
    print("Welcome to Tic Tac Toe.")
    whoFirst = input("Would you like to go first (y/n)? ")
    whoFirst = whoFirst.lower()
    while whoFirst != 'y' and whoFirst != 'n':
        print("Not valid. Try Again.")
        whoFirst = input("Would you like to go first (y/n)? ")
    if whoFirst == 'y':
        pFirst()
    elif whoFirst == 'n':
        cFirst()

def pFirst():
    ttt = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    compwon = False
    pwon = False
    found = False

    for i in range(3):
        print("| ", end = "")
        for j in range(3):
            print( ttt[i][j], end=' | ' )
        print()

    while compwon != True and pwon != True:
        choice = 0
        while not (choice >= 1 and choice <= 9):
            try:
                choice = int( input("Enter number: ") )
                while choice < 1 or choice > 9:
                    print("Invalid")
                    choice = int( input("Enter number: ") )
            except Exception:
                print("Not an accepted value. Try again.")

        # Player move
        found = False
        count = 0
        while found != True:
            for i in range(3):
                for j in range(3):
                    count += 1
                    if choice > count:
                        continue
                    if choice == ttt[i][j]:
                        ttt[i][j] = 'X'
                        found = True
                        break
                    else:
                        print("Spot " + str(choice) + " taken. Choosing again.")
                        choice = int( input("Enter number: ") )
                        while choice < 1 or choice > 9:
                            print("Invalid")
                            choice = int( input("Enter number: ") )
                        count = 0
                        break
                if found:
                    break

        # Check for player win
        if ttt[0][0] == 'X' and ttt[0][1] == 'X' and ttt[0][2] == 'X':
            pwon = True
        if ttt[1][0] == 'X' and ttt[1][1] == 'X' and ttt[1][2] == 'X':
            pwon = True
        if ttt[2][0] == 'X' and ttt[2][1] == 'X' and ttt[2][2] == 'X':
            pwon = True
        if ttt[0][0] == 'X' and ttt[1][1] == 'X' and ttt[2][2] == 'X':
            pwon = True
        if ttt[2][0] == 'X' and ttt[1][1] == 'X' and ttt[0][2] == 'X':
            pwon = True
        if ttt[0][0] == 'X' and ttt[1][0] == 'X' and ttt[2][0] == 'X':
            pwon = True
        if ttt[0][1] == 'X' and ttt[1][1] == 'X' and ttt[2][1] == 'X':
            pwon = True
        if ttt[0][2] == 'X' and ttt[1][2] == 'X' and ttt[2][2] == 'X':
            pwon = True

        if pwon:
            for i in range(3):
                print("| ", end = "")
                for j in range(3):
                    print( ttt[i][j], end=' | ' )
                print()
            break

    
        # -------------------------------------
        # write algorithm to try to have it so the computer tries to win
        # -------------------------------------


        # Computer move
        found = False
        comp = random.randint(1, 9)
        count = 0
        while found != True:
            for i in range(3):
                for j in range(3):
                    count += 1
                    if comp > count:
                        continue
                    if comp == ttt[i][j]:
                        ttt[i][j] = 'O'
                        found = True
                        break
                    else:
                        comp = random.randint(1, 9)
                        count = 0
                        break
                if found:
                    break

        # Check for computer win
        if ttt[0][0] == 'O' and ttt[0][1] == 'O' and ttt[0][2] == 'O':
            compwon = True
        if ttt[1][0] == 'O' and ttt[1][1] == 'O' and ttt[1][2] == 'O':
            compwon = True
        if ttt[2][0] == 'O' and ttt[2][1] == 'O' and ttt[2][2] == 'O':
            compwon = True
        if ttt[0][0] == 'O' and ttt[1][1] == 'O' and ttt[2][2] == 'O':
            compwon = True
        if ttt[2][0] == 'O' and ttt[1][1] == 'O' and ttt[0][2] == 'O':
            compwon = True
        if ttt[0][0] == 'O' and ttt[1][0] == 'O' and ttt[2][0] == 'O':
            compwon = True
        if ttt[0][1] == 'O' and ttt[1][1] == 'O' and ttt[2][1] == 'O':
            compwon = True
        if ttt[0][2] == 'O' and ttt[1][2] == 'O' and ttt[2][2] == 'O':
            compwon = True

        if compwon:
            for i in range(3):
                print("| ", end = "")
                for j in range(3):
                    print( ttt[i][j], end=' | ' )
                print()
            break

        # Print board after each round
        for i in range(3):
            print("| ", end = "")
            for j in range(3):
                print( ttt[i][j], end=' | ' )
            print()

    if compwon:
        print("The computer won! Better luck next time!")
    if pwon:
        print("You won! Hooray!")

def cFirst():
    ttt = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    compwon = False
    pwon = False
    found = False

    for i in range(3):
        print("| ", end = "")
        for j in range(3):
            print( ttt[i][j], end = ' | ' )
        print()

    while compwon != True and pwon != True:
        # -------------------------------------
        # write algorithm to try to have it so the computer tries to win
        # -------------------------------------

        # Computer move
        found = False
        comp = random.randint(1, 9)
        count = 0
        while found != True:
            for i in range(3):
                for j in range(3):
                    count += 1
                    if comp > count:
                        continue
                    if comp == ttt[i][j]:
                        ttt[i][j] = 'O'
                        found = True
                        break
                    else:
                        comp = random.randint(1, 9)
                        count = 0
                        break
                if found:
                    break

        # Check for computer win
        if ttt[0][0] == 'O' and ttt[0][1] == 'O' and ttt[0][2] == 'O':
            compwon = True
        if ttt[1][0] == 'O' and ttt[1][1] == 'O' and ttt[1][2] == 'O':
            compwon = True
        if ttt[2][0] == 'O' and ttt[2][1] == 'O' and ttt[2][2] == 'O':
            compwon = True
        if ttt[0][0] == 'O' and ttt[1][1] == 'O' and ttt[2][2] == 'O':
            compwon = True
        if ttt[2][0] == 'O' and ttt[1][1] == 'O' and ttt[0][2] == 'O':
            compwon = True
        if ttt[0][0] == 'O' and ttt[1][0] == 'O' and ttt[2][0] == 'O':
            compwon = True
        if ttt[0][1] == 'O' and ttt[1][1] == 'O' and ttt[2][1] == 'O':
            compwon = True
        if ttt[0][2] == 'O' and ttt[1][2] == 'O' and ttt[2][2] == 'O':
            compwon = True

        if compwon:
            for i in range(3):
                print("| ", end = "")
                for j in range(3):
                    print( ttt[i][j], end=' | ' )
                print()
            break

        # Print after computer moves
        print()
        for i in range(3):
            print("| ", end = "")
            for j in range(3):
                print( ttt[i][j], end=' | ' )
            print()


        # Player move
        choice = 0
        while not (choice >= 1 and choice <= 9):
            try:
                choice = int( input("Enter number: ") )
                while choice < 1 or choice > 9:
                    print("Invalid")
                    choice = int( input("Enter number: ") )
            except Exception:
                print("Not an accepted value. Try again.")

        found = False
        count = 0
        while found != True:
            for i in range(3):
                for j in range(3):
                    count += 1
                    if choice > count:
                        continue
                    if choice == ttt[i][j]:
                        ttt[i][j] = 'X'
                        found = True
                        break
                    else:
                        print("Spot " + str(choice) + " taken. Choosing again.")
                        choice = int( input("Enter number: ") )
                        while choice < 1 or choice > 9:
                            print("Invalid")
                            choice = int( input("Enter number: ") )
                        count = 0
                        break
                if found:
                    break

        # Check for player win
        if ttt[0][0] == 'X' and ttt[0][1] == 'X' and ttt[0][2] == 'X':
            pwon = True
        if ttt[1][0] == 'X' and ttt[1][1] == 'X' and ttt[1][2] == 'X':
            pwon = True
        if ttt[2][0] == 'X' and ttt[2][1] == 'X' and ttt[2][2] == 'X':
            pwon = True
        if ttt[0][0] == 'X' and ttt[1][1] == 'X' and ttt[2][2] == 'X':
            pwon = True
        if ttt[2][0] == 'X' and ttt[1][1] == 'X' and ttt[0][2] == 'X':
            pwon = True
        if ttt[0][0] == 'X' and ttt[1][0] == 'X' and ttt[2][0] == 'X':
            pwon = True
        if ttt[0][1] == 'X' and ttt[1][1] == 'X' and ttt[2][1] == 'X':
            pwon = True
        if ttt[0][2] == 'X' and ttt[1][2] == 'X' and ttt[2][2] == 'X':
            pwon = True

        if pwon:
            for i in range(3):
                print("| ", end = "")
                for j in range(3):
                    print( ttt[i][j], end=' | ' )
                print()
            break

        # Print board after each round
        for i in range(3):
            print("| ", end = "")
            for j in range(3):
                print( ttt[i][j], end=' | ' )
            print()

    if compwon:
        print("The computer won! Better luck next time!")
    if pwon:
        print("You won! Hooray!")

main()