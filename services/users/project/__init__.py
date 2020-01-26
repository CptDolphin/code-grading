from flask import Flask, jsonify
import sys

app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
  return jsonify({
    'status': 'success',
    'message': 'pong!'
  })

print(app.config, file=sys.stderr)
