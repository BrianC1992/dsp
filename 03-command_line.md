# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls-List directory contents /n
    ls -a, all.  Tells the computer not to ignore entries starting with ./n
    ls -l, use a long listing format /n
    ls -lh, use a long format and print sizes in human readable format /n
    ls -lah, use a long format, print sizes in human readable format, and print the author of each file /n
    ls -t, sort by modification time. /n
    ls -Glp, long listing without group names and append /indicator to directories. /n

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs constructs argument lists and invokes other utilities.  It reads standard input items, them executes the commands one or more times with any initial arguments followed by items read from standard input. /n

Example: $ echo 1234 | xargs will print 1234.

 

