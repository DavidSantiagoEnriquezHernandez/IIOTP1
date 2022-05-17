from flask import Flask, request

app = Flask ('__main__')

device = {
"code" : "121244",
"descrip": "Sensor. humedad",
"value" : 60
}

@app.route('/devices', methods=['GET'])
def go_home():
    return device
    #save an user
@app.route('/users' , methods=['POST'])
def save_user():
        user = request.json
        print(user)
        return user

#save a device
@app.route('/devices' , methods=['POST'])
def save_device():
    device = request.json
    return device

if __name__ == '__main__':
        app.run(debug= True, port=5000)
