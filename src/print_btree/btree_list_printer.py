def get_pipes(string: str) -> str:
    '''
    given a row, get pipes at correct positions

    'apple      orange         pear        pineapple'
                        to
    '  |          |             |              |'
    '''
    out = ''
    current = ''
    for c in string:
        if c == ' ': 
            if current: 
                out += '|'.center(len(current))
                current = ''
            out += ' '
        else:
            current += c
    if current: 
        out += '|'.center(len(current))
    return out.rstrip()

def get_row(
    string: str, 
    ls: list,
    none_val = '?'
) -> str:
    '''
    inputs:
        string: string of pipes
        ls: list of values to insert

    given inputs, return next row

    '  |    |    |      |    |      |     |    |'
                        to
    '  __a___    ___b____    ___c____     __d___'   
    '''
    indexes = []
    for i,c in enumerate(string):
        if c == '|': indexes.append(i)
    out = ' ' * indexes[0]
    ls_i = 0
    for i in range(len(indexes)-1):
        l = indexes[i]
        r = indexes[i+1]
        if i % 2 == 0:
            out += str(ls[ls_i] or none_val).center(r-l+1, '_')
            ls_i += 1
        else:
            out += ' ' * (r-l-1)
    return out


def display(
    ls: list[list],
    none_val: str = '?'
) -> None:
    """
    inputs:
        ls: 2d list representing btree eg [[1], [2,3], [4,5,6,7]]
        none_val: character we print if a value is None
    """
    ls = ls[::-1]
    def get_base(base):
        out = ''
        for i,val in enumerate(base):
            out += str(val or none_val) + '  '
        return out.strip()

    out = [get_base(ls[0])]
    for row in ls[1:]:
        pipes = get_pipes(out[-1])
        out.append(pipes)

        row = get_row(out[-1], row, none_val=none_val)
        out.append(row)

    print()
    for row in out[::-1]:
        print(row)
    print()
