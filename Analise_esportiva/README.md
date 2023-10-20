## ⚽ SofaScore
Este repositório contém um script em Python para obter e comparar estatísticas de equipes de futebol usando dados da API do SofaScore. O script permite selecionar duas equipes, escolher uma métrica de desempenho específica e gerar um gráfico de barras comparativo para as equipes selecionadas ao longo de várias temporadas.

## Dependências
Antes de usar este script, certifique-se de que as seguintes bibliotecas Python estão instaladas:
- Pandas: para manipulação de dados tabulares.
- Requests: para fazer solicitações HTTP à API do SofaScore.
- Plotly: para criar gráficos de barras interativos.
- Sys: para funcionalidades relacionadas ao sistema.
- Platform: para determinar o sistema operacional atual.
- Random: para gerar valores aleatórios.

Você pode instalar essas dependências usando o pip:

```bash
pip install pandas requests plotly
```

## Uso
1. Você pode usar a função `choose_team` para selecionar uma equipe e obter estatísticas. A função solicitará a divisão da equipe e retornará uma lista de estatísticas ao longo das temporadas.

```python
team_data = choose_team('nome_da_equipe')
```

2. Use a função `build_dataframe` para criar um DataFrame com os dados da equipe. Isso facilita a análise das estatísticas.

```python
team_dataframe = build_dataframe('nome_da_equipe')
```

3. Finalmente, use a função `build_chart` para construir um gráfico comparativo entre duas equipes com base em uma métrica específica. O gráfico será exibido interativamente.

```python
build_chart('metrica', 'equipe1', 'equipe2')
```

Lembre-se de substituir `'nome_da_equipe'` pela equipe de futebol desejada e `'metrica'` pela métrica de desempenho que deseja comparar, como 'chutes ao gol', 'gols marcados', 'assistências', etc.

### 🤝 Suporte/Contato

[![LinkedIn Badge](https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=)](https://www.linkedin.com/in/ihanmessias/)
[![Whatsapp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/61996487935)
[![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/devlinuxtv/)

✉ ihanmessias.dev@gmail.com

<p align="center">Ihan Messias Nascimento dos Santos</p>