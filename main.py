from flask import Flask, render_template

app = Flask(__name__)

# Sample data - replace with your own dynamic data source
posts = [
    {'author': 'John Doe', 'title': 'Blog Post 1', 'content': 'First post content', 'date_posted': 'June 1, 2023'},
    {'author': 'Jane Smith', 'title': 'Blog Post 2', 'content': 'Second post content', 'date_posted': 'June 2, 2023'}
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
