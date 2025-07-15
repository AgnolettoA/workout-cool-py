# Hosting the Python Port on PythonAnywhere

This repository includes a minimal Flask app under `python_port/`.
You can deploy it on [PythonAnywhere](https://www.pythonanywhere.com/) with the following steps:

1. Sign up and create a new **Web App**.
2. Choose **Flask** and the latest Python version available.
3. Upload the repository or clone it using Git.
4. Set the **WSGI file** to point to `python_port/app.py`.
5. Install dependencies in a virtualenv:
   ```bash
   pip install -r python_port/requirements.txt
   ```
6. Reload the web app in the PythonAnywhere dashboard.

The Flask app will serve a placeholder landing page and static files from the `public/` directory.
