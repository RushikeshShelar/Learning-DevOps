# Basic Bash Commands
1. `ssh [username]@[ipaddress/host]` - to connect to a linux Machine.
2. `echo` - Prints the argument in the terminal
   - `echo "[text]" > [filename]`: Write text to file.
   - `echo "[text]" >> [filename]`: Append text to the file
3. `namo [filename]` - nano text editor. To save the file `Ctrl + X > Y > Enter`
4. `vim [filename]` - Vim text editor. Press i to enter insert mode. Press `Esc` then Type `:wq` to write and Quit the file.
5. `cat [filename]` - Display the contents of the file to terminal
6. `shred [filename]` - So, in order to delete a file completely from a hard disk `shred` is used in Linux. This command overwrites the contents of a file multiple times. 
7. `ls` - list the files.
   - `ls -l` : The `-l` switch list the details as well like permissions.
   - `ls -a` : The `-a` Switch list the hidden Stuff as well.
   - `ls -al`: They can be combined as well.
8. `pwd` - Print Working Directory
9. `cd [path]` - change directory
10. `touch [filename]` - Quickest and Easiest Way to create a File.
    - `touch -d [date/time]` : Creates a File in future specified time.
11. `mkdir [foldername]` - Create a Folder.
12. `rmdir [foldername]` - Remove a Directory. The directory should be empty
13. `chown [username] [file]` - Change ownership of a file. 
15. `chmod` - chnage the permissions of the file / directory.
    - It has 3 Level (user, group, everyone)
    - It has 3 types of Permissions (read (r, 4) , write (w, 2), execute (x, 1))
    - You can change the permission using the following commands
    - `chmod 777 [file]` This gives everyone access to everthing ( 4 + 2 + 1 = 7)
    - `chmod g+w [file]` This give the Group acces to write the File
16. `cp [source] [destination]` - Used to copy from Source location to Destination
17. `mv [source] [destination]` - Used to move a file.
18. `rm [filename]` - Remove a File
     - `rm -r [directoryname]`: Remove files from a directory recursively
19. `ln -s [filename] [linkname]` - Create a link to the file.
20. `whoami` - Get which user is logged in.
21. `grep -i "[text" [file]` - Used to find the text from something. The -i flag indicates case insenstive
22.  `wc -w < [file]` - Word Count in a File.
23.  `sudo useradd [username]` - Add a user.
     - `sudo passwd [username]`: Set Password for username.
     - `sudo adduser [username]`: `adduser` prompts the user to set the password during user creation.
     - `su [username]`: Switch user
     - `passwd`: Change Current Password
24. `sudo userdel [username]` - Delete User
25. `sudo apt update` - Update the apt package.
26. `finger [username]` - Used to inspect a User.
27. `which [command]` - Gives the Location of the Command
28. `whereis [command]` - It gives the all the location of the command.
29. `whatis [command]` - Brief information about command
30. `wget [link/url]` - Get something form internet
31. `curl [url] > [filename]` - Get something from internet and save
32. `zip [zipFileName] [filename/folder]` - Compress into zip
    - `unzip [filename]` - Unzip the file
33. `cmp [file1] [file2]` - Compare two files
34. `diff [file1] [file2]` - Differnce between two files
35. `cat [file] | sort` - Sort the content Alphabetlically
36. `find [directory] -name "[filename]/[REGEX]"` Find a File
     - `find [directory] -type f -empty`: Find Empty Directories
     - ` find [directory] -perm /a=x`: Find all executables
37. `ifconfig` - IP Config
38. `grep` - Filter out based on parameter
    eg: `cat a.txt | grep "rushi"`
39. `ping [url/ip]` - Check whether your computer can reach it or not.
40. `traceroute [url/ip]` - Shows the route and Every hop as well as latency.
41. `netstat -tulpn` - Shows the Statistics.
    - `ss -tulpn`: Modern version of netstat
42. `sudo ufw allow 80` - Allows connection on Port 80.
43. `uname -a`- Displays system info.
    - `neofetch` : Displays formatted output
44. `ps -aux` - List all the active Processes.
45. `kill -9 [pid]` - Kill the Process
46. `pkill -f [filename]` - Kill the process
47. `systenctl` - Used to handles servicces
     - `sudo systemctl start [service]`
     - `sudo systemctl stop [service]`
     - `sudo systemctl status [service]`
     - `sudo systemctl restart [service]`
48. `history` - Command History
49. `sudo reboot`
50. `sudo shutdown -h now`        
 
## SYMBOLS
1. PIPE (|)

Use to pass(pipe) the output of a Command to another command. Used by the Symbol `|`
E.G: ``` cat one.txt | grep rushi```

2. OUTPUT REDIRECTION (> / >>)

Use to write a File or append to a file
E.G
- ``` echo Hello > hello.txt``` -  Overwrite the file with `Hello`
- ``` echo I am your Developer >> hello.txt``` -  Appnd the file with `I am your Developer`
