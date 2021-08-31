# TODO: check donate tree boolean translating correctly,

import sys
import importlib
import pandas as pd
from pathlib import Path
import pickle

import datetime
from dateutil.relativedelta import relativedelta

# Add parent directory to PYTHONPATH to be able to find package.
if __name__ == '__main__' and __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[1]

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
df = pd.merge(tpSQL.getTable('school'), tpSQL.getTable('event'), on="schoolid")
# print(df)

# CHECK NO SLASHES IN SCHOOL NAME
df['name'] = df['name'].apply(lambda name: name.replace('/', '-'))

# school names will always be unique?
eventData = df.set_index('name').T.to_dict()

school = tpSQL.getTable('school')
print(school)

# print(1003 in list(df['schoolid']))
# print(1003 in list(school['schoolid']))
# print(school.loc[school['schoolid'] == 1003])
# print(list(df.loc[df['schoolid'] == 1003].values))

# # print(eventData)

# Getting all tree images from drive
drive = GDrive()
treeImages = drive.getAllFiles("12U52jiXbTfUNbANiWXLZWeJLSCvzWfvk") # Get all tree images as a dict
treeImages = {k.lower(): v for k, v in treeImages.items()}
print(treeImages)


hostData = tpSQL.getTable('event_hosts')
# print(hostData)
for school in eventData:

    schoolData = eventData[school]
    print('price', schoolData['price'])

    # Get list of event hosts and add to eventData
    if schoolData['schoolid'] in list(hostData['schoolid']):
        # print(school)
        schoolData['hosts'] = hostData.loc[hostData['schoolid'] == schoolData['schoolid']].to_dict('records')
        # print(schoolData['hosts'])
    
    # Also reorganize tree species (species_one, species_two, etc.) into list of trees
    # print(schoolData['species_one'])
    # print(schoolData['species_two'])
    # print(schoolData['species_three'])
    schoolData['trees'] = []
    schoolData['trees'].append({'name': schoolData['species_one']})
    schoolData['trees'].append({'name': schoolData['species_two']})
    schoolData['trees'].append({'name': schoolData['species_three']})
    print(schoolData['trees'])
  
    # Get image for each tree (if available)
    trees = eventData[school]["trees"]
    for i in range(len(trees)):
        try:
            trees[i]["image"] =  "https://drive.google.com/uc?export=view&id=" + treeImages[trees[i]["name"].lower() + ".jpg"]
        except: 
            print("No image for", trees[i]["name"], "from school:", school)

    # Calculate event date - 1 month to get order deadline
    # Assumes event_date is always stored as '%Y-%m-%d' in database!
    try:
        date = datetime.datetime.strptime(eventData[school]['date'], '%Y-%m-%d').date()
        date_minus_month =  date - relativedelta(months=1)
        eventData[school]['order_deadline'] = date_minus_month.strftime('%B %d, %Y').replace(" 0", " ")
        eventData[school]['date'] = date.strftime('%B %d, %Y').replace(" 0", " ")
        print("Order deadline success for school:", school)
    except:
        print("Order deadline could not be calculated for date: ", eventData[school]['date'], "from school:", school)
    # print(school)
    # print(eventData[school]["tree_types"]) 

# dump dictionary into pickle file
with open('eventDataDict.pkl', 'wb') as handle:
    pickle.dump(eventData, handle, protocol=pickle.HIGHEST_PROTOCOL)

