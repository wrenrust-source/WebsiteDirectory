from drafter import Drafter, Page
import datetime

# Initialize Drafter app
app = Drafter(__name__)

# Basic in-memory task list
tasks = [
    {"text": "Finish homework", "due": "11/08/25"},
    {"text": "Read 3 chapters", "due": "11/09/25"},
    {"text": "Plan next week", "due": "11/10/25"},
]

@app.route("/")
def home():
    """Main page route — renders index.html with dynamic data."""

    today = datetime.date.today().strftime("%m/%d/%y")

    # Build HTML for task rows dynamically
    todo_rows = "\n".join([
        f"""
        <div class="todo-row">
            <div style="width:36px;">
                <input type="checkbox" />
            </div>
            <div class="todo-text">{t['text']}</div>
            <div style="min-width:110px;display:flex;gap:8px;align-items:center;justify-content:flex-end;">
                <div class="small-pill">{t['due']}</div>
                <button class="toggle-btn">view</button>
            </div>
        </div>
        """ for t in tasks
    ])

    # Render template and inject variables
    return Page("templates/index.html", {
        "today": today,
        "todo_rows": todo_rows
    })

if __name__ == "__main__":
    app.run()
