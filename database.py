import sqlite3
import pandas as pd
from typing import List, Optional
from models import SymptomEntry
from datetime import datetime


class SymptomDatabase:
    def __init__(self, db_path: str = "symptoms.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()

            # Existing Symptom Table
            c.execute("""
                CREATE TABLE IF NOT EXISTS symptoms (
                    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    symptom TEXT NOT NULL,
                    severity INTEGER NOT NULL CHECK (severity >= 1 AND severity <= 10),
                    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
                    triggers TEXT,
                    notes TEXT
                )
            """)

            # New Mood Table
            c.execute("""
                CREATE TABLE IF NOT EXISTS moods (
                    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    mood TEXT NOT NULL,
                    stress_level INTEGER NOT NULL CHECK (stress_level >= 1 AND stress_level <= 10),
                    trigger TEXT,
                    journal_entry TEXT,
                    sentiment TEXT
                )
            """)

            conn.commit()

    # ==========================
    # EXISTING SYMPTOM FUNCTIONS
    # ==========================

    def add_symptom(self, entry: SymptomEntry) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                c = conn.cursor()

                data = entry.to_dict()

                c.execute("""
                    INSERT INTO symptoms
                    (
                        timestamp,
                        symptom,
                        severity,
                        duration_minutes,
                        triggers,
                        notes
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    data["timestamp"],
                    data["symptom"],
                    data["severity"],
                    data["duration_minutes"],
                    data["triggers"],
                    data["notes"]
                ))

                conn.commit()

            return True

        except Exception as e:
            print(f"Database error: {e}")
            return False

    def get_all_symptoms(self) -> pd.DataFrame:
        try:
            with sqlite3.connect(self.db_path) as conn:
                df = pd.read_sql_query(
                    "SELECT * FROM symptoms ORDER BY timestamp DESC",
                    conn
                )

                if not df.empty:
                    df["timestamp"] = pd.to_datetime(df["timestamp"])

                return df

        except Exception:
            return pd.DataFrame()

    def get_symptoms_by_date(self, date_str: str) -> pd.DataFrame:
        try:
            with sqlite3.connect(self.db_path) as conn:
                df = pd.read_sql_query(
                    """
                    SELECT *
                    FROM symptoms
                    WHERE date(timestamp) = ?
                    ORDER BY timestamp
                    """,
                    conn,
                    params=(date_str,)
                )

                if not df.empty:
                    df["timestamp"] = pd.to_datetime(df["timestamp"])

                return df

        except Exception:
            return pd.DataFrame()

    # =====================
    # NEW MOOD FUNCTIONS
    # =====================

    def add_mood(
        self,
        mood,
        stress_level,
        trigger,
        journal_entry,
        sentiment,
        timestamp
    ):
        try:
            with sqlite3.connect(self.db_path) as conn:
                c = conn.cursor()

                c.execute("""
                    INSERT INTO moods
                    (
                        timestamp,
                        mood,
                        stress_level,
                        trigger,
                        journal_entry,
                        sentiment
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    timestamp,
                    mood,
                    stress_level,
                    trigger,
                    journal_entry,
                    sentiment
                ))

                conn.commit()

            return True

        except Exception as e:
            print(f"Mood insert error: {e}")
            return False

    def get_all_moods(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                df = pd.read_sql_query(
                    """
                    SELECT *
                    FROM moods
                    ORDER BY timestamp DESC
                    """,
                    conn
                )

                if not df.empty:
                    df["timestamp"] = pd.to_datetime(df["timestamp"])

                return df

        except Exception:
            return pd.DataFrame()

    def delete_mood(self, entry_id):
        try:
            with sqlite3.connect(self.db_path) as conn:
                c = conn.cursor()

                c.execute(
                    "DELETE FROM moods WHERE entry_id = ?",
                    (entry_id,)
                )

                conn.commit()

            return True

        except Exception:
            return False

    # ======================
    # DELETE SYMPTOM ENTRY
    # ======================

    def delete_entry(self, entry_id: int) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                c = conn.cursor()

                c.execute(
                    "DELETE FROM symptoms WHERE entry_id = ?",
                    (entry_id,)
                )

                conn.commit()

            return True

        except Exception:
            return False
