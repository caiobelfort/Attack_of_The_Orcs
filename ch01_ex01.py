import random
import textwrap


def wrap_bold(msg: str) -> str:
    return '\033[1m' + msg + '\033[0m'


if __name__ == '__main__':
    keep_playing = 'y'
    occupants = ['enemy', 'friend', 'unoccupied']
    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print('\033[1m' + 'Attack of The Orcs v0.0.01:' + '\033[0m')

    msg = (
        "The war between humans and their arch enemies, Ocrs, was in the offing. "
        "Sir Foo, one of the brave knights guarding the southern plains began a long "
        "journey towards the east through an unknown dense forest. On his way, he spotted "
        "a small isolated settlement. Tired and hoping to replenish his food stock, he "
        "decided to take a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he decided to enter.. "
    )

    print(textwrap.fill(msg, width=width))
    print(wrap_bold('Mission:'))
    print('\tChoose a hut where Sir Foo can rest...')
    print(wrap_bold('TIP:'))
    print('Be careful as there are enemies lurking around!')
    print(dotted_line)

    while keep_playing == 'y':
        huts = []
        # Randomly append 'enemy' or 'friend' or None to the huts list
        while len(huts) < 5:
            computer_choice = random.choice(occupants)
            huts.append(computer_choice)

        # Prompt user to select a hut
        msg = wrap_bold('Choose a hut number to enter (1-5): ')
        user_choice = input('\n ' + msg)
        idx = int(user_choice)

        # Print the occupant info
        print('Revealing the occupants...')
        msg = ''
        for i in range(len(huts)):
            occupant_info = '<%d:%s>' % (i+1, huts[i])
            if i + 1 == idx:
                occupant_info = wrap_bold(occupant_info)
            msg += occupant_info + ' '
        print('\t' + msg)
        print(dotted_line)
        print(wrap_bold('Entering hut %d... ' % idx), end=' ')

        # Determine and announce the winner
        if huts[idx-1] == 'enemy':
            print(wrap_bold('YOU LOSE :( Better luck next time!'))
        else:
            print(wrap_bold('Congratulations! YOU WIN!!!'))
        print(dotted_line)
        keep_playing = input('Play again? Yes(y)/No(n):')