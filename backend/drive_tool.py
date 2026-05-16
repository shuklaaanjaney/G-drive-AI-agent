from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


credentials = service_account.Credentials.from_service_account_file(
    'C:/Users/Aanjaney Shukla/OneDrive/Pictures/Desktop/drive-ai-agent/service_account.json',
    scopes=SCOPES
)

service = build('drive', 'v3', credentials=credentials)

def search_drive(query):

    results = service.files().list(
        q=query,
        fields="files(id, name, mimeType, webViewLink)"
    ).execute()

    return results.get("files", [])