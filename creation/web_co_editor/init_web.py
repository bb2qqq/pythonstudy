from flask import Flask
app = Flask(__name__)

@app.route("/")
def guide():
    return "Welcome to x-lab, I'll do something here.<br/>\n\
            You can append a-z after main domain to go to different child sites<br/>\n\
            main_domian/a       web_co_editor"

@app.route("/a")
def web_co_editor():                    # Return an editor or log-in here.
    return "web_co_editor allows you to create an artful text with your friends"

if __name__ == "__main__":
    app.run()
