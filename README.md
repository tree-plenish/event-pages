# event-pages
Automating Individual Event Pages.

## Current Progress
- General site content/structure is pretty much finished
- Flask app deployment details figured out (site can be easily deployed once finished)
- Loading/using event data from database is set up; script to save dict of all school event data as pickle file, and application.py gets school event data from pickle file and sends to rendered HTML page. Event page can currently show school name, event date, state, tree names, etc. based on school name in URL.
    - Some fields are empty or inconsistent (names separated by 'and', '&', or ',')
    - Pictures of trees: add to tree_species table?
    - Team member pictures, bios, goal message
