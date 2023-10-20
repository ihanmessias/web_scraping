# 🤖 Web Scraping com User-Agents Aleatórios
Este repositório contém um script Python para realizar web scraping de sites, utilizando User-Agents aleatórios para evitar bloqueios e aumentar a eficácia da coleta de dados.

## Desafio Enfrentado
Durante o processo de aprimoramento das habilidades de web scraping, enfrentamos desafios de lentidão e bloqueios em sites, mesmo ao utilizar cabeçalhos (headers) para simular um usuário comum. Esses problemas podem prejudicar a eficácia do web scraping.

## Solução Proposta
A solução para esses desafios veio com a técnica de User-Agents aleatórios. Com User-Agents que correspondem a navegadores populares, você pode se camuflar no meio dos usuários reais da web, tornando suas solicitações menos suspeitas e menos propensas a serem bloqueadas.

## Como Funciona
O script utiliza a biblioteca Requests para fazer solicitações HTTP ao site desejado, com um User-Agent aleatório. Aqui estão as etapas principais do processo:

1. Importa as bibliotecas necessárias, incluindo Requests e BeautifulSoup.
2. Define uma lista de User-Agents para sistemas operacionais Linux, Windows e Darwin, com navegadores populares.
3. Cria uma classe WebScraping que recebe a URL do site como parâmetro.
4. Gera um User-Agent aleatório com base no sistema operacional do usuário.
5. Realiza a solicitação HTTP com o User-Agent aleatório.
6. Utiliza BeautifulSoup para fazer o parsing do conteúdo HTML da página.

**OBS:** ***O trecho de código com o comentário "TODO" é onde você pode implementar o scraping específico para o site desejado.***

### 🤝 Suporte/Contato

[![LinkedIn Badge](https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=)](https://www.linkedin.com/in/ihanmessias/)
[![Whatsapp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/61996487935)
[![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/devlinuxtv/)

✉ ihanmessias.dev@gmail.com

<p align="center">Ihan Messias Nascimento dos Santos</p>