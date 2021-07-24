import sys
sys.path.append('../tech-team-database')
from DatabaseSQLOperations import TpSQL
sys.path.append('../common/gdrive')
from GoogleDriveOperations import GDrive
import pickle
import pandas as pd


# get school data from dict from pickle file
with open('eventDataDict.pkl', 'rb') as handle:
    eventData = pickle.load(handle)["Knight High School"]

print(eventData)
drive = GDrive()
treeImages = drive.getAllFiles("12U52jiXbTfUNbANiWXLZWeJLSCvzWfvk") # Get all tree images in a dict
print(treeImages)

#https://drive.google.com/uc?export=view&id=