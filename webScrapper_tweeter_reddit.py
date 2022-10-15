# TOPIC: SCRAPE DATA FROM TWEET AND REDDIT AND PRE-PROCESS THEM
# CONTRIBUTERS: Arnav Kumar Behera, Vedanta Mohapatra
# LAST UPDATED ON: 27/09/2022
# TESTED ON: MacOS Monterey (12.6) [M1 Architecture] - Python 3.9.13  

###################################
########## REQUIREMENTS: ##########
###################################
# This code requires python 3.8+ to run, otherwise snscrape (Scrapping Module) doesn't work for reddit.
# Please make sure the following libraries are installed: snscrape, pandas, nltk, contractions, emoji, pandas, re, string using pip or similar installers.

##############################################
########## SUPPORTED FUNCTIONALITY: ##########
##############################################
# This code scrapes data from either Twitter or Reddit and preprocesses the extracted text.

########### FOR TWITTER: ##########
# This code can scrape data from a particular User, or any searches.
# Incase, of searches either the tweets can be extracted either in latest or top order.
# Scrapped data are the tweets. The follwoing things are extracted:
# ['Unique ID', 'Date', 'User', 'Tweet', 'Preproccesed Tweet']

########## FOR REDDIT: ##########
# This code can scrape data from a particular User, Sub-reddit or any searches.
# Scraped data can include either comments or posts.
# For Comments/Posts the following data are extracted:
# ['Unique ID', 'Date', 'Sub-reddit', 'Author', 'Title/Comment', 'Preprocessed Title/Comment']
# Incase of Posts Title is extracted, and for Comments the Comment(body) is extracted.

########## PRE-PROCESSING THE TEXT IS SAME FOR BOTH REDDIT AND TWITTER ##########
# After Scrapping the Text Preprocessing the following preprocessing is done (these can be varied according to the use-case):
# remove_urls(text): Removes the URLs in the text
# expand_contractions(text): Expands the sentence say I'll go to I will go. This helps in the follwoing pre-processing of removing stop words etc.
# text_lowercase(text): Converts all the words to lower-case, might be ignored in cases where CAPS highlights something, like say CAPS is usually associated with Shouting
# remove_punctuation(text): Removes the Punctuations in the text
# remove_numbers(text): Removes the numbers in the text, this is used for sentiment analysis
# remove_extra_whitespace(text): Removes the extra white spaces in the sentence, helpful for easy tokenisation.
# remove_stopwords(text): Removes unimportant words like is, are, am etc. But this might be ingored for context analysis.
# replace_emojis_with_words(text): Replaces emoji with appropriate word (Essential for Sentiment Analysis).
# lemmatize_word(text): Lemmantizes the sentences, and the final output is tokenized.


# Importing the Modules:
# For Text Extraction
import snscrape.modules.reddit as snreddit # Installation: pip install snscrape --upgrade (Requires Python 3.8+ to run)
import snscrape.modules.twitter as sntwitter # Installation: pip install snscrape --upgrade (Requires Python 3.8+ to run)
import pandas as pd  # Installation: pip install pandas --upgrade


# For Text Preprocessing
import nltk  # Installation: pip install nltk --upgrade
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
lemmatizer = WordNetLemmatizer()

import emoji  # Installation: pip install emoji --upgrade
import contractions  # Installation: pip install contractions --upgrade
import re # Comes with the python 3.9 (for other versions check and install if not found)
import string # Comes with the python 3.9 (for other versions check and install if not found)


# For writing to the CSV File
import csv # Comes with the python 3.9 (for other versions check and install if not found)
##############################
########## SCRAPING ##########
##############################

########## TWITTER: ##########

# Used when tweets by a particular user needs to be extracted.
def twitterUser(query, sizeOfQuery):
    tweets = []
    for tweet in sntwitter.TwitterUserScraper(query).get_items():
        if len(tweets) == sizeOfQuery:
            break
        else:
            tweets.append([tweet.id, tweet.date, tweet.user.username, tweet.content])
    return (tweets)

