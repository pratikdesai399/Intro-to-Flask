from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'

    db.init_app(app)

    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    return app

# @app.route('/')
# def index():
#     return render_template('index.html', message='Hello World')

# @app.route('/post_method', methods=['POST'])
# def hello_post():
#     return 'POST'

# @app.route('/greet/<name>')
# def hello(name):
#     return f"Hello {name}" 


# @app.route('/handle_url_params')
# def handle_params():
#     return str(request.args)


# @app.route('/set_data')
# def set_data():
#     session['name'] = 'Pratik'
#     session['other'] = 'Hello World'

#     return render_template('index.html', message='Session SET')

# @app.route('/get_data')
# def get_data():
#     if 'name' in session.keys() and 'other' in session.keys():
#         name = session['name']
#         other = session['other'] 

#         return render_template('index.html', message=f'Name: {name} Other: {other}')
#     else:
#        return render_template('index.html', message='No session found') 


# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5555, debug=True)