import praw
import config

def bot_login():
	r=praw.Reddit(username=config.username,
			password=config.password,
			client_id=config.client_id,
			client_secret=config.client_secret,
			user_agent="Cosmic testing")
	return r
	
def run_bot(r):
	for comment in r.subreddit('test').comments(limit=25):
		if "batman" in comment.body:
			print("Comment found")
			print("Replying to comment | "+"author: "+str(comment.author))	
			comment.reply("[I am the night!](http://9cover.com/images/ccovers/1365477801cartoons-batman-in-the-night.jpg)")
				
r=bot_login()
run_bot(r)			
