import numpy as np
from Bio.Align import substitution_matrices


class GlobalAlignment:
    def __init__(self, seq1: str, seq2: str):
        self.BLOSUM62 = substitution_matrices.load("BLOSUM62")
        self.LINEAR_GAP_PENALTY = 5
        self.seq1 = seq1
        self.seq2 = seq2

    def score_matrix(self) -> int:
        matrix = np.zeros([len(self.seq1) + 1, len(self.seq2) + 1], dtype=np.int32)

        for j in range(1, len(self.seq2) + 1):
            matrix[0, j] = -self.LINEAR_GAP_PENALTY * j

        for i in range(1, len(self.seq1) + 1):
            matrix[i, 0] = -self.LINEAR_GAP_PENALTY * i

        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
                diag = (
                    matrix[i - 1, j - 1]
                    + self.BLOSUM62[self.seq1[i - 1], self.seq2[j - 1]]
                )
                up = matrix[i - 1, j] - self.LINEAR_GAP_PENALTY
                left = matrix[i, j - 1] - self.LINEAR_GAP_PENALTY
                matrix[i, j] = max(diag, up, left)

        return matrix[-1, -1]


def main():
    seq1 = """CWCRVYALSYFDQQLYMMPFLEVEKLEWNGCKNSWLHDQFPMLYVCEHVANCIQPQCVNQ
VVPVRTIFKDLEWFQKRTLLQTLTSLMRHKPEYNKSKKAMSRMSSMWKNLIWTMPNTQVM
EHHHRAADGARQKGNQQMEWKWKDRYYDMGQQLQTWHHWNNGWRPFTSHVVYSPSMWEID
AFIMGLAMWTCLAGRGIMKGLGYSVMDQMPCNSRHVWPGISNHFKIMFHVVSMHLPWRAD
SCIACGAVNHRYNVQLMWNNFDDSNSEQSCTGQTDTCVNKECDQEADEYALHFHHAHACV
FAAMCWYNTEFLEPIWDSGKGDERPEPFKACCRWKRNLDGVYNIWHCAHNVTPPTNCWVD
KTPQEGRPPYSIFNCMTYALMLKSDCDWTISGPACEEVRKCAQLNWEFQLYKSGRIPDHC
VSKNSYWMEIAMFIQCPLWFTTLAGAKLPFWTEHLEPFPSETTGSYKVHITGIKALFPGP
GFGMPWDICKEQGLLAQIKCTWPWHDGSGFLASSSKTYITECQAAGTHTCIQCTEDEVLI
NYWEPPCYLNTCPDQSNRRSINKDRSNFGRRELLALILLRAKPPINIVGAVWQGRRPAAC
KDYIDNLRRQVMDWLYEYYCQMLRQTCMGLPYDVFGFGAGYWKYWFGGNQGFLEISPDLD
DDCWAHCYMSIWPWINHTETYIHDDDGNGNWHVEWGGTEPYHNPNVKHIATSQPFGNYMQ
RNVLPIFWIPNVYWFWWATDCFQIPYKATLTFTCEQCYMPSPMVGNYSRIPVAFNCACVP
DLGAGEFGFCFRNVPVGKICDQDANDEIMHFMRDGRNEAQCMTFSPGGWHG"""
    seq2 = """QDHDSHWCRVYALSYFDQQLYEMDPFYHMVRYKLEWNGCKNSWLHDVCLDHQMHHMIHVA
NCIQPQVVNQVDEVWSLMRHKPEYNKTKKKNLIWTMEMFAVMVSTQVMTHHHRAPDGARQ
KGNQQMEWKWKSRYYNNGWRPFTSHVVYSPSMWTSRGCDYSRDQFIMYLNCVAGKGLGYS
VMRQMPCNSRQWVEQADKVWPKCHMRCHTISNMFKIMFHVVSMHLPNPCYMKWHRSAVNH
DYDVQLMWNNFDDSNSEQSCTGQTAGPRVRLHTCVNKNCLLHAHACVFAAKWGMCTGWDR
MNFLEPIWDSGKGDERKAMGIRNLDGSYNIWHCQHNVTPPTNCWVVKDPFECMTYAGMLK
SDPRHAICCMEVRKCAQLNWEFQLWWWHVDDWKSGRIPDHCDGFIQFGSRMPLWPTTLAH
AKLPFWTEHLEPFPSDMTGRWDVWTGSYKVHITGIKALFPCPWDICKEKCTWPWHDGSGF
LVPRTSSSEVFRMGQQACQMHGTDEVLINTCPDQSNRRSINKDRSNFGRRELLACIVMQY
WPNDLRRPAACKDYIDNLRRQVNLCWDFICRDRLYDYYCQMLPYCVFKAYMFGAGYWKKH
CGWFGGNQGFLEQSVDLDDDCWAHCYMSQDPWINHTESMQWYTIHDQKFWCFADGFGNWM
VVHNPNVKHIATSQPTRGPVGVYAQRNVLPIFWIPNVYWFWWATDCFQIPYKATLNAWMS
EDAVDTCEQCIVYMTAKIAESESPYSRRPVAFNCACVKPDLGGRPRSGEMDISNVPVGKS
RDQDYNDNIMHFMRLPNSWGDNEEWQMYMTDTCMTFSMGAWHG"""

    seq1 = seq1.replace("\n", "").replace(" ", "")
    seq2 = seq2.replace("\n", "").replace(" ", "")
    aligner = GlobalAlignment(seq1, seq2)

    print(aligner.score_matrix())


if __name__ == "__main__":
    main()
