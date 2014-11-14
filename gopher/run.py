import config
# config[DATABASE_URL] = 'sqlite:///gopher.db'

from application import app
app.run(port=16000)

