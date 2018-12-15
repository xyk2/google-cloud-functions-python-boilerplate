# Your main function here
def hello_world(request):
	return 'Hello world!'


# Get environmental variables at runtime
def get_env_var(var):
    return os.environ.get(var, 'Specified environment variable is not set.')


# When running locally (python main.py), a local Flask server will run passing `request` to your hello_world()
if __name__ == "__main__":
	from flask import Flask, request
	app = Flask(__name__)

	@app.route('/', defaults={'path': ''})
	@app.route('/<path:path>')
	def index(path):
		return hello_world(request)

	app.run('127.0.0.1', 5000, debug=True)

