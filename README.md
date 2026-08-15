# 🛡️ Ransomware Detection Simulator

A safe, defensive cybersecurity simulation built with **Python** and **CustomTkinter** that demonstrates how a ransomware detection system can monitor filesystem activity and identify suspicious behavior.

> **Safety first:** This project is a simulator. It does **not** encrypt, delete, rename, corrupt, or modify real user files. All simulated activity happens inside an isolated temporary sandbox created by the application.

## 📌 Project Overview

The simulator models a simplified ransomware-detection workflow:

```text
Safe Simulation Workspace
        │
        ▼
Synthetic File Activity
        │
        ├── Normal file activity
        ├── Rapid file modifications
        ├── Suspicious extension changes
        ├── Burst activity
        └── Simulated encryption-like events
                │
                ▼
        Behavioral Detector
                │
                ▼
       Risk Score + Alerts
                │
                ▼
       Security Dashboard
```

The goal is to demonstrate **behavior-based detection**, rather than build ransomware or execute malicious code.

## 🚀 Features

- 🛡️ Safe ransomware-behavior simulation
- 📁 Isolated temporary sandbox
- 🔍 Filesystem event monitoring
- ⚡ Burst-activity detection
- 🔄 Extension-change detection
- 🔐 Simulated encryption-event detection
- 📈 Dynamic 0–100 risk score
- 🚦 Normal / Elevated / High / Critical status
- 🚨 Alert log
- 📊 Behavioral statistics
- 🧪 Normal-activity simulation
- ⚠️ Suspicious-activity simulation
- 🧹 One-click sandbox cleanup
- 🌙 CustomTkinter dashboard
- 🧩 Modular architecture
- 🧪 Unit tests

## 🔒 Safety Design

The simulator intentionally avoids dangerous ransomware functionality.

It **does not**:

- Encrypt real files
- Delete real files
- Modify files outside its temporary sandbox
- Propagate across directories or systems
- Disable security software
- Create persistence
- Execute payloads
- Attempt to bypass security controls

Instead, suspicious events are represented as **metadata-only simulated events**.

The application creates a temporary directory such as:

```text
<system-temp>/ransomware_detection_simulator/
```

and uses harmless synthetic files there.

## 🧠 Detection Model

The detector scores behavioral indicators:

| Indicator | Example | Weight |
|---|---|---:|
| Rapid modification burst | Many events in short period | High |
| Encryption-like event | Simulated mass encryption activity | Critical |
| Suspicious extension change | `.docx → .locked` | Medium |
| High event rate | Unusually dense activity | High |
| Repeated target files | Same files repeatedly touched | Medium |
| Normal activity | Low-rate ordinary operations | None/Low |

The score is capped at **100**.

### Risk Levels

```text
0–24    Normal
25–49   Elevated
50–74   High
75–100  Critical
```

This is a demonstration model, not an enterprise EDR/ransomware detector.

## 📂 Project Structure

```text
Ransomware-Detection-Simulator/
│
├── src/
│   ├── main.py
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   └── gui.py
│   │
│   ├── simulator/
│   │   ├── __init__.py
│   │   ├── sandbox.py
│   │   └── scenarios.py
│   │
│   ├── detector/
│   │   ├── __init__.py
│   │   ├── events.py
│   │   └── engine.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── header.py
│   │   ├── risk_meter.py
│   │   ├── controls.py
│   │   └── event_log.py
│   │
│   └── config/
│       ├── __init__.py
│       └── theme.py
│
├── tests/
│   ├── __init__.py
│   ├── test_detector.py
│   └── test_sandbox.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 📦 Installation

```bash
git clone https://github.com/aryanshrma03/Ransomware-Detection-Simulator.git
cd Ransomware-Detection-Simulator

python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

## ▶️ Run

```bash
python src/main.py
```

## 🧪 Run Tests

```bash
python -m unittest discover -s tests -v
```

## 🎮 Simulation Scenarios

### Normal Activity

Simulates ordinary low-frequency file operations.

Expected result:

```text
Risk: Normal
Score: Low
```

### Suspicious Activity

Generates a burst of simulated events including:

- Rapid modifications
- Multiple encryption-like events
- Suspicious extension changes
- High event frequency

Expected result:

```text
Risk: High / Critical
```

No actual encryption is performed.

## 🔮 Future Improvements

- [ ] Real read-only filesystem telemetry
- [ ] Windows Event Tracing integration
- [ ] ETW-based process telemetry
- [ ] Process-to-file correlation
- [ ] Entropy measurement on copied sample data
- [ ] Explainable detection rules
- [ ] SQLite event history
- [ ] JSON/CSV reports
- [ ] Detection-rule configuration
- [ ] ROC/precision/recall evaluation
- [ ] ML-based behavioral classifier
- [ ] Alert severity tuning
- [ ] SOC-style incident timeline

## ⚠️ Limitations

Real ransomware detection requires much richer telemetry and context.

Legitimate applications such as backup tools, archive utilities, software updaters, and file synchronization programs can generate high-volume file activity and may resemble ransomware behavior.

Therefore, production systems need:

- Process context
- User context
- File reputation
- Baseline behavior
- Historical activity
- Network telemetry
- Multiple detection signals

## 👨‍💻 Author

**Aryan Sharma**

Cybersecurity-focused Python project demonstrating safe ransomware-behavior simulation and defensive behavioral detection.
