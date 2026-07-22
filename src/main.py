"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

# Edge case / adversarial profiles to probe how the scoring formula behaves
# outside the typical case.
EDGE_CASE_PROFILES = [
    (
        "Unknown genre & mood (no categorical match in catalog)",
        {
            "favorite_genre": "opera",
            "favorite_mood": "furious",
            "target_energy": 0.5,
            "likes_acoustic": False,
        },
    ),
    (
        "Boundary target_energy (max = 1.0)",
        {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 1.0,
            "likes_acoustic": False,
        },
    ),
    (
        "Out-of-range target_energy (negative, outside valid [0, 1])",
        {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": -0.5,
            "likes_acoustic": True,
        },
    ),
]


def print_report(label: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print(label)
    print("=" * 40)
    print("User Profile")
    print(f"  Favorite genre : {user_prefs['favorite_genre']}")
    print(f"  Favorite mood  : {user_prefs['favorite_mood']}")
    print(f"  Target energy  : {user_prefs['target_energy']}")
    print(f"  Likes acoustic : {user_prefs['likes_acoustic']}")

    print("\nTop Recommendations")
    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print(
            f"  {rank}. {song['title']} by {song['artist']} "
            f"[{song['genre']} / {song['mood']}]  (score: {score:.2f})"
        )
        print(f"     Because: {reasons}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    for label, user_prefs in EDGE_CASE_PROFILES:
        print_report(label, user_prefs, songs)


if __name__ == "__main__":
    main()
