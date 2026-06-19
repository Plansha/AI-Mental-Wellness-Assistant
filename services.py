from models import SymptomEntry, MoodEntry
from datetime import datetime
from typing import List


# ==========================
# EXISTING SYMPTOM SERVICE
# ==========================

class SymptomService:

    @staticmethod
    def create_entry(
        symptom: str,
        severity: int,
        duration: int,
        triggers: List[str],
        notes: str,
        timestamp=None
    ):
        return SymptomEntry(
            timestamp=timestamp or datetime.now(),
            symptom=symptom,
            severity=severity,
            duration_minutes=duration,
            triggers=triggers,
            notes=notes
        )

    @staticmethod
    def validate_entry(entry: SymptomEntry) -> bool:
        return (
            1 <= entry.severity <= 10
            and entry.duration_minutes > 0
            and entry.symptom.strip() != ""
        )


# ==========================
# NEW MOOD SERVICE
# ==========================

class MoodService:

    @staticmethod
    def create_mood_entry(
        mood: str,
        stress_level: int,
        trigger: str,
        journal_entry: str,
        sentiment: str,
        timestamp=None
    ):
        return MoodEntry(
            timestamp=timestamp or datetime.now(),
            mood=mood,
            stress_level=stress_level,
            trigger=trigger,
            journal_entry=journal_entry,
            sentiment=sentiment
        )

    @staticmethod
    def validate_mood_entry(entry: MoodEntry) -> bool:
        return (
            entry.mood.strip() != ""
            and 1 <= entry.stress_level <= 10
        )