# 📝 FastAPI Notes App

A simple yet production-ready **Notes Application** built using **FastAPI**, **MongoDB**, and **Jinja2**.  
This project demonstrates backend fundamentals, database integration, and clean project structure.

--------------------------------------------------

## 🚀 Features

- Create notes with **title** and **description**
- Mark notes as **important**
- Persist data using **MongoDB**
- Server-side rendering with **Jinja2**
- Light/Dark mode toggle (user preference saved)
- Clean and scalable FastAPI project structure
- Environment-variable based configuration (secure)

--------------------------------------------------

## 🛠 Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** MongoDB (Atlas)
- **Frontend:** HTML, CSS, Bootstrap
- **Templating:** Jinja2
- **Server:** Uvicorn

--------------------------------------------------

## 📂 Project Structure

```
notes-app/
│
├── database/
│ └── db.py
├── models/
│ └── note.py
├── routes/
│ └── note.py
├── schemas/
│ └── note.py
├── static/
│ └── style.css
├── templates/
│ └── index.html
│
├── index.py
├── requirements.txt
├── .gitignore
└── README.md
```

--------------------------------------------------

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
git clone https://github.com/MihirKalvatia/notes-app.git
cd notes-app

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Configure MongoDB
Create a file named .env in the project root and add:
MONGO_URI=your_mongodb_connection_string

Note: The `.env` file is ignored by Git for security reasons.

### 4️⃣ Run the application
uvicorn index:app --reload 

### 5️⃣ Open in browser
http://127.0.0.1:8000

--------------------------------------------------

## 🧠 What This Project Demonstrates

- FastAPI routing and request handling
- MongoDB integration using PyMongo
- Environment-based configuration
- Server-side rendering with templates
- Clean backend project structure

