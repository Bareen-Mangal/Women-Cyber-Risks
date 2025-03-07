from flask import Flask, render_template, request
app = Flask(__name__)

# In-memory dictionary to store visits:
# Key = username, Value = number of times "checked"
visitors_count = {}

@app.route('/', methods=['GET'])
def index():
    """
    Renders the main page (index.html) with the check form.
    """
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    """
    Handles the form submission from index.html.
    Increments the visitor's count and then displays the visitors list.
    """
    username = request.form.get('username')
    if not username:
        # If no username provided, just return index or handle error
        return render_template('index.html', error="Please enter a username.")

    # Increment the visit count for the given username
    visitors_count[username] = visitors_count.get(username, 0) + 1

    # Sort visitors by their visit count (descending)
    sorted_visitors = sorted(visitors_count.items(), key=lambda x: x[1], reverse=True)

    # Render a new template that displays the visitors table
    return render_template('check.html', visitors=sorted_visitors, current_user=username)

if __name__ == '__main__':
    app.run(debug=True)
