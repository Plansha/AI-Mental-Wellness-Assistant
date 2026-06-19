from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import pandas as pd


# ==========================
# EXISTING SYMPTOM MODEL
# ==========================

@dataclass
class SymptomEntry:
    entry_id: Optional[int] = None
    timestamp: datetime = None
    symptom: str = ""
    severity: int = 5
    duration_minutes: int = 60
    triggers: List[str] = None
    notes: str = ""

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

        if self.triggers is None:
            self.triggers = []

    def to_dict(self):
        return {
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "symptom": self.symptom,
            "severity": self.severity,
            "duration_minutes": self.duration_minutes,
            "triggers": ",".join(self.triggers),
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: dict):
        entry = cls()

        entry.entry_id = data.get("entry_id")
        entry.timestamp = pd.to_datetime(data.get("timestamp"))
        entry.symptom = data.get("symptom", "")
        entry.severity = data.get("severity", 5)
        entry.duration_minutes = data.get("duration_minutes", 60)
        entry.notes = data.get("notes", "")

        entry.triggers = (
            data.get("triggers", "").split(",")
            if data.get("triggers")
            else []
        )

        return entry

    def __repr__(self):
        return (
            f"SymptomEntry("
            f"id={self.entry_id}, "
            f"symptom={self.symptom}, "
            f"severity={self.severity})"
        )


# ==========================
# NEW MOOD MODEL
# ==========================

@dataclass
class MoodEntry:
    entry_id: Optional[int] = None
    timestamp: datetime = None
    mood: str = ""
    stress_level: int = 5
    trigger: str = ""
    journal_entry: str = ""
    sentiment: str = "Neutral"

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "mood": self.mood,
            "stress_level": self.stress_level,
            "trigger": self.trigger,
            "journal_entry": self.journal_entry,
            "sentiment": self.sentiment
        }

    @classmethod
    def from_dict(cls, data: dict):
        entry = cls()

        entry.entry_id = data.get("entry_id")
        entry.timestamp = pd.to_datetime(data.get("timestamp"))
        entry.mood = data.get("mood", "")
        entry.stress_level = data.get("stress_level", 5)
        entry.trigger = data.get("trigger", "")
        entry.journal_entry = data.get("journal_entry", "")
        entry.sentiment = data.get("sentiment", "Neutral")

        return entry

    def __repr__(self):
        return (
            f"MoodEntry("
            f"id={self.entry_id}, "
            f"mood={self.mood}, "
            f"stress_level={self.stress_level}, "
            f"sentiment={self.sentiment})"
        )