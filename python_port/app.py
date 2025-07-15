from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return 'WorkoutCool Python port placeholder'

@app.route('/public/<path:filename>')
def serve_public(filename):
    return send_from_directory('../public', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
