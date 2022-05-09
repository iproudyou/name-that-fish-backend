from flask import Flask
from flask.wrappers import Response
from flask_cors import CORS

def create_app():
  app = Flask(__name__)
  
  CORS(app)

  @app.route('/', methods=['GET', 'POST'])
  def handle_health_check():
    """Return response 200 for successful health check"""
    return Response(status=200)

  return app

app = create_app()


from fish import routes
