"""Google Analytics Reporting API V4 - Users Daily for Last 365 Days"""

from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

import httplib2
import matplotlib.pyplot as plt
import numpy as np

#create service credentials
#this is where you'll need your json key
#replace "keys/key.json" with the path to your own json key
credentials = ServiceAccountCredentials.from_json_keyfile_name('keys/client_secrets.json', ['https://www.googleapis.com/auth/analytics.readonly'])

# create a service object you'll later on to create reports
http = credentials.authorize(httplib2.Http())
service = build('analytics', 'v4', http=http, discoveryServiceUrl=('https://analyticsreporting.googleapis.com/$discovery/rest'))