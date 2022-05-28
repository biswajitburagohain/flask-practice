import os
from flask import Flask

# Instead of creating a Flask instance globally, 
# we will create it inside a function. 
# This function is known as the application factory.

# __init__.py: The __init__.py file makes Python treat directories containing it as modules. 
# Furthermore, this is the first file to be loaded in a module, 
# so you can use it to execute code that you want to run each time a module is loaded, 
# or specify the submodules to be exported.

def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
