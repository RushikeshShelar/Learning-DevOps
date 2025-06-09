import os
import shutil
from pathlib import Path
from datetime import datetime

source_dir=Path("test_logs")
today=datetime.today().strftime('%Y-%m-%d')
backup_dir = Path("backups") / today
backup_dir.mkdir(parents=True, exist_ok=True)


log_file = open("backup.log", "a")

for file in source_dir.glob("*.log"):
    file_size = file.stat().st_size
    size_mb = file_size / (1024 * 1024)

    if size_mb > 5:
        log_file.write(f"[SKIPPED] {file.name} - {size_mb:.2f} MB too large.\n")
        continue

    shutil.copy2(file,backup_dir)
    log_file.write(f"[COPIED]  {file.name} - {size_mb:.2f} MB\n")


log_file.write(f"Backup completed at {datetime.now()}\n{'-'*40}\n")
log_file.close()
print(f"Backup done! Check {backup_dir} and 'backup.log'")

