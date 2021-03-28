from flask import Flask, render_template, url_for, redirect

# example dictionary of event data for testing
from testData import eventData


# EB looks for an 'application' callable by default.
application = Flask(__name__)

# redirect to Tree-Plenish site if no school input
@application.route('/')
def index():
    return redirect('https://www.tree-plenish.org/')

@application.route('/<string:schoolName>')
def schoolPage(schoolName):
    # Use schoolName or some other event identifier to get event data from database

    # Then send in eventData as event to webpage
    return render_template('index.html', event=eventData)



# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    application.run()
