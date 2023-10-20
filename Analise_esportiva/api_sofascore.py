import pandas as pd  # manipulação de dados tabulares.
import sys  # funcionalidades do sistema.
import platform  # determinar o sistema operacional.
import random  # geração de valores aleatórios.
import requests  # solicitações HTTP.
import plotly.graph_objects as go  # criação de gráficos interativos.

# Define endereços das equipes de futebol, mapeando o nome da equipe para o endereço correspondente no site SofaScore.
teams_adress_A = {'palmeiras' : 'palmeiras/1963', 'internacional' : 'internacional/1966', 'flamengo' : 'flamengo/5981', 'fluminense' : 'fluminense/1961',
'corinthians' : 'corinthians/1957', 'athletico paranaense' : 'athletico/1967', 'atletico mineiro' : 'atletico-mineiro/1977',
'america mineiro' : 'america-mineiro/1973', 'fortaleza' : 'fortaleza/2020', 'botafogo' : 'botafogo/1958', 'santos' : 'santos/1968',
'sao paulo' : 'sao-paulo/1981', 'bragantino' : 'red-bull-bragantino/1999', 'goias' : 'goias/1960', 'coritiba' : 'coritiba/1982',
'ceara' : 'ceara/2001', 'cuiaba' : 'cuiaba/49202', 'atletico goianiense' : 'atletico-goianiense/7314', 'avai' : 'avai/7315', 'juventude' : 'juventude/1980'}

teams_adress_B = {'cruzeiro' : 'cruzeiro/1954', 'gremio' : 'gremio/5926', 'vasco' : 'vasco-da-gama/1974', 'bahia' : 'bahia/1955', 'ituano' : 'ituano/2025',
'londrina' : 'londrina/2022', 'sport' : 'sport-recife/1959', 'sampaio correa' : 'sampaio-correa/2005', 'criciuma' : 'criciuma/1984', 'crb' : 'crb/22032',
'guarani' : 'guarani/1972', 'vila nova' : 'vila-nova/2021',  'ponte preta' : 'ponte-preta/1969', 'tombense' : 'tombense/87202', 'chapecoense' : 'chapecoense/21845',
'csa' : 'csa/2010', 'novorizontino' : 'novorizontino/135514', 'brusque' : 'brusque-fc/21884', 'operario' : 'operario/39634', 'nautico' : 'nautico/2011'}

# Função para obter um agente do usuário aleatório com base no sistema operacional
def get_random_user_agent():
    user_agents = {  # Dicionário de User-Agents para diferentes sistemas e navegadores.
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

    system = platform.system()  # Determina o sistema operacional em uso.
    if system not in user_agents.keys():  # Verifica se o sistema é suportado.
        print(f"Sistema operacional não suportado: {system}")
        sys.exit()
    system_browsers = list(user_agents[system].keys())
    random_browser = random.choice(system_browsers)  # Escolhe aleatoriamente um navegador para o sistema.
    
    return user_agents[system][random_browser]  # Retorna o User-Agent aleatório.

browsers = {'User-Agent': get_random_user_agent()}  # Cria um dicionário com o User-Agent aleatório.

base_api = 'https://api.sofascore.com/api/v1/team/'  # Define a URL base da API do SofaScore.
end_api = '/statistics/overall'  # Define a parte final da URL da API.

# Função para escolher uma equipe e obter estatísticas
def choose_team(team: str):
    data_list = []
    division = input(str('Em qual divisão está o time? ')).upper()  # Solicita a divisão da equipe.

    # Define pontos finais para diferentes temporadas.
    # Obtém o ID da equipe a partir do dicionário.
    if division == 'A':
        serie = '325'
        id_team = teams_adress_A[team.lower()][-4:]
        end_point_17 = '13100'  
        end_point_18 = '16183'
        end_point_19 = '22931'
        end_point_20 = '27591'
        end_point_21 = '36166'
        end_point_22 = '40557'
    elif division == 'B':
        serie = '390'
        id_team = teams_adress_B[team.lower()][-4:]
        end_point_17 = ''
        end_point_18 = '16184'
        end_point_19 = '22932'
        end_point_20 = '27593'
        end_point_21 = '36162'
        end_point_22 = '40560'

    middle_api = f'/unique-tournament/{serie}/season/'  # Cria uma parte intermediária da URL.

    # Cria URLs para diferentes temporadas e as adiciona a uma lista.
    url_17 = base_api + id_team + middle_api + end_point_17 + end_api
    url_18 = base_api + id_team + middle_api + end_point_18 + end_api
    url_19 = base_api + id_team + middle_api + end_point_19 + end_api
    url_20 = base_api + id_team + middle_api + end_point_20 + end_api
    url_21 = base_api + id_team + middle_api + end_point_21 + end_api
    url_22 = base_api + id_team + middle_api + end_point_22 + end_api

    urls_list = [url_17, url_18, url_19, url_20, url_21, url_22]  # Lista de URLs para as temporadas.
    ano_inicial = 2017
    data_list = []

    # Itera sobre as URLs, faz solicitações à API e armazena os dados na lista.
    for i, url in enumerate(urls_list):
        ano = ano_inicial + i
        api_link = requests.get(url, headers=browsers).json()  # Faz uma solicitação à API e obtém os dados em formato JSON.

        if 'error' not in api_link:  # Verifica se não há erro na resposta da API.
            stats = api_link['statistics']  # Obtém as estatísticas da equipe.
            stats['ano'] = ano  # Adiciona o ano como uma estatística.
            data_list.append(stats)  # Adiciona os dados à lista.

    return data_list

# Função para construir um DataFrame com os dados da equipe
def build_dataframe(team: str):
    team = choose_team(team.lower())  # Chama a função choose_team para obter os dados da equipe.

    team_dataframe = pd.DataFrame(index=team[0].keys())  # Cria um DataFrame vazio com índices baseados nos nomes das estatísticas.

    for i in range(len(team)):
        team_dataframe[str(team[i]['ano'])] = team[i].values()  # Preenche o DataFrame com os valores das estatísticas para cada ano.

    team_dataframe['Media'] = team_dataframe.mean(axis=1).apply(lambda x: float(f"{x:.1f}"))  # Calcula a média das estatísticas e arredonda para uma casa decimal.

    return team_dataframe  # Retorna o DataFrame com as estatísticas.

# Função para construir um gráfico comparativo entre duas equipes
def build_chart(metric: str, team1: str, team2: str):
    df_team1 = build_dataframe(team1.lower())  # Chama a função build_dataframe para obter os dados da primeira equipe.
    df_team2 = build_dataframe(team2.lower())  # Chama a função build_dataframe para obter os dados da segunda equipe.

    anos = ['2017', '2018', '2019', '2020', '2021', '2022']  # Lista de anos.

    data = []
    # Gráfico para a equipe 1
    for team_df, team_name in [(df_team1, team1)]:
        y_values = [team_df[ano][metric] for ano in anos]  # Obtém os valores da métrica para cada ano.
        data.append(go.Bar(name=team_name, x=anos, y=y_values))  # Adiciona os dados ao gráfico.

    # Gráfico para a equipe 2
    for team_df, team_name in [(df_team2, team2)]:
        y_values = [team_df[ano][metric] for ano in anos]
        data.append(go.Bar(name=team_name, x=anos, y=y_values))

    fig = go.Figure(data, layout_title_text=metric)  # Cria um objeto Figure com os dados do gráfico.

    return fig.show()  # Exibe o gráfico.