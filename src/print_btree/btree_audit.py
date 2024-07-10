def rid_pipes(
    top: str, 
    bottom: str
) -> str:
    """
    removes unneccesary pipes
        - change bottom according to top

    inputs:
        '|  |  |  |  |  |  |  |'    # bottom
        '   9           8     7'    # top

    returns:
        '   |           |     |'
    """
    out = ''
    for t,b in zip(top, bottom):
        if t == ' ': out += ' '
        else: out += b
    return out

def rid_underscores(
    top: str,
    bottom: str
) -> str:
    """
    removes unnecessary underscores
        - change bottom according to top

    inputs:
        ' _4__  _ __  _6__  _7__'   # bottom
        '    |           |     |'   # top

    returns:
        '  4__         6__   7__'
    """
    out = bottom
    l = r = -1
    bottom += ' '
    for i, ch in enumerate(bottom):
        if ch == '_':
            if l < 0: l = i
            r = i

        else:
            # if l >= 0:
            #     if '4' in bottom:
            #         print(l,r,[bottom[l:r+1], top[l:r+1]])

            if l >= 0 and ('|' not in top[l:r+1]):
                out = out[:l] + ' '*(r-l+1) + out[r+1:]
            l = r = -1
    return out

def remove_front_spaces(
    rows: list[str]
) -> list[str]:
    """
    remove common whitespace at the front

    input:
        [
            '     aa',
            '       aa',
            '      aa',
        ]
    
    output:
        [
            'aa',
            '  aa',
            ' aa',
        ]
    """
    smallest = float('inf')
    for row in rows:
        num_spaces = len(row) - len(row.lstrip())
        if num_spaces < smallest:
            smallest = num_spaces
    for i, row in enumerate(rows):
        rows[i] = row[smallest:]
    return rows


def audit(
    rows: list[str]
) -> list[str]:
    """
    removes empty nodes + tidies up strings
    """
    rows[0] = rows[0].replace('?', ' ')
    for i in range(len(rows)-1):
        # change bottom based on top
        top = rows[i]
        bottom = rows[i+1]
        
        if i%2 == 1:
            # top contains pipes, bottom contains values
            bottom = bottom.replace('?', ' ')
            rows[i+1] = rid_underscores(top, bottom)
        else:
            # bottom contains pipes, top contains values:=
            rows[i+1] = rid_pipes(top, bottom)

    rows = remove_front_spaces(rows)
    return rows
