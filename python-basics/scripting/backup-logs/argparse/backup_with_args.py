import os
import argparse
import shutil
from datetime import datetime

parser = argparse.ArgumentParser(description="Simple backup Script")

parser.add_argument('--source', type=str, required=True, help="Path to the Source Directory to backup")
parser.add_argument('--dest', type=str, required=True, help="Path to the Target Directory to backup")

# Default Argument
parser.add_argument('--retention', type=int, default=7, help='Retention period in days')

# Optional Argument
parser.add_argument('--compress', action='store_true', help='Compress backup after copying')
args = parser.parse_args()

print(f"Backuping from {args.source} to {args.dest}")

args = parser.parse_args()

# Generate timestamp folder
today = datetime.today().strftime('%Y-%m-%d')
backup_dir = os.path.join(args.dest, today)
os.makedirs(backup_dir, exist_ok=True)

# Copy files
for file_name in os.listdir(args.source):
    if file_name.endswith(".log") or file_name.endswith(".bak"):
        full_path = os.path.join(args.source, file_name)
        if os.path.isfile(full_path):
            shutil.copy(full_path, backup_dir)

print(f"Backup complete: {backup_dir}")

# Optional: Compress
if args.compress:
    shutil.make_archive(backup_dir, 'zip', backup_dir)
    print(f"Compressed: {backup_dir}.zip")
