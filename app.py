from flask import Flask

app = Flask(__name__)
app.config.from_envvar('DEFAULT_CONFIG')
print(app.config)

@app.route('/first_hello', methods=['POST'])
def router():
    return b"OK"

if __name__=="__main__":
    app.run('localhost')

