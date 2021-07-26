# NOTE: This script is not updated to the new database setup yet.

import sys
import importlib
from pathlib import Path
import pickle

import datetime
from dateutil.relativedelta import relativedelta

# Add parent directory to PYTHONPATH to be able to find package.
if __name__ == '__main__' and __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError:
        pass

    __package__ = '.'.join(parent.parts[len(top.parts):])
    importlib.import_module(__package__)

from tech_team_database.dependencies.DatabaseSQLOperations import TpSQL
from common.gdrive.GoogleDriveOperations import GDrive

eventData = {}
tpSQL = TpSQL()
print(tpSQL.listTableNames())
df = tpSQL.getTable('event')
print(df)


# from old database setup:

eventData = df.set_index('name').T.to_dict()
# make any string lists (list of names, trees) into lists
# would be better to have them already as lists in the future, more consistent and reliable
# since some names are split by & or spaces
for school in eventData:
    eventData[school]["host_names"] = eventData[school]["host_names"].split(', ')
    eventData[school]["tree_types"] = eventData[school]["tree_types"].split(', ')


# Getting tree images for each tree
drive = GDrive()
treeImages = drive.getAllFiles("12U52jiXbTfUNbANiWXLZWeJLSCvzWfvk") # Get all tree images as a dict
treeImages = {k.lower(): v for k, v in treeImages.items()}
print(treeImages)

for school in eventData:
    trees = eventData[school]["tree_types"]
    for i in range(len(trees)):
        trees[i] = {"name": trees[i]}
        try:
            trees[i]["image"] =  "https://drive.google.com/uc?export=view&id=" + treeImages[trees[i]["name"].lower() + ".jpg"]
        except: 
            print("No image for ", trees[i]["name"])
    # Calculate event date - 1 month to get order deadline
    # Assumes event_date is always stored as '%m/%d/%Y' in database!
    if not 'order_deadline' in eventData[school]:
        date = datetime.datetime.strptime(eventData[school]['event_date'], '%m/%d/%Y').date()
        date_minus_month =  date - relativedelta(months=1)
        eventData[school]['order_deadline'] = date_minus_month.strftime('%B %d, %Y').replace(" 0", " ")
        eventData[school]['event_date'] = date.strftime('%B %d, %Y').replace(" 0", " ")
    # print(school)
    # print(eventData[school]["tree_types"])

# dump dictionary into pickle file
with open('eventDataDict.pkl', 'wb') as handle:
    pickle.dump(eventData, handle, protocol=pickle.HIGHEST_PROTOCOL)

