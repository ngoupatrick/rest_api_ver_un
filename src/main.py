from src import api, app  
from src.resources import PersonneResource, UserResource


api.add_resource(PersonneResource,
                 '/personnes/',
                 '/personnes/<string:eid>')

api.add_resource(UserResource,
                 '/users/',
                 '/users/<string:eid>')

#source /home/patrick/Bureau/python/any_prj/envs/env_rest/bin/activate
#sh run.sh OR sh run.sh gunicorn OR sh run.sh default

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
