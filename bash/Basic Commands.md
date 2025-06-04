# Basic Bash Commands
1. `echo` - Prints the argument in the terminal
2. `cat` - Display the contents of the file to terminal
3. `ls -l` - list the files with details like permissions
4. `chmod` - chnage the permissions of the file / directory.
   - It has 3 Level (user, group, everyone)
   - It has 3 types of Permissions (read (r, 4) , write (w, 2), execute (x, 1))
   - You can change the permission using the following commands
   - `chmod 777 [file]` This gives everyone access to everthing ( 4 + 2 + 1 = 7)
   - `chmod g+w [file]` This give the Group acces to write the File
5. `cp [source] [destination]` Used to copy from Source location to Destination
6. `grep -i "[text" [file]` - Used to find the text from something. The -i flag indicates case insenstive
7.  `wc -w < [file]` - Word Count in a File



## Shell scripts
1. `#!/bin/bash` - tells which interpreter to use as a shell.
2. `$FIRST_NAME` -  Varibales are placed using the `$` sign.
3. `read FIRST_NAME` - Used to read value from terminal and Store in Variable
4. `$1 $2` - Positional arguments (Refers to the Values passed at 1st and 2nd place.


## SYMBOLS
1. PIPE (|)

Use to pass(pipe) the output of a Command to another command. Used by the Symbol `|`
E.G: ``` cat one.txt | grep rushi```

2. OUTPUT REDIRECTION (> / >>)

Use to write a File or append to a file
E.G
- ``` echo Hello > hello.txt``` -  Overwrite the file with `Hello`
- ``` echo I am your Developer >> hello.txt``` -  Appnd the file with `I am your Developer`
