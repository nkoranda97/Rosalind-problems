from tkinter.filedialog import askopenfilename


def hamming_distance(s1, s2):
    return sum([1 for i in range(len(s1)) if s1[i] != s2[i]])


if __name__ == "__main__":
    filename = askopenfilename()
    with open(filename) as f:
        s1, s2 = f.readlines()
        print(hamming_distance(s1, s2))
