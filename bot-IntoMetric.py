import praw

reddit = praw.Reddit('IntoMetric')

pfe = reddit.subreddit('pythonforengineers')

for comment in pfe.stream.comments():
	# If we haven't replied to this post before
	# if submission.id not in posts_replied_to:
    text = comment.body
    author = comment.author
    list_of_words = text.split()

    if (' inches' in text.lower()):
        comment.reply("IntoMetric verifies")


# for comment in bot.subreddit('pythonforengineers').stream.comments():
#     text = comment.body
#     author = comment.author
#     list_of_words = text.split()
#
#     if (' inches ' in text.lower()):
#         comment.reply("IntoMetric verifies")

    # text = comment.body
    # author = comment.author
    # list_of_words = text.split()
    # print list_of_words
    #
    # if (' inches ' in text.lower()):
    #     prev_word = list_of_words[list_of_words.index('inches') - 1]
    #     message = "that is " + prev_word + ' cm'
    #     comment.reply(message)
