import praw, time

USERNAME  = "blendt"
PASSWORD  = "MYPASSWORD"
WAIT = 60

WAITS = str(WAIT)

r = praw.Reddit("Comment Deleter")
r.login(USERNAME, PASSWORD)

def deleteNeg():
    
    print("\nCOMMENT SCORE CHECK CYCLE STARTED")
    user = r.get_redditor(USERNAME)

    for c in user.get_comments(limit=None):
      
        if c.score < 1:
            print str(c.score) + " " + c.body
            c.delete()
            print("Comment Deleted")

      
    print("COMMENT SCORE CHECK CYCLE COMPLETED")
    print("\nComment Karma:\t\t%s"%user.comment_karma)

def unreadMessages():
    unread = 0
    for mail in r.get_unread():
            unread = unread + 1
            
    print("Unread Messages:\t" + str(unread) + "\n")

while True:
    try:
        deleteNeg()
        unreadMessages()
        time.sleep(WAIT)
    except :
        print('ERROR - Running again in ' + WAITS + ' seconds \n')
        deleteNeg()
        time.sleep(WAIT)
