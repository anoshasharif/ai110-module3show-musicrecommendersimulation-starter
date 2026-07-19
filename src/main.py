"""
Command line runner for the Music Recommender Simulation.
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    print(f"Loaded songs: {len(songs)}")

    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")

    for position, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec

        print(f"{position}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
