# from pip._internal import main as pipmain

# pipmain(['install', 'Flask'])

# print('All Done')
# exit(0)

from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/') #route decorator for server to run this html code then give to browser
def index():
	return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>') #wildcard to make sure everything after path is captured
def static_assets(path: str):
	return send_from_directory('static', path)

#put in repository then host on github pages is usedfor hosting pages
#unit, integration, end-to-end testing
print('Breakpoint me!')

if __name__ == '__main__':
	app.run('0.0.0.0', 5000, True)
            #host number, port, reruns the files automatically