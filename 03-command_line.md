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

> > pwd, print working directory  
    cd, change directory  
    ls, list files and directories  
    file, classify a files contents  
    /, root directory  
    /bin, where the binary files are.  
    /usr/bin, where the applications for the system users are.  
    /root, superuser root directory.  
    cp, copy files and directories  
    rm, remove files and directories.  
    mv, move files and directories.  
    mkdir, create directories.
     
     
     

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

> >  ls-List directory contents 
     ls -a, all.  Tells the computer not to ignore entries starting with.  
     ls -l, use a long listing format   
     ls -lh, use a long format and print sizes in human readable format   
     ls -lah, use a long format, print sizes in human readable format, and print the author of each file   
     ls -t, sort by modification time.   
     ls -Glp, long listing without group names and append /indicator to directories.  


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ```bash  
    ls -a  
    ls -d  
    ls -F  
    ls -p  
    ls -u  
    ```
    

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs constructs argument lists and invokes other utilities.  It reads standard input items, them executes the commands one or more times with any initial arguments followed by items read from standard input.   
Example:  
   ```bash  
   $ echo 1234 | xargs will print 1234.  
   ````

 

