import unittest
from main import LocalAlignment


class TestGlobalAlignment(unittest.TestCase):
    def test_example_alignment_score(self):
        seq1 = "MEANLYPRTEINSTRING"
        seq2 = "PLEASANTLYEINSTEIN"
        aligner = LocalAlignment(seq1, seq2)
        align1, align2, score = aligner.make_local_alignment()
        expected_align1 = "LYPRTEINSTRIN"
        expected_align2 = "LYEINSTEIN"
        expected_score = 23

        self.assertEqual(align1, expected_align1)
        self.assertEqual(align2, expected_align2)
        self.assertEqual(score, expected_score)


if __name__ == "__main__":
    unittest.main()
