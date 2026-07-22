# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Rangefinder 1.0

---

## 2. Intended Use  

This offers song recommendations based upon user profiles and a given dataset (songs.csv)

Users can use main.py to interface with the model card, and will try to predict the top 5 songs based on genre, mood, and energy score. 

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

We take the gnre, energy, and mood of the user profile.

We take these and assign a score to each song based upon the user. 

Genre is weighted the most heavily, with mood, and energy reviewed after. These will be multiplied by the weight in order to have more pleasing songs for a user profile have a higher score. 

These are then sorted via a top 5 songs and provided to the user. 
---

## 4. Data  

Describe the dataset the model uses.  

30 songs are added to the csv file containing a variety of moods and genres. In addition to starter songs, multiple songs were added. While a variety of songs were added, different portions or musical taste are missing. 
---

## 5. Strengths  
The system works well given a strong data set, and overindexes for user fit for similiar genres and moods. In the absence of songs that does not match the user profile's genre or mood, songs that match the users energy works well as a replacement. 
---

## 6. Limitations and Bias 

This model has multiple oversights that require a better dataset or additional work in the recommendation algorithm. 

The biggest flaws appear in the dataset, where certain genres are overrepresented or not found within the dataset.

As an example, classical music would not be recommended at all to a user, and certain genres like lofi has an overabundance of songs to choose from. With a higher weight given to songs in the same genre as a user profile, certain genres will be weighted more heavily, even if the energy or mood does not fit. In addition, there are multiple songs by an artist, which may crowd out other songs that they might like. 

The algorithm also has multiple things to consider that may result in an inaccurate summary. As an example, exact-string matching is used for the recommender, which relies on the user to type the genre exactly. Without it, it will be considered inaccurate. The algorithm also handles ties by whether it is earlier in the dataset, which is a poor way to handle ties in score that should be weighted by other charasterics in the dataset. 

---

## 7. Evaluation  

The following user profiles tested can be seen below:

```
User Profile
  Favorite genre : opera
  Favorite mood  : furious
  Target energy  : 0.5
  Likes acoustic : False

User Profile
  Favorite genre : rock
  Favorite mood  : intense
  Target energy  : 1.0
  Likes acoustic : False

User Profile
  Favorite genre : lofi
  Favorite mood  : chill
  Target energy  : -0.5
  Likes acoustic : True
```

This model worked generally well with no aberrations when songs existed in the dataset that matched a user profile's genre or mood.

As an example, the rock profile had a rock song as top of mind, and had similiar moods for the rest of the results. Multiple songs also had the same energy, and some of the songs differed, which was within expectations. 

The song recommendations that resulted only from song energy  was quite surprising, and pulled from a variety of genres. 

For the comparisons ran, we first looked to see if any of the songs matched the criteria of same genre, same mood, and same energy. This matched our prior expecatations when planning this out. 
---

## 8. Future Work  

I'd like to be able to add fuzzy logic for genres and moods. If a genre is not available, what are similar genres that would work (i.e, classical to jazz to folk)

I'd also like to tighten up what energy means, either by giving a non-numerical portion or having an AI provide additional context via guardrails. 
---

## 9. Personal Reflection  

A few sentences about your experience.  

I learned a lot about recommendation systems, especially how they seemed to handle cases where the genre or mood doesn't nesecarrily match. 

A lot of these systems rely on quality data. While these fields are not nesecarily all that companies review, this is a useful guidepost and is a lot of work to implement. 

AI tools helped me a lot for this project, but I found myself relying on my own opinion when determing the recommendation algorithm and other materials such as the dataset. 