from flask import Flask, request, jsonify, render_template
import playfab.PlayFabClientAPI as PlayFabClient
import playfab.PlayFabSettings as PlayFabSettings

app = Flask(__name__)

# Set PlayFab title ID and secret key
PlayFabSettings.TitleId = "Avalon"
PlayFabSettings.DeveloperSecretKey = "4685A"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login_request = {
        "TitleId": PlayFabSettings.TitleId,
        "Email": data['email'],
        "Password": data['password']
    }
    result = PlayFabClient.LoginWithEmailAddress(login_request)
    if 'data' in result and result['data']:
        return jsonify(result['data']), 200
    else:
        error_message = result.get('errorMessage', 'Unknown error')
        return jsonify({"error": error_message}), 400

if __name__ == '__main__':
    app.run(debug=True)
