from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return f'index page'

@app.route("/")
def hello():
    return f'hello world'

@app.route('/user/<user_name>')
def show_user_profile(user_name):
    return f'User, {user_name}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'post {post_id}'

if __name__ == "__main__":
    app.run()