from flask import Flask, request
##libraries used

app = Flask('__main__')

'''
CODE FOR TESTING, ASSUMING THAT COMES FROM THE DB
'''
device = {
    "code":"116233",
    "descrip":"Temp. Sensor",
    "value":67
}


@app.route('/devices', methods=['GET'])
def go_home():
    return device

#Save an user
@app.route('/users', methods=['POST'])
def save_user():
    user = request.json
    print(user)
    return user

#Save a device
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print (device)
    return device, 201


if __name__ == '__main__':
    app.run(debug=True, port=5000)
