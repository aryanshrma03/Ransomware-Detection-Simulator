import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from simulator.sandbox import SimulationSandbox


class SandboxTests(unittest.TestCase):

    def test_sandbox_creates_only_synthetic_files(self):
        sandbox = SimulationSandbox()
        sandbox.reset(count=5)

        files = sandbox.files()

        self.assertEqual(len(files), 5)
        for path in files:
            self.assertTrue(path.name.startswith("sample_document_"))
            self.assertEqual(path.suffix, ".txt")

        sandbox.clear()

    def test_reset_recreates_requested_count(self):
        sandbox = SimulationSandbox()
        sandbox.reset(count=3)
        self.assertEqual(len(sandbox.files()), 3)
        sandbox.clear()


if __name__ == "__main__":
    unittest.main()
