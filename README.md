# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Real-world recommendation utilizes weights (either stored as numbers or data points) and existing user data to determine a song recommendation. This is done by running user preferences and the aspects of a given song into an algorithm for a recommendation score.

In this project, we will use the following algorithm to determine a score that the receommendor will suggest songs by:

score = (
    2.0 * (song.genre == user.favorite_genre) +
    1.5 * (song.mood == user.favorite_mood) +
    1.0 * (1 - abs(song.energy - user.target_energy))
)
- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

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
User Profile
========================================
Favorite genre : jazz
Favorite mood  : melancholic
Target energy  : 0.61
Likes acoustic : True

Top Recommendations
========================================
1. Coffee Shop Stories  (score: 2.76)
   Because: genre matches your favorite (jazz); energy 0.37 is close to your target 0.61

2. Delta Dust  (score: 2.19)
   Because: mood matches your favorite (melancholic); energy 0.30 is close to yourtarget 0.61

3. Sunset Skank  (score: 0.97)
   Because: energy 0.58 is close to your target 0.61

4. Velvet Static  (score: 0.94)
   Because: energy 0.55 is close to your target 0.61

5. Isla Nocturna  (score: 0.93)
   Because: energy 0.68 is close to your target 0.61
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

```
Unknown genre & mood (no categorical match in catalog)
========================================
User Profile
  Favorite genre : opera
  Favorite mood  : furious
  Target energy  : 0.5
  Likes acoustic : False

Top Recommendations
  1. Tokyo Daydream  (score: 1.00)
     Because: energy 0.50 is close to your target 0.50
  2. Harvest Porch  (score: 0.95)
     Because: energy 0.45 is close to your target 0.50
  3. Velvet Static  (score: 0.95)
     Because: energy 0.55 is close to your target 0.50
  4. Sunset Skank  (score: 0.92)
     Because: energy 0.58 is close to your target 0.50
  5. Midnight Coding  (score: 0.92)
     Because: energy 0.42 is close to your target 0.50

Boundary target_energy (max = 1.0)
========================================
User Profile
  Favorite genre : rock
  Favorite mood  : intense
  Target energy  : 1.0
  Likes acoustic : False

Top Recommendations
  1. Storm Runner  (score: 4.41)
     Because: genre matches your favorite (rock); mood matches your favorite (intense); energy 0.91 is close to your target 1.00
  2. Gym Hero  (score: 2.43)
     Because: mood matches your favorite (intense); energy 0.93 is close to your target 1.00
  3. Crimson Fists  (score: 0.97)
     Because: energy 0.97 is close to your target 1.00
  4. Warehouse Pulse  (score: 0.88)
     Because: energy 0.88 is close to your target 1.00
  5. Sunrise City  (score: 0.82)
     Because: energy 0.82 is close to your target 1.00

Out-of-range target_energy (negative, outside valid [0, 1])
========================================
User Profile
  Favorite genre : lofi
  Favorite mood  : chill
  Target energy  : -0.5
  Likes acoustic : True

Top Recommendations
  1. Library Rain  (score: 3.65)
     Because: genre matches your favorite (lofi); mood matches your favorite (chill); energy 0.35 is close to your target -0.50
  2. Midnight Coding  (score: 3.58)
     Because: genre matches your favorite (lofi); mood matches your favorite (chill); energy 0.42 is close to your target -0.50
  3. Focus Flow  (score: 2.10)
     Because: genre matches your favorite (lofi); energy 0.40 is close to your target -0.50
  4. Spacewalk Thoughts  (score: 1.72)
     Because: mood matches your favorite (chill); energy 0.28 is close to your target -0.50
  5. Cathedral Echoes  (score: 0.30)
     Because: energy 0.20 is close to your target -0.50
```

As an experiment, I commented out the 1.5 * mood_match term in score_song (src/recommender.py:73) and reran main.py. Rankings shifted in both edge cases that had mood matches:

Boundary energy (rock/intense, target=1.0): Gym Hero dropped from #2 to #3 (4.41→2.91 for Storm Runner losing the mood bonus knocked it, and Gym Hero lost its 1.5 mood boost, falling behind Crimson Fists which never had mood).

Negative energy (lofi/chill): Midnight Coding dropped from #2 to #3, and Spacewalk Thoughts fell from #4 to last place — both had relied on the mood bonus to outrank songs that only matched on genre or energy.

Net effect: mood-only matches lose their edge entirely, and any song whose ranking depended on stacking a mood match with genre/energy gets pulled down toward songs with fewer matching criteria.

One caveat: the reasons text still says "mood matches your favorite" even though it's no longer scored — the explanation strings weren't updated to reflect the disabled term, so they're now slightly misleading. Want me to fix that, or leave the mood check commented out as-is for this experiment?
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



## Probable Algorithm

score = (
    2.0 * (song.genre == user.favorite_genre) +
    1.5 * (song.mood == user.favorite_mood) +
    1.0 * (1 - abs(song.energy - user.target_energy))
)