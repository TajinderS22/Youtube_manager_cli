import requests # type: ignore

def fetch_random_user(i):
    url='https://api.freeapi.app/api/v1/public/randomusers'
    response= requests.get(url);
    data= response.json()
    if data['success']:
        user_data=data['data']['data'][i]
        username=user_data['name']['first']
        country=user_data['location']['country']
        return username,country
    else:
        raise Exception("Failed to fetch Data fro Api ")

def main(i):
    try:
        username, country= fetch_random_user(i)
        print(f" {username} is from { country }")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    for i in range(0,10):
        main(i)