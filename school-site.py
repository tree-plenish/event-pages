from flask import Flask, render_template, url_for, redirect

# example dictionary of event data for testing
from testData import eventData


app = Flask(__name__)

# redirect to Tree-Plenish site if no school input
@app.route('/')
def index():
    return redirect('https://www.tree-plenish.org/')

@app.route('/<string:schoolName>')
def schoolPage(schoolName):
    # Use schoolName or some other event identifier to get event data from database

    # Then send in eventData as event to webpage
    return render_template('index.html', event=eventData)

if __name__ == '__main__':
    app.run(debug=True)
