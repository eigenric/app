from flask.ext.script import Manager
from app import *
from views import *

manager = Manager(app)

if __name__ == "__main__":
	manager.run()
