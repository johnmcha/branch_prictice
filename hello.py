mport requests

def get_response():
    return requests.get('https://www.google.co.kr/').status_code
