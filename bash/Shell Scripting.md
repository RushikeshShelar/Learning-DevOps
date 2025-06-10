## Shell scripts
1. `#!/bin/bash` - tells which interpreter to use as a shell. The `#!` is know as Shebang.
2. `$FIRST_NAME` -  Varibales are placed using the `$` sign.
3. `read FIRST_NAME` - Used to read value from terminal and Store in Variable
4. `$1 $2` - Positional arguments (Refers to the Values passed at 1st and 2nd place.
5. Conditionals (IF ELSE)
    ```shell
   if [{$1,,} = "Rushi"]; then
      echo "You are Welcome"
   elif [{$1,,} = "help"]; then
      echo "Enter your user name"
   else
      echo "Idk you!"
   fi
   ```
6. Case Statement (Similar to Switch Case)
   ```shell
    case ${1,,} in
            Rushi | Admin)
               echo "Welcome"
            help)
               echo "Enter Username"
            *)
               echo "Idk YOU"
    esac
   ```
7. Array (@ print whole list)
   ```shell
   MY_LIST=(one two three)
   echo ${MY_LIST[@]}
   echo ${MY_LIST[1]}
   ``` 
8. For Loop
   ```shell
   MY_LIST=(one two three four five)
   for item in ${MY_LIST[@]}; do
      echo -n $item | wc -c; done
   ```
7. Functions
   ```shell
   #!/bin/bash
   showuptime(){
      local uptime=$(uptime -p | cut -c4-)
      local since=$(uptime -s)
      cat << EOF
   -----
   This machine is up for ${uptime}
   IT has been running since ${since}
   -----
   EOF
   }

   showuptime
   ```
   ```shell
   #!/bin/bash

   showname(){
           echo Hello $1;
           if [ ${1,,} = rushi ]; then
                   return 0;
           else
                   return 1;
           fi
   }
   
   showname $1
   if [ $? = 1 ]; then
           echo "Unknown"
   else
           echo Hello $1
   fi
   ```
8. AWK
It is used to filter the contents of a File to a text input.
- ```awk '{print $1}' file``` this prints the 1st Word in the file seprated by space
- ```awk -F[symbol] '{print $1}' file``` THe -F flag followed by a seperator
- ``` echo just get this word: Rushi | awk '{print $5}' ``` Piping words in awk    
