from pathlib import Path
import tempfile

class SimulationSandbox:
    """Creates harmless synthetic files inside a temporary directory."""

    def __init__(self):
        self.root = Path(tempfile.gettempdir()) / "ransomware_detection_simulator"
        self.root.mkdir(parents=True, exist_ok=True)

    def reset(self, count: int = 20):
        self.clear()
        for index in range(1, count + 1):
            path = self.root / f"sample_document_{index:02d}.txt"
            path.write_text(
                f"SAFE SIMULATION FILE {index}\n"
                "This file contains no sensitive data.\n",
                encoding="utf-8",
            )

    def clear(self):
        if not self.root.exists():
            return

        for path in self.root.iterdir():
            if path.is_file():
                path.unlink(missing_ok=True)

    def files(self):
        return sorted(self.root.glob("*.txt"))
