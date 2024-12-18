from tkinter.filedialog import askopenfilename
from operator import gt, lt

def longest_subsequence(numList, comparison_func,n):
    nums = [[num] for num in numList]
    for i in range(1, n):
        for j in range(i):
            if comparison_func(numList[i], numList[j]) and len(nums[i]) < len(nums[j]) + 1:
                nums[i] = nums[j] + [numList[i]]
    print(nums)
    return ' '.join(map(str, max(nums, key=len)))

if __name__ == "__main__":
    '''
    # to read from file:
    with open (askopenfilename()) as f:
        n = int(f.readline())
        numList = f.readline().split(" ")
        numList = [int(i.replace('\n','')) for i in numList]
    '''
    n = 5
    numList = [5,1,4,2,3]
    print(longest_subsequence(numList, gt, n))  # For longest decreasing subsequence
    print(longest_subsequence(numList, lt, n))  # For longest increasing subsequence
