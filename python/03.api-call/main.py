import requests

def _get_data():
    url = "https://fakestoreapi.com/products/1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        fact = response.text
        return fact

    except requests.exceptions.RequestException as e:
        print(e)
        print(f"an error occured")
        return None
    
product = _get_data()
print(product)