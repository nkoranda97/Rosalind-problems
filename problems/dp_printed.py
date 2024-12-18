from tkinter.filedialog import askopenfilename
from operator import gt, lt

def longest_subsequence(numList, comparison_func, n):
    nums = [[num] for num in numList]

    print("Initial subsequence setup for each element:", nums)

    for i in range(1, n):
        for j in range(i):
            if comparison_func(numList[i], numList[j]) and len(nums[i]) < len(nums[j]) + 1:
                nums[i] = nums[j] + [numList[i]]
                print(f"Updated nums[{i}] to be {nums[i]} because numList[{i}] ({numList[i]}) {'>' if comparison_func == gt else '<'} numList[{j}] ({numList[j]})")

    print("Final subsequence array:", nums)
    longest = max(nums, key=len)
    print("Longest subsequence:", longest)
    return ' '.join(map(str, longest))

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
    print("Testing longest decreasing subsequence:")
    print(longest_subsequence(numList, gt, n))  # For longest decreasing subsequence
    print("\nTesting longest increasing subsequence:")
    print(longest_subsequence(numList, lt, n))  # For longest increasing subsequence
