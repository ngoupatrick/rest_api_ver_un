from main import create_app
#from main.routes import load_routes  # type:ignore
from main.resources import PersonneResource,UserResource

app, db, api, bcrypt, ma = create_app()
#load_routes()
api.add_resource(PersonneResource,
                 '/personnes/',
                 '/personnes/<string:eid>')

api.add_resource(UserResource,
                 '/users/',
                 '/users/<string:eid>')
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
