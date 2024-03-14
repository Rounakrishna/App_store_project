from flask import Flask, render_template, jsonify,url_for

app = Flask(__name__)

# Mock data for apps and categories
apps = [
    {
        'id': 1,
        'name': 'App 1',
        'description': 'This is a description for App 1',
        'icon': 'https://via.placeholder.com/100x100'
    },
    {
        'id': 2,
        'name': 'App 2',
        'description': 'This is a description for App 2',
        'icon': 'https://via.placeholder.com/100x100'
    },
    {
        'id': 3,
        'name': 'App 3',
        'description': 'This is a description for App 3',
        'icon': 'https://via.placeholder.com/100x100'
    },
    {
        'id': 4,
        'name': 'App 4',
        'description': 'This is a description for App 4',
        'icon': 'https://via.placeholder.com/100x100'
    },
    {
        'id': 5,
        'name': 'App 5',
        'description': 'This is a description for App 5',
        'icon': 'https://via.placeholder.com/100x100'
    }
    # Add more app data here
]

categories = [
    {
        'id': 1,
        'name': 'Category 1',
        'icon': 'https://via.placeholder.com/100x100'
    },
    {
        'id': 2,
        'name': 'Category 2',
        'icon': 'https://via.placeholder.com/100x100'
    },
    # Add more category data here
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apps')
def get_apps():
    return jsonify(apps)

@app.route('/categories')
def get_categories():
    return jsonify(categories)


app.run(debug=True)