# event-pages
Automating Individual Event Pages.

## Current Progress
- General site content/structure is pretty much finished
- Tree images are obtained from the Google Drive folder (by tree name)
- Loading/using event data from database is in progress

## Deployment
- Github actions is configured to automatically deploy the Flask app on Elastic Beanstalk whenever a new change is pushed to the main branch. See workflow/deployment progress in Github "Actions" tab. 
- TODO: Add tests to run during workflow to prevent deployment if site has problems.
- Demo deployed [here](http://test-environment.eba-s4xs6euy.us-east-1.elasticbeanstalk.com/Timber%20Woods%20High%20School)
