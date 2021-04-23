import sys
sys.path.append('../tech-team-database')
from DatabaseSQLOperations import TpSQL
import pickle

eventData = {}
tpSQL = TpSQL()
# print(tpSQL.listTableNames())
df = tpSQL.getTable('event_informationall_client')


eventData = df.set_index('name').T.to_dict()
# make any string lists (list of names, trees) into lists
for school in eventData:
    eventData[school]["host_names"] = eventData[school]["host_names"].split(', ')
    eventData[school]["tree_types"] = eventData[school]["tree_types"].split(', ')

# dump dictionary into pickle file
with open('eventDataDict.pkl', 'wb') as handle:
    pickle.dump(eventData, handle, protocol=pickle.HIGHEST_PROTOCOL)

