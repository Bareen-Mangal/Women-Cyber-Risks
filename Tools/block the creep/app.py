from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Form submission to check for stalkers
@app.route('/check', methods=['POST'])
def check_stalker():
    username = request.form.get('username')

    # This is where we'll later integrate the API call
    message = f"Checking social media activity for user: {username}"

    return render_template('result.html', message=message)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
