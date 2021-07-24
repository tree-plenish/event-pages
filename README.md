# event-pages
Automating Individual Event Pages.

## Current Progress
- General site content/structure is pretty much finished
- Loading/using event data from database is set up; script to save dict of all school event data as pickle file, and application.py gets school event data from pickle file and sends to rendered HTML page. Event page can currently show school name, event date, state, tree names, etc. based on school name in URL.
    - Some fields are empty or inconsistent (names separated by 'and', '&', or ',')
    - Pictures of trees: currently getting google drive image links from tree names in dataToPickle script. 
    - Tree more info links?
    - Team member pictures, emails, bios, goal message
    - city?
    - Jinja html template embeds video from youtube video link or google drive video link (when opened in its own tab)

## Deployment
- Github actions is configured to automatically deploy the Flask app on Elastic Beanstalk whenever a new change is pushed to the main branch.
- Demo [here](http://test-environment.eba-s4xs6euy.us-east-1.elasticbeanstalk.com/Timber%20Woods%20High%20School)
