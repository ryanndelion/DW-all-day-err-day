#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:49:26 2017

@author: hoonqt
"""

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    binA = []
    binB = []
    binC = []
    binD = []
    binE = []
    binF = []
    binG = []
    binH = []
    binI = []
    megalist = []
    averagelist = []
  
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1QQA7KBKwlvOq7grMQGzqJOPykbH1MyvbpXFwagiiQfs'
    rangeName = 'Formresponse!B2:J'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            binA.append(str(row[0]))
            binB.append(str(row[1]))
            binC.append(str(row[2]))
            binD.append(str(row[3]))
            binE.append(str(row[4]))
            binF.append(str(row[5]))
            binG.append(str(row[6]))
            binH.append(str(row[7]))
            binI.append(str(row[8]))
            
    for i in range(len(binA)):
        binA[i] = int(binA[i])
        binB[i] = int(binB[i])
        binC[i] = int(binC[i])
        binD[i] = int(binD[i])
        binE[i] = int(binE[i])
        binF[i] = int(binF[i])
        binG[i] = int(binG[i])
        binH[i] = int(binH[i])
        binI[i] = int(binI[i])
    
    megalist.append(binA)
    megalist.append(binB)
    megalist.append(binC)
    megalist.append(binD)
    megalist.append(binE)
    megalist.append(binF)
    megalist.append(binG)
    megalist.append(binH)
    megalist.append(binI)
    
    for k in range(len(megalist)):
        adder = 0
        length = len(megalist[k])
        for l in range(len(megalist[k])):
            adder += megalist[k][l]
        average = adder/float(length)
        averagelist.append(average)
            
    
    return averagelist
    


if __name__ == '__main__':
    main()
