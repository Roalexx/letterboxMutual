import requests
from bs4 import BeautifulSoup

def fetch_all_movies(username):
    base_url = f"https://letterboxd.com/{username}/films/page/"
    page_number = 1
    movies_set = set()

    while True:
        url = f"{base_url}{page_number}/"
        try:
            response = requests.get(url)
            response.raise_for_status()  # İstek başarısız olursa hata fırlat
            
            soup = BeautifulSoup(response.text, 'html.parser')
            movie_elements = soup.find_all('li', class_='poster-container')

            if not movie_elements:
                break

            for element in movie_elements:
                title = element.find('img')['alt']
                movies_set.add(title)

            page_number += 1
        
        except requests.exceptions.RequestException as e:
            print("Bir hata oluştu:", e)
            break

    return movies_set

# Ana dosyadan çağırabilmek için bir fonksiyon ekleyelim
def get_movies(username):
    return fetch_all_movies(username)
