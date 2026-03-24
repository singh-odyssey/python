import requests

HTTP_OK:int =200
def get_ip()->str:
    url:str = "https://api.freeapi.app/api/v1/kitchen-sink/request/ip"
    response =requests.get(url)
    payload =response.json()
    
    if payload['statusCode'] ==HTTP_OK:
        ip = payload['data']['ip']
        
    else:
        raise Exception(f"Failed to get IP, status code: {payload['statusCode']}")
    
    return ip

def main():
    ip = get_ip()
    print(ip)
    
if __name__ == "__main__":
    main()