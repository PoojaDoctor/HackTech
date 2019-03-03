from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	cursor = connection.cursor
	location = request.args.get()
    return 'Hello, World!'

if __name__ == "__main__":
	app.run()