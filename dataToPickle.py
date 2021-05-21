import sys

sys.path.append('../tech-team-database')
from DatabaseSQLOperations import TpSQL

sys.path.append('../common/gdrive')
from GoogleDriveOperations import GDrive

import pickle

eventData = {}
tpSQL = TpSQL()
# print(tpSQL.listTableNames())
df = tpSQL.getTable('event_informationall_client')


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
    print(school)
    print(eventData[school]["tree_types"])

# dump dictionary into pickle file
with open('eventDataDict.pkl', 'wb') as handle:
    pickle.dump(eventData, handle, protocol=pickle.HIGHEST_PROTOCOL)

