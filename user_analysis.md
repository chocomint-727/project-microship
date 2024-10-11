# Potential Users:
- Anime Newcomers: Those who are new to anime and want to get their feet wet in the world of anime by searching for animes with good ratings and by looking for genres that match their interests.
- Anime Enthusiasts: The seasoned Anime enjoyers - anime enthusiasts have watched a number of anime and know their way around anime lingo, enabling them to easily search for the next anime that they want to watch.
- Anime Researchers: Those who are researching anime and want a robust way to get information quickly.

# Potential Benefits
- Users who are comfortable with a command line interface can get a near instant answer to their queries.
- The ability to filter anime based on multiple genres allows users to tailor results to their specific tastes.
- Researchers can find information about the ratings and genres of various anime quickly.
- There is something for everyone; with our extremely large and comprehensive dataset, anime enjoyers will be able to find anime they will undoubtedly enjoy.


# CIDER Analysis

## Four assumptions are analyzed here.

### Critique
The app assumes users will always know and input the exact titles of anime correctly, excluding users who do not remember the exact names of an anime. The app also assumes that users understand anime genres and are able to input them correctly for filtering purposes, which will make users who are new to anime or unfamiliar with specific genres excluded from using the app efficiently. Furthermore, the app assumes that all users are familiar with English, which excludes non-English speakers or users who are more comfortable in other languages, especially Japanese, the language of the media we are trying to make more accessible to users.


### Imagine
Users who don't remember the exact title of an anime or who misspell the title would not be able to retrieve the corresponding score and would not be able to get any use out of the software. Users who are new to anime or who don’t understand the distinctions between genres (e.g. the difference between "Shounen" and "Seinen") may struggle to use the genre-filtering feature effectively - thus would not be able to utilize the feature. Non-English-speaking users may find it difficult to use the app if they cannot read the instructions or understand the dataset's content, especially since the anime titles and genres are presented only in English.

### Design
To make the app software more inclusive, it could offer auto-complete suggestions or allow for partial title matches, which would help users find the anime they are looking for in a more efficient way and decrease the likelihood of bad input. This would help users who do not remember the exact title of an anime that they may be looking for.
To help users who are unfamiliar with anime genres, the app could provide the user with a sort of genre guide through help messages, or even predefined genre categories that users can select from, rather than requiring them to input genre names manually, thus making the software more accessible to users with varying levels of knowledge about anime, appealing to anime newcomers and anime enthusiasts.
Non-English speaking would benefit from the app adding support for multiple languages, providing localized versions of the command line prompts and dataset content for various languages, definitely including Japanese since a large amount of anime users are native-Japanese speakers. Users could select their preferred language when starting the app.

### Expand
We have learned about biases related to precision in user input in class, particularly that which has to do with less-abled users; the app may unintentionally exclude users who are prone to typos, such as people with less experience with typing or uncertain about the exact details of various anime.

### Repeat
We can also help out users who have difficulty typing titles correctly either because they are not very comfortable with typing or because they do not remember how to spell titles by implementing the previously mentioned auto-complete system which can complete the start of a title being typed in the command line.

---

