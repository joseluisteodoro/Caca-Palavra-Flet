#🕵️‍♂️ Caça-Palavras com Flet + Requests

Este é um mini game em Python com interface gráfica feito usando Flet. Ele simula um jogo de "forca", onde o usuário deve descobrir uma palavra secreta, letra por letra. A palavra é buscada online por meio da API pública https://api.dicionario-aberto.net/random. A interface é leve, moderna, em modo escuro e com mensagens interativas ao usuário.

O jogo funciona da seguinte maneira: ao clicar no botão "🔄 Gerar palavra", o programa faz uma requisição usando a biblioteca requests e retorna uma palavra aleatória. Caso essa palavra contenha acentos (á, ç, ê, etc), ela é descartada, garantindo que o usuário possa digitá-la facilmente no teclado comum. Uma vez gerada, a palavra é oculta com sublinhados (ex: "_ _ _ _ _") e o usuário começa a digitar letras para tentar acertar. A interface exibe as letras já tentadas e destaca se a tentativa foi correta ou incorreta, inclusive evitando letras repetidas.

As tecnologias usadas são:
- Flet (versão 0.28.3): framework para construir apps visuais multiplataforma (web, desktop e mobile) com Python.
- Requests: biblioteca para requisições HTTP simples e eficientes.

Para executar este projeto localmente:
1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual com `python -m venv .venv` e depois ative com `.venv\Scripts\activate` no Windows.
3. Instale as dependências com `pip install -r requirements.txt`.
4. Rode o projeto com `flet run src/main.py`.

Este projeto **não funciona em modo `flet build web` nem com `--web-renderer`** porque utiliza a biblioteca requests, que depende do backend Python para fazer chamadas HTTP. Sendo assim, o app precisa ser rodado como aplicação local ou publicado em um servidor backend que suporte Python (como Render, Railway, Replit ou Fly.io).

As dependências do projeto estão descritas no arquivo `pyproject.toml`, e são:
- flet==0.28.3
- requests

Autor: José Luis Teodoro (joselteodoro2@gmail.com)
Licença: MIT
