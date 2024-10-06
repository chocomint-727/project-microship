# Potential Users:
- Anime Newcomers: Those who are new to the Anime genre and want to get their feet wet in the world of Anime.
- Anime Enthusiasts: The seasoned Anime enjoyers - an Anime Enthusiast has watched a number of Anime and know their way around Anime lingo.
- Anime Researchers: Those who are researching Anime and want a robust way to get information quickly.

# Potential Benefits
- Robust use, where users who are comfortable with a commandline can get a near instant answer to their queries.
- The ability to filter anime based on multiple genres allows users to tailor results to their specific tastes - or find new Anime shows to watch based on the aforementioned tastes.
- There is something for everyone; with our extremely large and comprehensive dataset, users will be able to find at least dozens of Anime they will undoubtedly enjoy.


# CIDER Analysis

## Assumption 1: Users are able to input titles correctly when using the score retrieval feature

### Critique
The app assumes users will always know and input the exact titles of anime correctly, excluding users who may mistype titles for whatever reason such as a disability, or those who cannot physically type -- even those who are simply unsure of a genres name.

### Imagine
Users who don't remember the exact title of an anime or who misspell the title would not be able to retrieve the corresponding score -- then they would get frustrated and not be able to get any use out of the app.

### Design
To make the app more inclusive, it could offer auto-complete suggestions or allow for partial title matches, which would help users find the anime they are looking for in a more efficient way and decrease the likelihood of bad input.

### Expand
We have learned about biases related to precision in user input -- particularly which has do with less-abled users; the app may unintentionally exclude users who are prone to typos or uncertain about exact details.

### Repeat
Some users may not be familiar with anime titles written in Romanized Japanese or may confuse similar-sounding names. Incorporating a more advanced search function, which recognizes alternative spellings or popular aliases for anime titles - perhaps even acronyms - could prevent this exclusion

---

## Assumption 2: Users know anime genres well enough to fully utilize the genre filtering feature

### Critique
The app assumes that users understand anime genres and are able to input them correctly for filtering purposes, which will make users who are new to anime or unfamiliar with specific genres excluded from using the app efficiently.

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

### Critique
The app assumes that all users are familiar English, which excludes non-English speakers or users who are more comfortable in other languages -- especially Japanese, the language of the media we are trying to make more accessible to users.

### Imagine
Non-English-speaking users may find it difficult to use the app if they cannot read the instructions or understand the dataset's content, especially since the anime titles and genres are presented only in English.

### Design
The app could support multiple languages, providing localized versions of the command line prompts and dataset content. Users could select their preferred language when starting the app.

### Expand
Biases related to language accessibility. Users who speak languages other than English may feel excluded if the app doesn't accommodate their linguistic needs.

### Repeat
Even users with a basic understanding of English might struggle with complex vocabulary so simplifying the language used in instructions or providing language-level options (e.g. beginner vs. advanced) could further increase accessibility.