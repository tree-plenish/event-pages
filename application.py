from flask import Flask, render_template, url_for, redirect
import pickle

# example dictionary of event data for testing
from testData import data

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# redirect to Tree-Plenish site if no school input
@application.route('/')
def index():
    return redirect('https://www.tree-plenish.org/')

@application.route('/<string:schoolName>')
def schoolPage(schoolName):
    # Use schoolName or some other event identifier to get event data from database
    # Try getting school info
    try:
        
        if schoolName != "Timber Woods High School" and schoolName != "Timber Woods High School2": # just for demo
            raise Exception
            
        # get school data from dict from pickle file
        # with open('eventDataDict.pkl', 'rb') as handle:
        #     eventData = pickle.load(handle)[schoolName]
        eventData = data[schoolName]
        schoolName = "Timber Woods High School"
        # Then send in as event to webpage
        return render_template('index.html', event=eventData, school=schoolName)
    except Exception as e:
        print(e) 
        # redirect to error page if any error with loading data or school not found
        print('School not found')
        return render_template('error.html', school=schoolName)
        
        

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    application.run()
