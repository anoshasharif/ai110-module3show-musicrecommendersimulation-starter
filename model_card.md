# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The recommender compares each song's features with the user's preferences. It checks whether the genre and mood match and then compares how close the song's energy level is to the user's preferred energy. Songs that match more of the user's preferences receive higher scores. After every song is scored, the recommender ranks them from highest to lowest and returns the top recommendations along with explanations. Compared to the starter code, I implemented the scoring system, ranking logic, explanations, and CSV loading.


---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset contains **15 songs** stored in `songs.csv`. The songs include genres such as pop, rock, lofi, jazz, EDM, ambient, folk, blues, hip hop, synthwave, and electronic. They also include different moods such as happy, chill, intense, relaxed, focused, energetic, melancholy, and euphoric. I added additional songs to expand the dataset, but it is still small and does not include features like lyrics, listening history, artist popularity, or user ratings.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The recommender works well when a user's preferences closely match songs in the dataset. For example, the High-Energy Pop profile correctly recommended **Sunrise City**, the Chill Lofi profile recommended **Library Rain**, and the Deep Intense Rock profile recommended **Storm Runner**. The scoring system also explains why each song was recommended, making the results easy to understand.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  
- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I discovered is that the recommender relies heavily on genre, mood, and energy while ignoring other important factors such as favorite artists, lyrics, and listening history. Because the dataset only contains 15 songs, some genres and moods have very few choices, which can cause the same songs to appear repeatedly. During my weight-shift experiment, increasing the importance of energy caused songs with similar energy levels to rank highly even when they did not match the user's preferred genre or mood. This shows that the scoring system can create a small filter bubble by repeatedly recommending songs that share the most heavily weighted features.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

   The recommendations mostly matched my expectations. High-Energy Pop favored Sunrise City, Chill Lofi favored Library Rain, and Deep Intense Rock favored Storm Runner because they matched the user's preferences. The Conflicting Sad Energy profile showed that genre and mood can outweigh energy, and songs with similar energy can still rank highly even if other features don't match.

   After reducing the genre weight and doubling the energy weight, songs with similar energy ranked higher even when their genre or mood did not match. The top songs mostly stayed the same, but energy had a much stronger influence on the results. This made the recommendations different, but not always more accurate.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

If I continued this project, I would:
- Add more songs, genres, and moods to improve recommendation variety.
- Include additional features such as tempo, danceability, valence, favorite artists, and listening history.
- Improve the explanations by showing a detailed breakdown of how each song earned its score.
- Add diversity to the recommendations so similar songs do not always appear together.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

This project helped me understand how recommendation systems compare user preferences with item features to generate personalized suggestions. I was surprised that a relatively simple scoring algorithm could still produce recommendations that felt reasonable. AI tools were helpful for brainstorming ideas, debugging code, and explaining concepts, but I still had to test everything myself to make sure it worked correctly. If I continued this project, I would build a larger dataset and experiment with more advanced recommendation techniques.

