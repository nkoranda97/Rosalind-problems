from tkinter.filedialog import askopenfilename
from math import log10

def stringProb(s, gc_contents):
    results = []
    for gc in gc_contents:
        at = log10((1 - gc) / 2)
        gc = log10(gc / 2)
        
        total_log_odds = round(sum(at if base in 'AT' else gc for base in s),3)
        results.append(total_log_odds)
    
    return ' '.join(map(str,results))
            
def readText():
    filename = askopenfilename()
    with open(filename, 'r') as f:
        s = f.readline().strip()
        gc_contents = map(float, f.readline().strip().split())
        
    return s, gc_contents

if __name__ == '__main__':
    s, gc_contents = readText()
    print(stringProb(s, gc_contents))

    
    
    

