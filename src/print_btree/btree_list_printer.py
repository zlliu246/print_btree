class BTreeSpacingException(Exception):
    """
    to be thrown if not enough spacing when printing btree
    """
    pass

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
    ls: list
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
            val = str(ls[ls_i] or '?').center(r-l+1, '_')

            if val[0] != '_' or val[-1] != '_':
                raise BTreeSpacingException()

            out += val
            ls_i += 1
        else:
            out += ' ' * (r-l-1)
    return out


def generate_display_strings_attempt(
    ls: list[list],
    num_spaces
) -> list[str]:
    """
    inputs:
        ls: 2d list representing btree eg [[1], [2,3], [4,5,6,7]]
        num_spaces: num spaces between values in bottom of tree
    """
    ls = ls[::-1]
    def get_base(base, num_spaces):
        out = ''
        for i,val in enumerate(base):
            out += str(val or '?') + ' '*num_spaces
        return out.strip()

    out = [get_base(ls[0], num_spaces=num_spaces)]
    for row in ls[1:]:
        pipes = get_pipes(out[-1])
        out.append(pipes)

        row = get_row(out[-1], row)
        out.append(row)

    return out


def generate_display_strings(ls: list[list]) -> list[str]:
    """
    keep trying to display btree until BTreeSpacingException is not raised

    inputs:
        ls: 2d list representing btree eg [[1], [2,3], [4,5,6,7]]
    """
    num_spaces = 1
    while True:
        try:
            return generate_display_strings_attempt(ls, num_spaces)
        except BTreeSpacingException as e:
            num_spaces *= 2
        
