"""
Very simple 'HelloClass' & 'NameClass' Application Programming Interface:
    (returns a greeting &/or returns name provided by the user)
        built using Flask Flask-RESTX and Swagger UI.
"""

# TODO: Get simple app running then testing.
#   focus on dependencies, flask-restX
#   could try using '$ poetry init' in a poetry_branch?
#   develop can seek to catch up with openvar version of application


# Import modules
from flask import Flask, make_response, request
from flask_restx import Api, Resource, reqparse, fields, abort
from dicttoxml import dicttoxml



# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
# Most tutorials define application as "app", but I have had issues with this when it comes to deployment,
# so application is recommended
application = Flask(__name__)


print(f'Application type is {type(application)} with methods and properites [dir(application)]:')
for i in dir(application):
    if  i == "config":
        print("We've got a config method: ", i)

for j in dir(application.config):
    print(j)


# Define the API as api
api = Api(app = application)

# Create a RequestParser object to identify specific content-type requests in HTTP URLs
# The requestparser allows us to specify arguements passed via a URL, in this case, ....?content-type=application/json
parser = reqparse.RequestParser()
parser.add_argument('content-type',
                    type=str,
                    help='Accepted:\n- application/json\n- text/xml')




# Define a name-space to be read Swagger UI which is built in to Flask-RESTPlus
# The first variable is the path of the namespace the second variable describes the space
hello_space = api.namespace('hello', description='Simple API that returns a greeting')
@hello_space.route("/")

class HelloClass(Resource):

    # Add documentation about the parser
    @api.doc(parser=parser)
    def get(self):

        # Collect Arguements
        args = parser.parse_args()

        # Overides the default response route so that the standard HTML URL can return any specified format
        if args['content-type'] == 'application/json':
            # example: http://127.0.0.1:5000/name/name/bob?content-type=application/json
            return json({
                "greeting" : "Hello World"
            },
                200, None)
        # example: http://127.0.0.1:5000/name/name/bob?content-type=text/xml
        elif args['content-type'] == 'text/xml':
            return xml({
                 "greeting" : "Hello World"
            },
                200, None)
        else:
            # Return the api default output
            return {
                 "greeting" : "Hello World"
            }

name_space = api.namespace('name', description='Return a name provided by the user')
@name_space.route("/<string:name>")
class NameClass(Resource):


    # Add documentation about the parser
    @api.doc(parser=parser)
    def get(self, name):

        # Collect Arguements
        args = parser.parse_args()

        # Overides the default response route so that the standard HTML URL can return any specified format
        if args['content-type'] == 'application/json':
            # example: http://127.0.0.1:5000/name/name/bob?content-type=application/json
            return json({
                "My name is" : name
            },
                200, None)
        # example: http://127.0.0.1:5000/name/name/bob?content-type=text/xml
        elif args['content-type'] == 'text/xml':
            return xml({
                "My name is": name
            },
                200, None)
        else:
            # Return the api default output
            return {
                "My name is" : name
            }


"""
Representations
 - Adds a response-type into the "Response content type" drop-down menu displayed in Swagger
 - When selected, the APP will return the correct response-header and content type
 - The default for flask-restplus is aspplication/json
"""
# Add additional representations using the @api.representation decorator
# Requires the module make_response from flask and dicttoxml
@api.representation('text/xml')
def xml(data, code, headers):
    data = dicttoxml(data)
    resp = make_response(data, code)
    resp.headers['Content-Type'] = 'text/xml'
    return resp

@api.representation('application/json')
def json(data, code, headers):
    resp = make_response(data, code)
    resp.headers['Content-Type'] = 'application/json'
    return resp




# Allows app to be run in debug mode
if __name__ == '__main__':
    application.debug = True # Enable debugging mode
    application.run(host="127.0.0.1", port=5000) # Specify a host and port fot the app