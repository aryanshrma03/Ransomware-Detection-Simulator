from datetime import datetime, timedelta

from detector.events import FileEvent

def normal_scenario(filenames):
    base = datetime.now()
    events = []

    for index, filename in enumerate(filenames[:6]):
        events.append(
            FileEvent(
                timestamp=base + timedelta(seconds=index * 3),
                action="read",
                filename=filename.name,
            )
        )

    return events

def suspicious_scenario(filenames):
    base = datetime.now()
    events = []

    # Metadata-only simulation. No file contents are encrypted or changed.
    for index, filename in enumerate(filenames[:16]):
        events.append(
            FileEvent(
                timestamp=base + timedelta(milliseconds=index * 250),
                action="encryption_simulated",
                filename=filename.name,
                old_extension=".txt",
                new_extension=".locked",
            )
        )

    return events
