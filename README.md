### **Agentic AI Backend – Real-Time Intelligent Assistant System**

Agentic AI Backend is a modular, FastAPI-based backend system that demonstrates an agent-based AI workflow, where each agent independently handles a specific task such as document question answering, meeting scheduling, and external information retrieval.

This project is designed to showcase how multiple intelligent agents can work together to provide structured, context-aware responses in real time.

---

### **Technologies Used**

Python · FastAPI · SQLite · DuckDuckGo Search · PyPDF2 · Uvicorn

---

### **Project Overview**

This backend system integrates multiple AI-inspired agents:

- **Document Agent** – Reads PDF/Text documents and answers questions from the content

- **Web Search Fallback** – Uses DuckDuckGo when answers are not found in documents

- **Database Agent** – Queries meeting data (today, tomorrow, all meetings) from SQLite

- **Agentic Architecture** – Each agent is modular and independently extendable

The architecture is built for **clarity, scalability, and learning purposes,** making it ideal for academic projects, demos, and backend experimentation.

---

### **Features**

- Modular agent-based backend design

- PDF & text document question answering

- Smart fallback to web search

- SQLite-powered meeting scheduler queries

- FastAPI Swagger UI for easy API testing

- Beginner-friendly project structure

---

### **Project Structure**

```md
agentic-ai-backend/
│
├── main.py                   # FastAPI entry point
├── agents/
│   ├── document_agent.py     # Document Q&A logic
│   ├── db_agent.py           # Database query agent
│   ├── weather_agent.py      # Weather agent (optional)
│   └── __init__.py
│
├── database/
│   └── meetings.db           # SQLite database
│
├── requirements.txt
├── .gitignore
└── README.md 
```

---

### **Installation & Setup**

 **Step 1: Clone the Repository**
 
```git clone https://github.com/<your-username>/agentic-ai-backend.git```
```cd agentic-ai-backend ```

 **Step 2: Create Virtual Environment**
 
``` python -m venv venv ```

 **Step 3: Activate Virtual Environment**

  **Windows**

``` venv\Scripts\activate ```

  **macOS / Linux**

  ```source venv/bin/activate```

You should see:

```(venv) C:\Users\...```

**Step 4: Install Dependencies**

```pip install -r requirements.txt```

If requirements.txt is not present, install manually:

```pip install fastapi uvicorn python-multipart PyPDF2 duckduckgo-search```

---

### **Running the Application**

Start the FastAPI server:

```uvicorn main:app --reload```

If successful, you’ll see:

```Uvicorn running on http://127.0.0.1:8000```

---

### **API Usage**

Open your browser and go to:

```http://127.0.0.1:8000/docs```

Using **Swagger UI**, you can:

- Upload documents

- Ask questions

- Query meetings (today / tomorrow)

- Test all API endpoints interactively

---

### **Agents Description**

**📄 Document Agent**

- Reads PDF or text files

- Matches user questions against document content

- Falls back to web search if answer is not found

**📅 Database Agent**

- Uses SQLite

- Supports queries like:

  -- “Meetings today”

  -- “Meetings tomorrow”

  -- “All meetings”

---

### **Learning Outcomes**

- Understanding agent-based system design

- Building REST APIs using FastAPI

- Working with SQLite databases

- Handling file uploads and parsing PDFs

- Practical Git & GitHub workflow

---

### **Future Enhancements**

- Semantic search using embeddings

- Authentication and user roles

- Frontend integration

- Cloud deployment

- Advanced agent coordination

---

### **Author**

#### Kaviya
**Computer Science Engineering Student**

🚀 Passionate about **Frontend & Backend Development**, **AI-powered systems**, and creating **practical, real-world solutions** 💙

---

### **Support**

If you found this project useful, **please give it a star ⭐**
It really helps and motivates future improvements!
