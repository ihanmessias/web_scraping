# Import libs
import sys
import platform
import random
import requests
from bs4 import BeautifulSoup

# User-Agents for Web Scraping
user_agents = {
    'Linux': {
        'Mozilla Firefox': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Google Chrome': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Opera': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 OPR/77.0.4054.146'
    },
    'Windows': {
        'Mozilla Firefox': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Google Chrome': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Microsoft Edge': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
    },
    'Darwin': {
        'Safari': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
    }
}

class WebScraping:
    def __init__(self, site_url) -> None:
        self.site_url = site_url
        self.user_agent = self.get_random_user_agent()
    # Get System
    def get_random_user_agent(self):
        system = platform.system()
        if system not in user_agents.keys():
            print(f"Sistema operacional não suportado: {system}")
            sys.exit()    
        system_browsers = list(user_agents[system].keys())
        random_browser = random.choice(system_browsers)
        return user_agents[system][random_browser]
    # Scraping
    def scraping(self):
        headers = {'User-Agent': self.user_agent}
        try:
            response = requests.get(self.site_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # TODO: Faça o scraping da página e extraia as informações aqui
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a solicitação: {e}")

if __name__ == '__main__':
    site_url = 'https://www.exemplo_de_site.com/'  # Substitua pelo URL do site que deseja raspar
    scraper = WebScraping(site_url)
    scraper.scraping()