# (HoneyPOT) Domino Genius PDF

![Logo do Domino Genius PDF](favicon.png)

O Domino Genius PDF é uma simples HoneyPOT HTTP/HTTPS baseada em Python, o aplicativo em si permite gerar fichas personalizadas do jogo de Dominó em formato PDF. Com este aplicativo, você pode criar e baixar facilmente fichas de jogo de Dominó imprimíveis com letras ou palavras randomizadas. Este aplicativo loga todas as tentativas de acesso a URLs que venham a gerar ERRO 404, funcionando como uma HoneyPot HTTP, HTTPS. os Logs ficarão armazenados em um arquivo de LOGs onde é possível consultar depois de onde vieram as requisições (IP) e quais foram.

## Recursos do aplicativo

- Gere fichas personalizadas do jogo de Dominó em formato PDF
- Randomize letras ou palavras nas fichas de jogo
- Interface web simples e intuitiva
- Fácil de usar e amigável para o usuário

## Recursos HoneyPOT
- Capturar IP e requisições realizadas.

## Instalação

1. Clone o repositório: `git clone https://github.com/nocerainfosec/domino-genius-pdf.git`
2. Navegue até o diretório do projeto: `cd domino-genius-pdf`
3. Instale as dependências necessárias: `pip install -r requirements.txt`

## Utilização do aplicativo

1. Execute o aplicativo: `python app.py`
2. Abra seu navegador da web e acesse `http://localhost:5000`
3. Digite a lista de palavras ou letras separadas por vírgulas.
4. Clique no botão "Gerar Peças".
5. O arquivo PDF será baixado automaticamente.

## Contribuição

Contribuições são bem-vindas! Se você tiver ideias, sugestões ou relatórios de bugs, abra uma issue ou envie um pull request. Para alterações importantes, abra uma issue primeiro para discutir as alterações propostas.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Agradecimentos

- [Flask](https://flask.palletsprojects.com/) - Framework web usado para desenvolver o aplicativo
- [FPDF](https://pyfpdf.readthedocs.io/) - Biblioteca usada para gerar arquivos PDF
- [Geolite2](https://pypi.org/project/GeoLite2/) - Biblioteca usada para geolocalização de IP


## Sobre mim
Olá, Sou Guilherme Nocera. Eu sou um pesquisador de segurança e Red Teamer, faço engajamentos de segurança ofensiva em [Nocera Infosec](https://www.nocerainfosec.com.br/). Gosto de fazer Scripts no meu tempo livre para ajudar a comunidade, Espero que você goste deste projeto!

Por fim, se você usar este projeto para fins ilegais, não serei responsável por tal ato!

## Contribuir
Em primeiro lugar, um grande obrigado 🙏🏻 ! Contribir para o projeto é fácil: [PRs](https://help.github.com/articles/about-pull-requests/) (https://www.nocerainfosec.com.br).

_P.S. Para qualquer dúvida ou preocupação, você pode entrar em contato comigo em  [Nocera Infosec](https://nocerainfosec.com.br). Farei o possível para ajudar 🙏._
