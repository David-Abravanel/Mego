def Display(display_word,loc):
    print('\n the name is : ',end = '')
    for _ in display_word:
        print(_,end = '')
    print()
    for _ in hengman[loc]:
        print(_)

def User():
    inword = input('\n Enter a name to play with: ')
    display_word = [' _ ']*len(inword)
    loc = 0
    Display(display_word,loc)
    while loc < 7:
        t = 0
        inleter = input(' Enter a leter : ')
        for j in range(len(inword)):
            if inleter == inword[j]:
                display_word[j] = F' {inleter} '
                t = 1
        if t == 0:
            loc += 1
        Display(display_word,loc)
        if ' _ ' not in display_word:
            print('\n  >>  you sve!  (: \n')
            return
    print('\n  >>  you henge ): \n')
    
hengman = [ ['_____\n|\n|\n|\n|\n|____\n'],
            ['_____\n|   |\n|\n|\n|\n|____\n'],
            ['_____\n|   |\n|   o\n|\n|\n|____\n'],
            ['_____\n|   |\n|   o\n|  /\n|\n|____\n'],
            ['_____\n|   |\n|   o\n|  / \\\n|\n|____\n'],
            ['_____\n|   |\n|   o\n|  /|\\\n|\n|____\n'],
            ['_____\n|   |\n|   o\n|  /|\\\n|  /\n|____\n'],
            ['_____\n|   |\n|   o\n|  /|\\\n|  / \\\n|____\n']]
User()