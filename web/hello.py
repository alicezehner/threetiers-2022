# import package flask
from flask import Flask

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 

# create flask app
app = Flask(__name__)

#create root route
@app.route('/')
def hello_world():
    return 'ALICE!'

#start server
if __name__ == '__main__': 
    app.run(debug =True, port=3000)