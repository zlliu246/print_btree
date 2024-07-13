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

def remove_redundant_chars(
    rows: list[str]
) -> list[str]:
    """
    removes redundant undescores in middle of binary tree
    to prevent tree from being too wide

    
                          __________________________________1__________________________________                             
                          |                                                                   |                             
         _________________2_________________                                                  3__________________           
         |                                 |                                                                    |           
         4                             pineapple                                                         appleorangepear__  
                                                                                                                         |  
                                                                                                                        100 

        # becomes

            ______________1___                    
            |                |                    
        ___2_______         3__________          
        |         |                   |          
        4     pineapple        appleorangepear__ 
                                                | 
                                            100

    """
    def keep(column: list[str]):
        for trigram in column:
            if trigram not in ('___', '   '):
                return True
            
        return False
        
    out = ['' for r in rows]
    index = 0
    max_len = len(max(rows, key=len))
    for i in range(len(rows)):
        rows[i] = ' ' + rows[i].ljust(max_len, ' ') + ' '

    for index in range(1, max_len+1):
        column = [row[index-1:index+2] for row in rows]

        if keep(column):
            for i in range(len(out)):
                out[i] += column[i][1]
    # return rows
    return out


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

    rows = remove_redundant_chars(rows)
    return rows
