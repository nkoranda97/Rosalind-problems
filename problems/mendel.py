from tkinter.filedialog import askopenfilename


def mendel_prop(k, m, n):
    k = int(k)
    m = int(m)
    n = int(n)
    p = k + m + n
    kk = (k / p * (k - 1) / (p - 1)) * 1
    mm = (m / p * (m - 1) / (p - 1)) * 0.75
    km = 2 * (k / p * m / (p - 1))
    kn = 2 * (k / p * n / (p - 1))
    mn = (2 * (m / p * n / (p - 1))) * 0.5
    return kk + mm + km + kn + mn


if __name__ == "__main__":
    filename = askopenfilename()
    with open(filename) as f:
        k, m, n = f.read().split()
        print(mendel_prop(k, m, n))
