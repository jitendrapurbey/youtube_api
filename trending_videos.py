import os
from apiclient import discovery
from oauth2client import file, client, tools
from httplib2 import Http


SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CLIENT_SECRETS_FILE = "client_secret.json"


def get_authenticated_service():
    store = file.Storage('token.json')
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
        credentials = tools.run_flow(flow, store)
    result = discovery.build(API_SERVICE_NAME, API_VERSION, http=credentials.authorize(Http()))
    return result


def main():
    youtube = get_authenticated_service()
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="IN",
        maxResults=10
    )
    response = request.execute()
    return response


if __name__ == "__main__":
    result = main()
    print(result)
