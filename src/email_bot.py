
import os.path
import pickle

from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

import base64
from bs4 import BeautifulSoup

class GmailConfig:

    def __init__(self, token_path='auth/token.pickle', creds_path='auth/credentials.json'):

        creds=None

        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        
        if os.path.exists(token_path):
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)
  
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
                creds = flow.run_local_server(port=0)
  
        # Save the access token in token.pickle file for the next run
            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)
  
        # Connect to the Gmail API
        self.service = build('gmail', 'v1', credentials=creds)

class EmailBot(GmailConfig):

    def __init__(self, token_path='auth/token.pickle'):
        self.config = GmailConfig(token_path)
        self.messages = None

    def fetch_messages(self):
        result = self.config.service.users().messages().list(userId='me').execute()
        self.messages = result.get('messages')

    def display_messages(self):
        if self.messages is not None:
            for msg in self.messages:
                txt = self.config.service.users().messages().get(userId='me', id=msg['id']).execute()
                payload = txt['payload']
                headers = payload['headers']
                for d in headers:
                    if d['name'] == 'Subject':
                        subject = d['value']
                    if d['name'] == 'From':
                        sender = d['value']

                parts = payload.get('parts')[0]
                data = parts['body']['data']
                data = data.replace("-","+").replace("_","/")
                decoded_data = base64.b64decode(data)

                # Now, the data obtained is in lxml. So, we will parse it with BeautifulSoup library
                soup = BeautifulSoup(decoded_data , "lxml")
                body = soup.body()
  
                # Printing the subject, sender's email and message
                print("Subject: ", subject)
                print("From: ", sender)
                print("Message: ", body)
                print('\n')


if __name__ == '__main__':
    test = EmailBot()
    test.fetch_messages()
    test.display_messages()



