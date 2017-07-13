import praw
import os

reddit = praw.Reddit('IntoMetric')

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

im = reddit.subreddit('IntoMetric')

for comment in im.stream.comments():

    text = comment.body
    author = comment.author

    if (' inches' in text.lower() and author != 'IntoMetric'):
        list_of_words = text.split()

        # If we haven't replied to this post before
        if comment.id not in posts_replied_to:
            prev_word = list_of_words[list_of_words.index('inches')-1]
            # Remove dots and change decimal commas to dots
            prev_num = float((prev_word.replace('.','')).replace(',','.'))
            comment.reply(str(prev_num)+" inches = "+str(prev_num*2.54)+" cm")
