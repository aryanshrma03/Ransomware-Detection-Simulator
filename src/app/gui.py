import customtkinter as ctk

from components.controls import create_controls
from components.event_log import EventLog
from components.header import create_header
from components.risk_meter import RiskMeter
from config.theme import load_theme
from detector.engine import RansomwareDetector
from simulator.sandbox import SimulationSandbox
from simulator.scenarios import normal_scenario, suspicious_scenario

load_theme()

class RansomwareDetectionApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Ransomware Detection Simulator")
        self.root.geometry("950x760")
        self.root.minsize(820, 680)

        self.sandbox = SimulationSandbox()
        self.detector = RansomwareDetector()

        create_header(self.root)
        self.risk_meter = RiskMeter(self.root)

        create_controls(
            self.root,
            self.simulate_normal,
            self.simulate_suspicious,
            self.reset,
        )

        self.event_log = EventLog(self.root)

        self.stats = ctk.CTkLabel(
            self.root,
            text="Events: 0   |   Encryption-like: 0   |   Extension changes: 0",
            text_color="#9aa4b2",
            font=("Segoe UI", 11),
        )
        self.stats.pack(anchor="w", padx=30, pady=(3, 5))

        ctk.CTkLabel(
            self.root,
            text="⚠ Simulation only. Activity is represented as metadata and never encrypts real files.",
            text_color="#9aa4b2",
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=30, pady=(0, 18))

        self.reset()

    def reset(self):
        self.sandbox.reset()
        self.detector.reset()
        self.event_log.clear()

        result = self.detector.evaluate()
        self.risk_meter.update(result)
        self._update_stats(result)

        self.event_log.add(
            f"[SANDBOX] Safe workspace initialized: {self.sandbox.root}"
        )

    def simulate_normal(self):
        self.detector.reset()
        self.event_log.clear()

        events = normal_scenario(self.sandbox.files())

        for event in events:
            result = self.detector.add_event(event)
            self.event_log.add(
                f"[NORMAL] {event.action.upper():8} {event.filename}"
            )

        self.risk_meter.update(result)
        self._update_stats(result)

    def simulate_suspicious(self):
        self.detector.reset()
        self.event_log.clear()

        events = suspicious_scenario(self.sandbox.files())

        for event in events:
            result = self.detector.add_event(event)
            self.event_log.add(
                f"[SIMULATED] {event.action.upper():20} "
                f"{event.filename}  ({event.old_extension} → {event.new_extension})"
            )

        self.risk_meter.update(result)
        self._update_stats(result)

        self.event_log.add("")
        self.event_log.add("[ALERT] Behavioral ransomware pattern detected.")
        for reason in result.reasons:
            self.event_log.add(f"  • {reason}")

    def _update_stats(self, result):
        self.stats.configure(
            text=(
                f"Events: {result.event_count}   |   "
                f"Encryption-like: {result.encryption_like_events}   |   "
                f"Extension changes: {result.extension_changes}"
            )
        )

    def run(self):
        self.root.mainloop()