# Used when tweets of particular search topic needs to be extracted.
def twitterTopic(query, sizeOfQuery):
    tweets = []
    topOrLatest = int(input("Do you want to scrape tweets sorted by top or latest?\n [Press 1 for Top, Press anything else for Latest]\n:"))
    flag = False
    if topOrLatest == 1:
        flag = True
        # Basically the third attribute states if we need to scrape tweets sorted by top, i.e., if true we scrape by top.
    for tweet in sntwitter.TwitterSearchScraper(query, None, flag).get_items():
        if len(tweets) == sizeOfQuery:
            break
        else:
            tweets.append([tweet.id, tweet.date, tweet.user.username, tweet.content])
    return (tweets)
########## REDDIT: ##########
# Used when Comments/Posts by a particular user is neened for scrapping.


def redditUser(query, sizeOfQuery):
    results = []
    commentOrPost = int(input("Do you want to scrape for comments or posts?\n [Press 1 for Comment, Press anything else for Posts]\n: "))
    if commentOrPost == 1:
           # Attributes of RedditUserScraper: (name, submissions: bool = True, comments: bool = True, before: Any | None = None, after: Any | None = None, **kwargs: Any) -> None
        for result in snreddit.RedditUserScraper(query, False, True).get_items():
            if len(results) == sizeOfQuery:
                break
            else:
                results.append([result.id, result.created, result.subreddit, result.author, result.body])
    else:
        # Attributes of RedditUserScraper: (name, submissions: bool = True, comments: bool = True, before: Any | None = None, after: Any | None = None, **kwargs: Any) -> None
        for result in snreddit.RedditUserScraper(query, True, False).get_items():
            if len(results) == sizeOfQuery:
                break
            else:
                results.append([result.id, result.created, result.subreddit, result.author, result.title])
    return (results)

# Used when Comments/Posts in a particular Sub-reddit is neened for scrapping.
def redditSubreddit(query, sizeOfQuery):
    results = []
    commentOrPost = int(input("Do you want to scrape for comments or posts?\n [Press 1 for Comment, Press anything else for Posts]\n: "))
    if commentOrPost == 1:
        # Attributes of RedditSubredditScraper: (name, submissions: bool = True, comments: bool = True, before: Any | None = None, after: Any | None = None, **kwargs: Any) -> None
        for result in snreddit.RedditSubredditScraper(query, False, True).get_items():
            if len(results) == sizeOfQuery:
                break
            else:
                results.append([result.id, result.created, result.subreddit, result.author, result.body])
    else:
        # Attributes of RedditSubredditScraper: (name, submissions: bool = True, comments: bool = True, before: Any | None = None, after: Any | None = None, **kwargs: Any) -> None
        for result in snreddit.RedditSubredditScraper(query, True, False).get_items():
            if len(results) == sizeOfQuery:
                break
            else:
                results.append([result.id, result.created, result.subreddit, result.author, result.title])
    return (results)

# Used when Comments/Posts of a particular search is neened for scrapping.
def redditTopic(query, sizeOfQuery):
    results = []
    commentOrPost = int(input("Do you want to scrape for comments or posts?\n [Press 1 for Comment, Press anything else for Posts]\n: "))
    if commentOrPost == 1:
        # Attributes of RedditSearchScraper: (name, submissions: bool = True, comments: bool = True, before: Any | None = None, after: Any | None = None, **kwargs: Any) -> None
        for result in snreddit.RedditSearchScraper(query, False, True).get_items():
            if len(results) == sizeOfQuery:
                break
            else:
                results.append([result.id, result.created, result.subreddit, result.author, result.body])
    else:
        # Attributes of RedditSearchScraper: (name, submissions: bool = True, comments: bool = True, before: Any | None = None, after: Any | None = None, **kwargs: Any) -> None
        for result in snreddit.RedditSearchScraper(query, True, False).get_items():
            if len(results) == sizeOfQuery:
                break
            else:
                results.append([result.id, result.created, result.subreddit, result.author, result.title])
    return (results)

# Doesn't Execute further unless a valid input is provided.
twitterOrReddit = 0
invalid = True
while invalid == True:
    twitterOrReddit = int(input("Do you want to scrape from Twitter or Reddit?\n [Press 1 for Twitter, Press 2 for Reddit]\n:"))
    if twitterOrReddit == 1 or twitterOrReddit == 2:
        invalid = False
    else:
        print("Choice is invalid, select 1 or 2")

