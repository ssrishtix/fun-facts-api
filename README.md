# 🧠 Fun Facts API

Welcome to the **Fun Facts API** — a beginner-friendly project built using **FastAPI** that serves random and quirky facts through a simple REST API.

Perfect for learning how APIs work, practicing backend development, or just having fun with interesting trivia! ✨

---

## 🚀 Features

- `GET /fact` – Get a single random fun fact  
- `GET /facts` – Get all available fun facts  
- `POST /facts` – Submit your own fun fact with an optional category  

---

## 🛠️ Tech Stack

- **Python 3.13**
- **FastAPI** – Web framework
- **Uvicorn** – ASGI server for FastAPI

---

## 💻 Getting Started

### 🔗 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/fun-facts-api.git
cd fun-facts-api
📦 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the API Server
bash
Copy
Edit
uvicorn main:app --reload
Open your browser and visit:

Swagger Docs → http://127.0.0.1:8000/docs

Random Fact → http://127.0.0.1:8000/fact

📬 Example POST Request
json
Copy
Edit
{
  "text": "Honey never spoils. Archaeologists have found 3,000-year-old honey that’s still edible.",
  "category": "science"
}
🗂️ Project Structure
kotlin
Copy
Edit
fun-facts-api/
├── main.py           # FastAPI routes and endpoints
├── facts.py          # In-memory data and logic
├── requirements.txt  # Python dependencies
├── README.md         # Project overview (this file)
🚧 Future Improvements
 Filter facts by category (/facts?category=science)

 Store facts in a real database (e.g., PostgreSQL or SQLite)

 Add authentication for posting facts

 Deploy the API to Render or Railway

🙋‍♀️ About Me
Hi! I'm Your Name, a 3rd-year Computer Science student passionate about backend development, AI/ML, and building projects that make learning fun. This mini API helped me learn how to:

Use FastAPI

Build and test REST APIs

Handle version control with Git & GitHub

🌟 Show Some Love
If you liked this project, consider ⭐ starring the repo and sharing it with friends!

yaml
Copy
Edit

---

### ✅ Replace:
- `YOUR_USERNAME` with your GitHub username  
- `Your Name` with your actual name

Then:

```bash
git add README.md
git commit -m "Add final polished README"
git push
