# Real World Docker Scenario(1)
Simulate a real Dev + DB setup with backup automation.

## Stack:
- Flask App
- MySQL
- Docker Compose
- Volume for persistence
- Backup script that copies DB data into host

##  Folder Structure
```bash
root/
│
├── app/
│   ├── app.py
│   └── Dockerfile
│
├── mysql/
│   └── init.sql
│
├── docker-compose.yml
├── backup.sh
└── .env
```