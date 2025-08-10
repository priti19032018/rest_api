# rest_api
# Flask Users REST API

## Overview
A simple Flask-based REST API to manage users in memory.  
Supports the following operations:
- Create a user (POST)
- List all users (GET)
- Get a user by ID (GET)
- Update a user (PUT)
- Delete a user (DELETE)

## Requirements
- Python 3.8+
- pip

## Setup

1. **Clone or download the project**
   ```bash
   git clone <your_repo_url>
   cd <project_folder>
   ```

2. **Create and activate a virtual environment**
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - **Linux/Mac**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App
```bash
python main.py
```
The app will run at:
```
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint        | Description         |
|--------|----------------|---------------------|
| GET    | /users         | List all users      |
| GET    | /users/<id>    | Get user by ID      |
| POST   | /users         | Create a new user   |
| PUT    | /users/<id>    | Update a user       |
| DELETE | /users/<id>    | Delete a user       |

## Example Usage (PowerShell)
**Create a user**:
```powershell
Invoke-RestMethod -Method POST http://127.0.0.1:5000/users `
  -ContentType "application/json" `
  -Body '{"name":"Alice","email":"alice@example.com"}'
```

**List all users**:
```powershell
Invoke-RestMethod -Method GET http://127.0.0.1:5000/users
```


