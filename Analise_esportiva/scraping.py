from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html

# Teams Adress
teams_adress_A = {'palmeiras' : 'palmeiras/1963', 'internacional' : 'internacional/1966', 'flamengo' : 'flamengo/5981', 'fluminense' : 'fluminense/1961',
'corinthians' : 'corinthians/1957', 'athletico paranaense' : 'athletico/1967', 'atletico mineiro' : 'atletico-mineiro/1977',
'america mineiro' : 'america-mineiro/1973', 'fortaleza' : 'fortaleza/2020', 'botafogo' : 'botafogo/1958', 'santos' : 'santos/1968',
'sao paulo' : 'sao-paulo/1981', 'bragantino' : 'red-bull-bragantino/1999', 'goias' : 'goias/1960', 'coritiba' : 'coritiba/1982',
'ceara' : 'ceara/2001', 'cuiaba' : 'cuiaba/49202', 'atletico goianiense' : 'atletico-goianiense/7314', 'avai' : 'avai/7315', 'juventude' : 'juventude/1980'}

# Search team
def team_search(team:str):
    driver = webdriver.Edge()
    base_url = f'https://www.sofascore.com/team/football/{teams_adress_A[team]}'
    
    driver.get(base_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    conteudo = str(soup)
    estrutura = html.fromstring(conteudo)
    data_dict = {}
    
    for i in range(2, 7):
        base_xpath = f'//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[{i}]/div[2]/div[*]/'
        element_1 = estrutura.xpath(base_xpath + 'span[1]')
        element_2 = estrutura.xpath(base_xpath + 'span[2]')
        for data in range(len(element_1)):
            if data == 0:
                data_dict['Team'] = team.title()
            data_dict[element_1[data].text] = element_2[data].text
    
    return data_dict
            
team_search(team='flamengo')