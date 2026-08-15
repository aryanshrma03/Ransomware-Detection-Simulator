import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from detector.engine import RansomwareDetector
from detector.events import FileEvent


class DetectorTests(unittest.TestCase):

    def test_empty_detector_is_normal(self):
        result = RansomwareDetector().evaluate()
        self.assertEqual(result.score, 0)
        self.assertEqual(result.level, "Normal")

    def test_normal_events_remain_low_risk(self):
        detector = RansomwareDetector()
        now = datetime.now()

        for index in range(3):
            result = detector.add_event(
                FileEvent(
                    timestamp=now + timedelta(seconds=index * 3),
                    action="read",
                    filename=f"file{index}.txt",
                )
            )

        self.assertLess(result.score, 25)

    def test_suspicious_burst_becomes_critical(self):
        detector = RansomwareDetector()
        now = datetime.now()

        for index in range(16):
            result = detector.add_event(
                FileEvent(
                    timestamp=now + timedelta(milliseconds=index * 100),
                    action="encryption_simulated",
                    filename=f"file{index}.txt",
                    old_extension=".txt",
                    new_extension=".locked",
                )
            )

        self.assertGreaterEqual(result.score, 75)
        self.assertEqual(result.level, "Critical")
        self.assertGreater(result.encryption_like_events, 0)

    def test_score_is_capped(self):
        detector = RansomwareDetector()
        now = datetime.now()

        for index in range(100):
            result = detector.add_event(
                FileEvent(
                    timestamp=now,
                    action="encryption_simulated",
                    filename=f"file{index}.txt",
                    old_extension=".txt",
                    new_extension=".locked",
                )
            )

        self.assertLessEqual(result.score, 100)


if __name__ == "__main__":
    unittest.main()
