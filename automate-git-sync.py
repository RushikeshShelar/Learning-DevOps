import git
from datetime import datetime

repo_path = "/home/rushi/devops"

try:
    repo = git.Repo(repo_path)
    stashed = False

    # Check if the repository is clean before pulling
    if repo.is_dirty(untracked_files=True):
        # Stash any uncommitted changes
        repo.git.stash('save', 'Auto Stash before pulling')
        with open('/var/log/rushi/git-sync.log', 'a') as log_file:
            print("Uncommitted changes detected. Stashing changes before pulling.")
            log_file.write(
                f"[INFO]: {datetime.now().strftime('%Y-%m-%d-%H:%M:%S')} - Stashed the files temporary for pulling.\n")
        stashed = True

    origin = repo.remotes.origin
    origin.pull()

    log_message = f"[SUCCESS]: {datetime.now().strftime('%Y-%m-%d-%H:%M:%S')} - Pulled latest changes\n"
    print(log_message)

except Exception as e:
    log_message = f"[ERROR]: {datetime.now().strftime('%Y-%m-%d-%H:%M:%S')} - {str(e)}\n"
    print(log_message)

finally:
    with open('/var/log/rushi/git-sync.log', 'a') as log_file:
        log_file.write(log_message)

    if stashed:
        repo.git.stash('pop')
        # Log Message for popping the stash
        with open('/var/log/rushi/git-sync.log', 'a') as log_file:
            print("Popped the stashed changes after pulling.")
            log_file.write(
                f"[INFO]: {datetime.now().strftime('%Y-%m-%d-%H:%M:%S')} - Popped the stashed files after pulling.\n")
