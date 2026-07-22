import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file into a list of dicts."""
    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences, returning (score, reasons)."""
    genre_match = song["genre"] == user_prefs["favorite_genre"]
    mood_match = song["mood"] == user_prefs["favorite_mood"]
    energy_closeness = 1 - abs(song["energy"] - user_prefs["target_energy"])

    score = (
        2.0 * genre_match +
        1.5 * mood_match +
        1.0 * energy_closeness
    )

    reasons = []
    if genre_match:
        reasons.append(f"genre matches your favorite ({song['genre']})")
    if mood_match:
        reasons.append(f"mood matches your favorite ({song['mood']})")
    reasons.append(
        f"energy {song['energy']:.2f} is close to your target {user_prefs['target_energy']:.2f}"
    )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores and ranks songs, returning the top k as (song, score, explanation) tuples."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    scored = [
        (song, score, "; ".join(reasons))
        for song, score, reasons in scored
    ]
    return sorted(scored, key=lambda entry: entry[1], reverse=True)[:k]
