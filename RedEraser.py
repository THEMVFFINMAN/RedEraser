#!python2

import praw

# Enter your username and password below
USERNAME  = "YOUR USERNAME"
PASSWORD  = "YOUR PASSWORD"

# Enter list of subreddits to ignore in lowercase
IGNORE_SUBREDDITS = {}

# Leave this as -1 if you want to erase everything
# Otherwise change to how many comments or posts you want deleted
commentsToDelete = -1
postsToDelete = -1

'''--------------------------------------------------------'''
#                                                            #
# Generally the things below this line should not be touched #
#                                                            #
'''--------------------------------------------------------'''

# Leave the useragent as is
USERAGENT = "Comment Deleter"

# This just tracks how many comments and posts have been deleted so far
# Do not touch
commentsDeleted = 0
postsDeleted = 0

# This simply logs you in and returns a user object
def login():
    r = praw.Reddit(USERAGENT)
    r.login(USERNAME, PASSWORD)
    user = r.get_redditor(USERNAME)

    print "Successfully logged %s in" % USERNAME

    return user

# Takes the user object and deletes the users comments up to the amount
# specified in commentsToDelete above
def commentDeleter(user, commentsToDelete):

    print "Deleting comments now"

    # Tracks how many comments have deleted so far
    global commentsDeleted

    # By accessing the 100 comment limit one billion times,
    # it's safe to assume that this will delete any and all comments/posts (up to 100 billion)
    for o in xrange(0,999999999):

        # This is a simple check after one run through to see if there were any comments to delete
        if o > 0 and commentsDeleted == 0:
            print "No comments to delete!"
            return

        # Due to the limits on reddit's API, this for loop can only access 100 comments at a time
        for c in user.get_comments(limit=None):

            # Because reddit only saves the most recently edited comment,
            # each comment is edited with a pound symbol and then deleted
            if str(c.subreddit).lower() in IGNORE_SUBREDDITS:
                continue
            c.edit('#')
            c.delete()

            commentsDeleted += 1
            print "Comment Deleted"

            # It checks if it's deleted your specified amount of comments,
            # if left at '-1' this condition will never be met and it will delete all comments
            if commentsDeleted == commentsToDelete:
                print "{0} Comments Deleted".format(commentsDeleted)
                return

            # After every 10 comments it prints how many comments have been deleted so far
            if commentsDeleted % 10 == 0:
                print "{0} Comments Deleted".format(commentsDeleted)

    if commentsDeleted != 0:
        print "All {0} Comments Deleted".format(postsDeleted)

# This is almost identical to commentDeleter()
def postDeleter(user, postsToDelete):

    print "Deleting posts now"

    global postsDeleted

    for o in xrange(0,999999999):

        if o > 0 and postsDeleted == 0:
            print "No posts to delete!"
            return

        for p in user.get_submitted(limit=None):
            if str(p.subreddit).lower() in IGNORE_SUBREDDITS:
                continue
            if p.selftext:
                p.edit('#')
            p.delete()
            postsDeleted += 1

            if postsDeleted == postsToDelete:
                print "{0} Posts Deleted".format(postsDeleted)
                return

            if postsDeleted % 10 == 0:
                print "{0} Posts Deleted".format(postsDeleted)

    if postsDeleted != 0:
        print "All {0} Posts Deleted".format(postsDeleted)

def main():
    try:
        user = login()
    except Exception, e:
        print "Login failed due to: "
        print str(e)
        return

    try:
        commentDeleter(user, commentsToDelete)
        postDeleter(user, postsToDelete)
    except Exception, e:
        print "Deletion failed due to: "
        print str(e)
        return

    print "All {0} Comments and {1} posts Deleted".format(commentsDeleted, postsDeleted)


if __name__ == "__main__":
    main()
