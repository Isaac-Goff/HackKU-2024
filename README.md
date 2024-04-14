# HackKU-2024: Info Checker
The goal of this project is to create a Chrome extension capable of doing basic fact checking and bias tracking on news articles.  This extension would work by comparing key words within an article against 
key words from other articles from reputable sources (BBC, The Guardian, etc) that are not the same article, then funneling the information and keywords to ChatGPT in to ask it whether the keywords selected from 
both the user's article and reputable article appear to be saying similar or the same things.  This in theory should determine whether the article the user is reading is trustworthy or not.  In addition to this,
the program will perform a sentiment analysis on the article to see if the article contains mostly positive, negative, or neutral wording to determine whether the article is more likely to be biased or not.  
This information will always be displayed on the user's screen.

This program works into the theme of social good as it will allow users to better determine the reliability of their news sources.  In modern times, news articles are commonly biased or outright fake when
displaying their information, making it harder for the average person to determine what is real and what is fake when browsing common news sources.  This is an issue that can make it hard to find good information 
with which to form our own opinions and make informed decisions.  With this extension, we hope to allow everyone the chance to quickly and easily determine what articles are worth reading and what articles may 
contain bias or misinformation.

## Inspiration
We are sick and tired of news articles that give misleading/biased views on world events. This project is way to slightly curve that issue. 


## What it does
This application webscrapes data and works with the nltk module to give an accurate sentiment analysis of an article. It will then allow you to compare the results to other webpages. There is also another feature that allows you to send parts of the article to open ai api to give a best estimation of the event. 


## How we built it
We combined our skills in both python, open ai api , and some ductape in order to create this application. 


## Challenges we ran into
Tkinter was used to create a GUI. One of our members is much more well versed in both html and css in the creation of front-end product. Python is rather weak when it comes to GUIs and the member had issues adjusting to it. Webscraping for the other teammate went much better. It was still hard as getting the data was easy but parsing it/getting the info we needed was very hard. 


## Accomplishments that we're proud of
The web scraper works + sentiment analysis + open ai api. It was very fun to learn how all this works together.


## What we learned
In web scarping getting the data is easy. Organizing/extracting what you want is hard. 

## What's next for Hack the Truth
Possibly an edition that webscrapes and tells you history about memes. 
