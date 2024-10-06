# Potential Users:
- Anime Newcomers
- Anime Enthusiasts
- Anime Researchers

# CIDER Analysis

## Assumption 1: Users are able to input titles correctly when using the score retrieval feature

### Critique
The app assumes users will always know and input the exact titles of anime correctly, excluding users who may mistype titles for whatever reason such as a disability or are unsure of exact names.

### Imagine
Users who don’t remember the exact title of an anime or who misspell the title would not be able to retrieve the corresponding score -- then they would get frustrated and not be able to get any use out of the app.

### Design
To make the app more inclusive, it could offer auto-complete suggestions or allow for partial title matches. This would help users find the anime they are looking for, even if they don't remember the full or correct title.

### Expand
We have learned about biases related to memory and precision in user input; the app may unintentionally exclude users who are prone to typos or uncertain about exact details.

### Repeat
Some users may not be familiar with anime titles written in Romanized Japanese or may confuse similar-sounding names. Incorporating a more advanced search function, which recognizes alternative spellings or popular aliases for anime titles, could prevent this exclusion.

---

## Assumption 2: Users know anime genres well enough to fully utilize the genre filtering feature

### Critique
The app assumes that users understand anime genres and are able to input them correctly for filtering purposes. This can exclude users who are new to anime or unfamiliar with specific genres.

### Imagine
Users who are new to anime or who don’t understand the distinctions between genres (e.g. the difference between "Shounen", "Hentai", and "Seinen") may struggle to use the genre-filtering feature effectively - thus would not be able to utilize the feature.

### Design
The app could provide the user with a sort of genre guide through help messages, or even predefined genre categories that users can select from, rather than requiring them to input genre names manually, thus making the app more accessible to users with varying levels of knowledge about anime -- appealing to both potential users: Anime Newcomers and Enthusiasts.

### Expand
Biases related to familiarity with niche terminology -- newcomers to anime, or those unfamiliar with genre definitions, could feel excluded if they are expected to know & use specific genre names.

### Repeat
Some users may be unfamiliar with Japanese terms or genre definitions used in anime culture. Providing translations or simpler descriptions of each genre could help broaden the app's appeal to casual anime viewers or non-Japanese speakers.

---

## Assumption 3: Users are familiar with the English language

### C: Critique
The app assumes that all users are familiar English, which excludes non-English speakers or users who are more comfortable in other languages -- especially Japanese, the language of the media we are trying to make more accessible to users.

### I: Imagine
Non-English-speaking users may find it difficult to use the app if they cannot read the instructions or understand the dataset's content, especially since the anime titles and genres are presented only in English.

### D: Design
The app could support multiple languages, providing localized versions of the command line prompts and dataset content. Users could select their preferred language when starting the app.

### E: Expand
Biases related to language accessibility. Users who speak languages other than English may feel excluded if the app doesn't accommodate their linguistic needs.

### R: Repeat
Even users with a basic understanding of English might struggle with complex vocabulary so simplifying the language used in instructions or providing language-level options (e.g. beginner vs. advanced) could further increase accessibility.