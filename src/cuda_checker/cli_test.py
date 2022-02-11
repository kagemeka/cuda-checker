import unittest


class Test(unittest.TestCase):
    def test_check(self) -> None:
        import cuda_checker.cli

        cuda_checker.cli.check()


if __name__ == "__main__":
    unittest.main()
