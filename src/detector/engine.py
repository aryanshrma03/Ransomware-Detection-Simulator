from collections import Counter, deque
from dataclasses import dataclass
from datetime import datetime, timedelta

from detector.events import FileEvent

@dataclass
class DetectionResult:
    score: int
    level: str
    reasons: list[str]
    event_count: int
    encryption_like_events: int
    extension_changes: int
    burst_events: int

class RansomwareDetector:
    """Simple explainable behavioral scoring engine for simulation."""

    def __init__(self, window_seconds: int = 10):
        self.window_seconds = window_seconds
        self.events = deque(maxlen=1000)

    def reset(self):
        self.events.clear()

    def add_event(self, event: FileEvent) -> DetectionResult:
        self.events.append(event)
        return self.evaluate()

    def evaluate(self) -> DetectionResult:
        if not self.events:
            return DetectionResult(0, "Normal", [], 0, 0, 0, 0)

        now = self.events[-1].timestamp
        cutoff = now - timedelta(seconds=self.window_seconds)
        recent = [event for event in self.events if event.timestamp >= cutoff]

        encryption_count = sum(event.encryption_like for event in recent)
        extension_changes = sum(event.extension_changed for event in recent)

        burst_events = len(recent)
        score = 0
        reasons = []

        if encryption_count >= 3:
            score += 60
            reasons.append("Multiple encryption-like events detected.")
        elif encryption_count:
            score += 25
            reasons.append("Encryption-like file activity detected.")

        if extension_changes >= 5:
            score += 25
            reasons.append("Multiple file-extension changes detected.")
        elif extension_changes:
            score += 8
            reasons.append("A suspicious file-extension change was observed.")

        if burst_events >= 20:
            score += 30
            reasons.append("Very high file-event rate detected.")
        elif burst_events >= 10:
            score += 18
            reasons.append("Elevated file-event rate detected.")
        elif burst_events >= 5:
            score += 5

        target_counts = Counter(event.filename for event in recent)
        if any(count >= 3 for count in target_counts.values()):
            score += 10
            reasons.append("Repeated activity against the same target was observed.")

        score = min(100, score)

        if score >= 75:
            level = "Critical"
        elif score >= 50:
            level = "High"
        elif score >= 25:
            level = "Elevated"
        else:
            level = "Normal"

        return DetectionResult(
            score=score,
            level=level,
            reasons=reasons,
            event_count=len(recent),
            encryption_like_events=encryption_count,
            extension_changes=extension_changes,
            burst_events=burst_events,
        )
