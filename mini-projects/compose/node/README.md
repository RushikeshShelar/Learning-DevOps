# Real World Docker Scenario (2)
Simulate a real Dev + DB setup with backup automation.

## Stack:
- Node + Express 
- MongoDB
- Docker Compose
- Volume for persistence
- Backup script that copies DB data into host

##  Folder Structure
```bash
root/
│
├── app/
│   ├── index.js
│   ├── package.json
│   ├── package-lock.json
│   └── Dockerfile
│   
├── mongol/
│   └── init.js
│
├── docker-compose.yml
└── .env
```