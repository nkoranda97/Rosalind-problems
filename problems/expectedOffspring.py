from tkinter.filedialog import askopenfilename

def expectedOffspring(nums):
    return sum([a*b for a,b in zip(nums,[2,2,2,1.5,1,0])])
    

if __name__ == "__main__":
    with open(askopenfilename(),'r') as f:
        print(expectedOffspring([int(i) for i in f.read().split()]))