from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class FileEvent:
    timestamp: datetime
    action: str
    filename: str
    old_extension: str = ""
    new_extension: str = ""
    simulated: bool = True

    @property
    def extension_changed(self) -> bool:
        return bool(self.old_extension and self.new_extension and
                    self.old_extension.lower() != self.new_extension.lower())

    @property
    def encryption_like(self) -> bool:
        return self.action.lower() == "encryption_simulated"
