# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project simulates a simple content-based music recommendation system. It compares the features of each song, such as genre, mood, energy, tempo, valence, danceability, and acousticness, with a user's taste profile. Each song receives a weighted score based on how closely it matches the user's preferences, and the songs with the highest scores are recommended.

---

## How The System Works

Explain your design in plain language.

My music recommender uses a content-based approach, meaning it recommends songs by comparing each song's features to a user's taste profile rather than comparing the user to other listeners. While platforms like Spotify and YouTube Music combine collaborative filtering with content-based filtering, my recommender focuses only on song features such as genre, mood, energy, tempo, valence, danceability, and acousticness.

Some prompts to answer:
- What features does each `Song` use in your system
Each `Song` stores information like its title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

- For example: genre, mood, energy, tempo
- What information does your `UserProfile` store 
The `UserProfile` stores the user's preferred genre, mood, and target values for the numerical features.

- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

### Algorithm Recipe

Each song is scored out of 100 points based on how well it matches the user's preferences.

- Genre match: **25 points**
- Mood match: **20 points**
- Energy similarity: **up to 15 points**
- Danceability similarity: **up to 15 points**
- Valence similarity: **up to 10 points**
- Tempo similarity: **up to 10 points**
- Acousticness similarity: **up to 5 points**

Genre and mood earn full points when they match. The numerical features earn more points the closer they are to the user's preferred values. Once every song is scored, the recommender ranks them from highest to lowest and recommends the top matches.

### Data Flow

**Input:** User preferences and songs from `songs.csv`

**Process:** Compare each song to the user's preferences and calculate a weighted score.

**Output:** Rank the songs by score and recommend the best matches.

### Potential Bias

This recommender puts the most weight on genre and mood, so it may recommend similar types of songs over and over. Because the dataset is small, it also has limited variety and may miss songs that fit the user's taste in other ways.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Top recommendations:

1. Sunrise City by Neon Echo
   Score: 5.46
   Because: genre match (+2.0), mood match (+1.5), energy similarity (+1.96)

2. Rooftop Lights by Indigo Parade
   Score: 4.42
   Because: related genre (+1.0), mood match (+1.5), energy similarity (+1.92)

3. Gym Hero by Max Pulse
   Score: 3.74
   Because: genre match (+2.0), energy similarity (+1.74)

4. Concrete Dreams by Blocktown
   Score: 1.98
   Because: energy similarity (+1.98)

5. Night Drive Loop by Neon Echo
   Score: 1.90
   Because: energy similarity (+1.90)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



