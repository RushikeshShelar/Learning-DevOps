import subprocess

# Run a simple command
subprocess.run(["ls", "-l"])

# Capture output (Python 3.7+)
result = subprocess.run(["whoami"], capture_output=True, text=True)
print(result.stdout)

# Run with shell=True
subprocess.run("echo $HOME", shell=True)

# Run and get return code
res = subprocess.run(["ls", "not_found.txt"])
print(res.returncode)  # 0 = success, 1+ = error

