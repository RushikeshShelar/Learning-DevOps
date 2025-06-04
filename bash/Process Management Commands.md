# Process Management Commands

- List all Processes or Jobs
```bash
jobs
```
- Resume job to Foreground
 ```bash
fg [id]
```
- Resume jon to background
  ```bash
   bg [id]
  ```

## Nice Value 
Nice value states the Priority of the job. It ranges from -20 to 19
-20 highest priority while 19 being lowest priority
```bash 
nice -n [nice_value] [process]
```
eg: `nice -n -5 hello.sh`

To check the nice value of a Process
```ps -i [pid] ```

## nohup
If you want your proceess to keep running even after closing your terminal use nohup.
Command: 
```bash
nohup [process] &
```
This creates a file called `nohup.out` that has all the logs or output of the process/Program.
If you don't want a log file to be created use follwing command.
```bash
nohup [process] > /dev/null 2>&1 &
```
