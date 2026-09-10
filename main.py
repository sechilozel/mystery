from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template('index.html')


@app.route("/click")
def click():
    return render_template('click.html')


if __name__ == "__main__":
    app.run(debug=True)
