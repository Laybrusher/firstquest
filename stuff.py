class StapleError(Exception):
    def __init__(self, staple, err):
        reason = '%s%s:<<%s>>:%s'
        staple.line = staple.line.replace('\n', '\\n')
        self.reason = reason % (err, staple.idx_line, staple.line, staple.idx_char)
 
    def __str__(self):
        return self.reason
 
 
class Staple:
    def __init__(self, idx_line, line, idx_char):
        self.idx_line = idx_line
        self.line = line
        self.idx_char = idx_char
 
 
def check(filename):
    dstaple = {'(':[], '[':[], '{':[]}
    dstaple_close = {')':'(', ']':'[', '}':'{'}
    
    with open(filename) as f:
        for idx_line, line in enumerate(f, start=1):
            for idx_char, char in enumerate(line, start=1):
                if char in dstaple:
                    dstaple[char].append(Staple(idx_line=idx_line, line=line, idx_char=idx_char))
                elif char in dstaple_close:
                    try:
                        dstaple[dstaple_close[char]].pop()
                    except IndexError:
                        raise StapleError(Staple(idx_line=idx_line, line=line, idx_char=idx_char), 'Error staple close in: ')
    
    for _, l in dstaple.items():
        for staple in l:
            raise StapleError(staple, 'Error staple open in: ')
 
    print('Check is done. File is correct')
 
 
check('file.txt')
