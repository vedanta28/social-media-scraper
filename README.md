# Social Media Scraper
## _Arnav Kumar Behera, Vedanta Mohapatra_
### _October, 2022_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

In this project, we have implemented a social media scrapper for select supported websites and also pre-processed the extracted content. The project is built using [snscrape](https://github.com/JustAnotherArchivist/snscrape). Kindly refer to Download section in the README.md file of the linked github page for help in installing it.

## Features

- **Supported Websites**: Twitter, Reddit
- **Supported Features for Twitter**:
  - Scrape tweets from a particular User, or any searches
  - Incase, of searches either the tweets can be extracted either in latest or top order.
  - The follwoing things are extracted:  ['Unique ID', 'Date', 'User', 'Tweet', 'Preproccesed Tweet']
- **Supported Features for Reddit**:
  - This code can scrape comments/posts from a particular User, Sub-reddit or any searches.
  - For Comments/Posts the following data are extracted:
  - ['Unique ID', 'Date', 'Sub-reddit', 'Author', 'Title/Comment', 'Preprocessed Title/Comment']
  - Incase of Posts Title is extracted, and for Comments the Comment(body) is extracted.
- **Preprocessing the data**: The pre-processing involves removing URLS, expanding contractions, lower-casing all the texts, removing punctuations, removing numbers, removing extra white spaces, removing stop words, replacing emojis with words (implemented using [emoji](https://github.com/carpedm20/emoji)), lemmantizing the words. Any combinations of these pre-processing can be used depending on the use case.
- Storing the Extracted data into .csv files.

## 

## Softwares used

- [snscrape](https://github.com/JustAnotherArchivist/snscrape)
- [emoji](https://github.com/carpedm20/emoji)

## Contact Us

- Arnav Kumar Behera (www.alphaorionis@gmail.com)
- Vedanta Mohapatra (manav.sep.28@gmail.com)
