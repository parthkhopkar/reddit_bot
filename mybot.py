import praw
import config
import re
import time
import math
import json

def bot_login():
	reddit = praw.Reddit(username=config.username,
			 password=config.password,
			 client_id=config.client_id,
			 client_secret=config.client_secret,
			 user_agent="Cosmic testing")
	return reddit


	
def run_bot(reddit):
	subreddit = reddit.subreddit('cosmic_crash')
	for submission in subreddit.hot(limit=None):
		for comment in submission.comments:
			if comment.id not in comments_id:	
				
				#Call forth the bot
				if "cosmic_bot!" in comment.body:
					print("Bot called by {author} | Comment ID= {comment_id} | Says Hello".format(author=str(comment.author),comment_id=str(comment.id)))
					print("Replying...")
					comment.reply("You beckoned and here I am!")
					comments_id.append(comment.id)
			
				#Factorial Calculator Regex		
				fact = re.search(r'(\d+)!', comment.body)
				if fact:
					num = int(fact.group(1))
					print("Bot called by {author} | Comment ID= {comment_id} | Factorial of {number}".format(author=str(comment.author),comment_id=str(comment.id),number=str(num)))
					print("Replying...")
					comment.reply("Factorial of {} is {}".format(str(num), math.factorial(num)))
					comments_id.append(comment.id)
		
		#Append to JSON file after checking one submission
		with open('comment_id.json','w') as f:
			json.dump(comments_id,f)
		#Bot sleeps after checking one submission			
		print("Sleeping for 5 seconds")
		time.sleep(5)			
		
with open('comment_id.json','r') as f:					
	comments_id = json.load(f)					
reddit = bot_login()
while True:
	run_bot(reddit)			