if twitterOrReddit == 1:

    # Doesn't Execute further unless a valid input is provided.
    choice = 0
    invalid = True
    while invalid == True:
        choice = int(input("Do you want to search for a particular user or a topic?\n [Press 1 for User, Press 2 for Topic]\n: "))
        if choice == 1 or choice == 2:
            invalid = False
        else:
            print("Choice is invalid, select 1 or 2")

    sizeOfQuery = int(input("Enter the number of tweets you want to scrape: "))
    query = input("Enter the query: ")
    tweets = []
    if choice == 1:
        tweets = twitterUser(query, sizeOfQuery)
    else:
        tweets = twitterTopic(query, sizeOfQuery)
else:

    # Doesn't Execute further unless a valid input is provided.
    choice = 0
    invalid = True
    while invalid == True:
        choice = int(input("Do you want to search for a particular user, subreddit or a topic?\n [Press 1 for User, Press 2 for Subreddit, Press 3 for Topic]\n: "))
        if choice == 1 or choice == 2 or choice == 3:
            invalid = False
        else:
            print("Choice is invalid, select 1, 2 or 3")

    sizeOfQuery = int(input("Enter the number of results you want to scrape: "))
    query = input("Enter the query: ")
    results = []
    if choice == 1:
        results = redditUser(query, sizeOfQuery)
    elif choice == 2:
        results = redditSubreddit(query, sizeOfQuery)
    else:
        results = redditTopic(query, sizeOfQuery)

# Can be used to check if the data has been succesfully scraped.
# df = pd.DataFrame(tweets, columns=['Unique ID', 'Date', 'Sub-reddit', 'Author', 'Title/Comment'])
# print(df)

########################################
########## TEXT PREPROCESSING ##########
########################################

# Remove URLs from text
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

# expand contractions, Like I'll go will be converted to I will got
def expand_contractions(text):
    return contractions.fix(text)

# Converts all the text into lower case, so basically HeLp, HELP, help all are same.
def text_lowercase(text):
    return text.lower()

# Removes punctuation
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# Remove numbers
def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result

# remove extra whitespaces
def remove_extra_whitespace(text):
    return " ".join(text.split())

# remove stopwords function
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return " ".join(filtered_text)

# Replace Emoji with words
def replace_emojis_with_words(text):
    return emoji.demojize(text, delimiters=("", ""))

# lemmatize string
def lemmatize_word(text):
    word_tokens = word_tokenize(text)
    # provide context i.e. part-of-speech
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in word_tokens]
    return lemmas


def text_preprocessing(text):
    text = remove_urls(text)
    text = expand_contractions(text)
    text = text_lowercase(text)
    text = remove_punctuation(text)
    text = remove_numbers(text)
    text = remove_extra_whitespace(text)
    text = remove_stopwords(text)
    text = replace_emojis_with_words(text)  # More useful for sentiment analysis
    text = lemmatize_word(text)  # More useful for sentiment analysis
    return text

final_result = []

# TWITTER:
if (twitterOrReddit == 1):
    for entry in tweets:
        preprocessed_text = text_preprocessing(entry[3])
        final_result.append([entry[0], entry[1], entry[2], entry[3], preprocessed_text])
    df = pd.DataFrame(final_result, columns=['Unique ID', 'Date', 'User', 'Tweet', 'Preproccesed Tweet'])
    print(df)

# REDDIT:
else:
    for entry in results:
        preprocessed_text = text_preprocessing(entry[4])
        final_result.append([entry[0], entry[1], entry[2], entry[3], entry[4], preprocessed_text])
    df = pd.DataFrame(final_result, columns=['Unique ID', 'Date', 'Sub-reddit', 'Author', 'Title/Comment', 'Preprocessed Title/Comment'])
    print(df)


#######################################
########## WRITE TO CSV FILE ##########
#######################################

# TWITTER:
Details = ['Unique ID', 'Date', 'User', 'Tweet', 'Preproccesed Tweet']

# REDDIT:
if (twitterOrReddit == 2):
    Details = ['Unique ID', 'Date', 'Sub-reddit', 'Author', 'Title/Comment', 'Preprocessed Title/Comment']

with open('data.csv', 'w', encoding='UTF8') as f:
    write = csv.writer(f)
    write.writerow(Details)
    write.writerows(final_result)
