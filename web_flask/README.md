## Web Flask
This Directory contains the files for tasks of 0x04. AirBnB clone - Web framework

## Learning Objects
# General
- What is Web FrameWork
- How to build a Web Framework with Flask
- How to define routes in Flask
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by Using a Template
- How to create a dynamic template(loops, conditions...)
- How to display in HTML data from a MySQL database

# Tasks
- 0.Hello Flask!:
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition

file: 0-hello_route.py, __init__.py

- 1.HBNB
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition
file: 1-hbnb_route.py

- 2.C is fun!
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
file: 2-c_route.py

- 3.Python is cool!
Write a script that starts a Flask web application
    Your web application must be listening on 0.0.0.0 port 5000
    Routes:
            /: display "Hello HBNB!"
            /hbnb: display "HBNB"
            /c/<text>:display "C",followed by the value of the text variable(replace underscore _ symbols with a space )
            /python/<text>:display "Python",followed by the value of the text variable(replace underscore _ symbols with a space )
                The default value of text is "is cool"
            You must use the option strict_slashes=False in your route definition
