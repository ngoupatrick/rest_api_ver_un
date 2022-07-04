from src.main import create_app

app, db, bcrypt, ma = create_app()

#source /home/patrick/Bureau/python/any_prj/envs/env_rest/bin/activate
#source run.sh
#sh run.sh OR sh run.sh gunicorn OR sh run.sh default OR sh run.sh wsgi
