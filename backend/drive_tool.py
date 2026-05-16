from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import json


SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


service_account_info = json.loads(os.getenv("GOOGLE_CREDENTIALS"))

credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=SCOPES
)

service = build('drive', 'v3', credentials=credentials)

def search_drive(query):

    results = service.files().list(
        q=query,
        fields="files(id, name, mimeType, webViewLink)"
    ).execute()

    return results.get("files", [])