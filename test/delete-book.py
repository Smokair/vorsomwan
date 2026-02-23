import requests
import json

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
      authCreds = (LOGIN, PASSWORD)
      r = requests.post(
            f"{APIHOST}/api/v1/loginViaBasic",
            auth = authCreds
      )
      if r.status_code == 200:
        return r.json()["token"]
      else:
           raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to AUTH.")
def deleteBook(book, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{book}",
        headers={
            "Content-type": "application/json",
            "X-API-Key": apiKey
        }
    )
    if r.status_code == 200:
        print(f"Book {book} deleted.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to delet book {book}.")
    
apiKey = getAuthToken()

for i in range(0,40):
    book = i
    deleteBook(book, apiKey)






