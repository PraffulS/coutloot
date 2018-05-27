from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS
import hashlib
app = Flask(__name__)
CORS(app)
app.config['MONGO_DBNAME'] = 'mydb1'
app.config['MONGO_URI'] = 'mongodb://prafful54:prafful54@ds237669.mlab.com:37669/mydb1'

mongo = PyMongo(app)
@app.route('/register', methods=['POST'])
def register():
  star = mongo.db.user
  username = request.json['username']
  password = request.json['password']
  emailid = request.json['emailid']
  m = hashlib.md5()
  m.update(password.encode())
  password = m.hexdigest()
  #star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'username': username })
  if(new_star):
      output = 'username already exists'
  else:
      '''star_id = star.insert({'name': name, 'distance': distance})
      new_star = star.find_one({'_id': star_id })'''
      output = {'username' :username, 'password' : password, 'emailid': emailid}
      star.insert(output)
      output = 'registration successful'
  return jsonify({'result' : output})


@app.route('/login', methods=['POST'])
def login():
  star = mongo.db.user
  username = request.json['username']
  password = request.json['password']
  m = hashlib.md5()
  m.update(password.encode())
  password = m.hexdigest()
  #star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'username': username })
  if(new_star):
    if password==new_star['password']:
      output = 'login successful'
    else:
      output = 'invalid password'
  else:
      '''star_id = star.insert({'name': name, 'distance': distance})
      new_star = star.find_one({'_id': star_id })
      output = {'name' : new_star['name'], 'distance' : new_star['distance']}'''
      output = "login unsuccessful"
  return jsonify({'result' : output})


      
  
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
