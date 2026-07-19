"""
Command line runner for the Music Recommender Simulation.
"""

from .recommender import load_songs, recommend_songs


def print_recommendations(profile_name, user_prefs, songs):
    """Prints the top recommendations for one user profile."""

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n=== {profile_name} ===")
    print(f"Preferences: {user_prefs}\n")

    for position, (song, score, explanation) in enumerate(
        recommendations, start=1
    ):
        print(f"{position}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
        },
        "Conflicting Sad Energy": {
            "genre": "blues",
            "mood": "melancholy",
            "energy": 0.95,
        },
    }

    for profile_name, user_prefs in profiles.items():
        print_recommendations(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
