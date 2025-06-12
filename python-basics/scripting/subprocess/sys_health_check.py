import subprocess
from rich.console import Console
console = Console()

commands = {
    "Uptime": ["uptime", "-p"],
    "Disk Space": ["df", "-h"],
    "Memory Usage": ["free", "-h"],
    "LoggedIn Users": ["who"],
    "Top 5 Processes": ["ps","aux","--sort=-%mem"],
    "Python Verison": ["python3", "--version"]
}

console.print("[bold green]🔍 SYSTEM HEALTH CHECK REPORT [/bold green]\n" + "-"*30)

for title, command in commands.items():
    console.print(f"\n [bold blue]🧪 {title}: [/bold blue]")

    try:
        result = subprocess.run(command, capture_output = True, text = True, check = True)
        output_lines = result.stdout.strip().split("\n")
        for line in output_lines[:5]:  # Limit output if long
            print("   " + line)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red] ❌ Error running {title}: {e} [/bold red]")

