import requests # type: ignore

def fetch_random_user():
    url='https://api.freeapi.app/api/v1/public/'
    response= requests.get(url)
    data = response.json()
    if data["success"] and 'data' in data :
        user_data = data['data']
        username=user_data['data'][3]['name']['first']
        country=user_data['data'][3]['location']['country']

        
        # country=user_data['location']['country']
        return username,country
        print(user_data)
    
    else:
        # raising exception in case of error 
        raise Exception("Failed to fetch user data from API")   

def main():
    try:
        username, country=fetch_random_user()
        print(f" {username} is from {country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()