import praw
import os

with open('/home/tomas/IntoMetric/posts_replied_to.txt') as f:
posts_replied_to = open('posts_replied_to.txt','r+')

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

units_imp = ["inches", "feet", "miles", "gallons", "pounds", "ounces", "mph"]
units_met = ["cm", "m", "km", "L", "kg", "g", "km/h"]
multip = [2.54, 0.3048, 1.60934, 3.78541, 0.453592, 28.3495, 1.60934]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print posts_replied_to

for comment in im.stream.comments():
    author = comment.author
    if (author!='IntoMetric' and comment.id not in posts_replied_to):
        text = comment.body
        list_of_words = text.lower().split()
        for u in range(len(units_imp)):
            if (units_imp[u] in list_of_words):
            	num_str = list_of_words[list_of_words.index(units_imp[u])-1]
            	num_usable = num_str.replace(',','')
            	if is_number(num_usable):
                    num_eur = num_usable.replace('.',',')
                    comment.reply(num_eur+" "+units_imp[u]+" = "+str(float(num_usable)*multip[u])+" "+units_met[u])
                    posts_replied_to.append(comment.id)
                    print posts_replied_to
