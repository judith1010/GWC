'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
#
# def numOfLetter(tw, letter):
# 	count = 0
# 	for l in tw:
# 		if l == letter or l.lower() == letter:
# 			#print(l)
# 			count += 1
# 	return count

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)

# We can close the file now that we have locally stored the data.
tweetFile.close()

# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])

# Encourage students to think about how there are
# often multiple solutions for each problem, and
# how each solution might have strenghts and drawbacks.
# sum = 0
# num = 0
# for tweet in tweetData:
# 	# tweet = tweetData[i]
# 	if "favorite_count" not in tweet:
# 		 print('none')
# 	else:
# 		 print(tweet['favorite_count'])
# 		sum += tweet["favorite_count"]
# 		num += 1
# avg = sum/num
#  print(avg)
#
# a = []
# for tweet in tweetData:
# 	a.append(tweet['lang'])
#  # print(a)
#  print(set(a))
#
# eCount = 0
# jCount = 0
# for tweet in tweetData:
# 	if 'text' in tweet:
# 		eCount += numOfLetter(tweet['text'], 'e')
# 		jCount += numOfLetter(tweet['text'], 'j')
#  print(f"There are {eCount} 'e's in this data")
#  print(f"There are {jCount} 'j's in this data")
#
# letterCount = ["Number of letters in data:"]
# alpha = sorted('qwertyuiopasdfghjklzxcvbnm')
# for letter in alpha:
# 	tempCount = 0
# 	for tweet in tweetData:
# 		if 'text' in tweet:
# 			tempCount += numOfLetter(tweet['text'], letter)
# 	letterCount.append([letter, tempCount])
#  print(letterCount)

tweetList = []
for tweet in tweetData:
	if 'text' in tweet:
		tweetList.append(tweet['text'])
# print(tweetList)

pList = []
for tweet in tweetList:
	tb = TextBlob(tweet)
	tbp = tb.polarity
	pList.append(tbp)
# print(pList)

dictList = []
for i in range(len(tweetData)):
	temp_dict = {}
	temp_dict["tweet id"] = tweetData[i]['id']
	temp_dict["tweet"] = tweetList[i]
	temp_dict["polarity"] = pList[i]
	dictList.append(temp_dict)
# print(dictList)

# tString = ""
# for tweet in tweetList:
# 	tString += tweet + ' '
# # print(tString)
# stopwords = set(STOPWORDS)
# wc = WordCloud(height = 10000, width = 10000, max_words = 1000, stopwords = stopwords)generate(tString)
# plt.figure(figsize = (10, 10), facecolor = None)
# plt.imshow(wc, interpolation = 'bilinear')
# plt.tight_layout()
# plt.axis('off')
# # plt.show()
# plt.savefig('wodcloud.png')

n, bins, patches = plt.hist(pList, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Polarity')
plt.ylabel('Probability')
plt.title('Histogram of Sentiment')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
