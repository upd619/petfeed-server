import pusher
from flask import Flask
from flask import request
from flask import jsonify
from flask import copy_current_request_context
 # ERROR RESPONSES

  #THIS CONTAINS THE FLASK SERVER


app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def home():
	response={
	'status':'online',
	'connection':'local'
	}
	if request.method=='GET' or request.method=='POST':
		return jsonify(response)




if __name__=='__main__':
	app.run()

