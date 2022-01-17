try:
    from subprocess import call
    import subprocess
    import ast
    import json
    import flask
    from flask import Flask
    from flask_restful import Resource, Api
except Exception as e:
    print("Some  Modules are missing : {} ".format(e))
 
app = Flask(__name__)
api = Api(app)
 
 
class HealthCheck(Resource):
    def get(self):
        result = subprocess.run('docker inspect mydocker_nginx',shell=True, check=True, stdout=subprocess.PIPE)
        result = result.stdout
        result = result.decode("utf-8")
        result = json.loads(result)
        return json.dumps(result)
 
api.add_resource(HealthCheck, '/foo')
 
 
if __name__ == '__main__':
    app.run(host="0.0.0.0")
