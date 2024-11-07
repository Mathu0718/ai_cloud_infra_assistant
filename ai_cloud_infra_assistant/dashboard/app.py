from flask import Flask, render_template
from cloud_integration.vultr_api import list_instances

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return "Dashboard route works!"
if __name__ == '__main__':
    app.run(debug=True)
