# Flask Microservices

## Tasks Overview
Python Flask web application (Criteria Pf1-Pf3).

### Included Files
* **Pf3 - `Pf3_custom_app.py`**: The application logic.
* **`templates/index.html`**: The HTML visual template.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is Flask?
Flask is a **Micro-framework** for Python. It allows you to build web servers quickly. It is "Micro" because it keeps the core simple but extensible.

### 2. What is a Decorator (`@app.route`)?
In Python, the `@` symbol is a decorator.
* `@app.route("/")`: This tells Flask "When a user visits the root URL (`/`), run the function immediately below this line."
* It maps a URL to a Python Function.

### 3. What is Jinja2 (Templating)?
We don't just return static HTML. We use `render_template`.
* In HTML: `{{ current_time }}` is a placeholder.
* In Python: We pass the variable `current_time=now`.
* **Jinja2** is the engine that replaces the placeholder with the actual time before sending it to the browser.