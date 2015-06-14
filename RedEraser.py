#!python2
 
import praw
 
USERNAME  = "Username"
PASSWORD  = "Password"
USERAGENT = "Comment Deleter"
 
r = praw.Reddit(USERAGENT)
r.login(USERNAME, PASSWORD)
 
user = r.get_redditor(USERNAME)
 
for o in xrange(0,999):
    cc = 0
    pp = 0    
 
    for c in user.get_comments(limit=None):
        c.edit('#')
        c.delete()
        print 'Pass: ' + str(o) + ' ; Iteration: ' + str(cc) + ' ; Comment Deleted'
        cc += 1
 
    print str(cc) + ' Comments Deleted'
 
    for p in user.get_submitted(limit=None):
        if p.selftext:
            p.edit('#')
        p.delete()
        print 'Pass: ' + str(o) + ' ; Iteration: ' + str(pp) + ' ; Post Deleted'
        pp += 1
 
    print str(pp) + ' Posts Deleted'
