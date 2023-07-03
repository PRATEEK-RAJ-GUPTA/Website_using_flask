from flask import Flask

#creating an object of class flask
app=Flask(__name__)

#route->part of url after domain name

@app.route('/')#empy route
def hello_world():
  return "Hello World!"

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)#everytime we make a chane it will change automatically

