# event-pages
Automating Individual Event Pages.

## Current Progress
- General site content/structure is pretty much finished
- Tree images are obtained from the Google Drive folder (by tree name)
- Loading/using event data from database is mostly done. Just need to test/tune.
    - `dataToPickle.py` is the server script that fetches data from the database, processes it, and dumps it into a pickle file for `application.py` to send in the relevant data to populate the HTML template based on the school name appended to the URL. 

## Deployment
- Github actions is configured to automatically deploy the Flask app on Elastic Beanstalk whenever a new change is pushed to the main branch. See workflow/deployment progress in Github "Actions" tab. 
- TODO: Add tests to run during workflow to prevent deployment if site has problems.
- *Current state of this repo automatically deployed [here](http://test-environment.eba-s4xs6euy.us-east-1.elasticbeanstalk.com/Timber%20Woods%20High%20School)* **(temporarily terminated environment while site is being connected to test data)**