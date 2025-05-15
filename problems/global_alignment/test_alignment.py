import unittest
from main import GlobalAlignment


class TestGlobalAlignment(unittest.TestCase):
    def example_alignment_score(self):
        seq1 = "PLEASANTLY"
        seq2 = "MEANLY"
        aligner = GlobalAlignment(seq1, seq2)
        score = aligner.score_matrix()

        expected_score = 8
        self.assertEqual(score, expected_score)


if __name__ == "__main__":
    unittest.main()
