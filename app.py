from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_method', methods=['POST'])
def hello_post():
    return 'POST'

@app.route('/greet/<name>')
def hello(name):
    return f"Hello {name}" 


@app.route('/handle_url_params')
def handle_params():
    return str(request.args)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)