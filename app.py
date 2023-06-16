# Dominó Genius PDF
# Desenvolvido por Guilherme Elias Gomes Nocera

from flask import Flask, render_template, request, send_file, abort
from fpdf import FPDF
import random
from datetime import date
import os
import schedule
import time
import secrets
import string
import logging
from geolite2 import geolite2
import user_agents

app = Flask(__name__)

class DominoPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Dominó Genius PDF", 0, 1, "C")
            self.ln(10)  # Adiciona um espaço após o título

            self.set_font("Arial", "", 10)
            self.cell(0, 8, f"Lista de Palavras ({len(self.palavras)} palavras):", 0, 1, "L")
            self.ln(5)

            self.set_font("Arial", "", 8)
            palavra_str = ", ".join(self.palavras)
            self.multi_cell(0, 5, palavra_str, 0, "L")
            self.ln(10)  # Adiciona um espaço após a lista de palavras

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Dominó Impresso por Dominó Genius PDF - Página {self.page_no()} - {date.today().strftime('%d/%m/%Y')}", 0, 0, "C")

    def create_domino(self, letra):
        self.rect(self.x, self.y, 20, 40)
        self.set_xy(self.x + 5, self.y + 5)
        self.set_font("Arial", "", 20)
        self.cell(10, 10, letra, align="C")

def generate_random_token(length):
    characters = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(characters) for _ in range(length))
    return token

def criar_pasta():
    if not os.path.exists('dominos'):
        os.makedirs('dominos')

def deletar_dominos():
    dominos_dir = 'dominos'
    for filename in os.listdir(dominos_dir):
        file_path = os.path.join(dominos_dir, filename)
        os.remove(file_path)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        palavras_input = request.form['palavras'].strip()
        palavras = [palavra.strip() for palavra in palavras_input.split(",")]
        random.shuffle(palavras)

        criar_pasta()

        pdf = DominoPDF(format='A4')
        pdf.palavras = palavras

        pdf.add_page()

        espaco_horizontal = 5
        espaco_vertical = 5

        num_linhas = int(pdf.h / 40)
        num_colunas = int(pdf.w / 20)

        espaco_total_horizontal = (num_colunas - 1) * espaco_horizontal
        espaco_total_vertical = (num_linhas - 1) * espaco_vertical

        tamanho_real_horizontal = (pdf.w - espaco_total_horizontal) / num_colunas
        tamanho_real_vertical = (pdf.h - espaco_total_vertical) / num_linhas

        x = pdf.l_margin
        y = pdf.t_margin + 40

        for index, palavra in enumerate(palavras):
            if index != 0 and index % (num_linhas * num_colunas) == 0:
                pdf.add_page()

            if pdf.page_no() == 1:
                pdf.set_xy(x, y)
                pdf.create_domino("")

            for letra in palavra:
                pdf.set_xy(x, y)
                pdf.create_domino(letra)
                x += tamanho_real_horizontal + espaco_horizontal

                if x + tamanho_real_horizontal > pdf.w - pdf.r_margin:
                    x = pdf.l_margin
                    y += tamanho_real_vertical + espaco_vertical

                    if y + tamanho_real_vertical > pdf.h - pdf.b_margin:
                        pdf.add_page()
                        x = pdf.l_margin
                        y = pdf.t_margin

            x += tamanho_real_horizontal + espaco_horizontal

            if x + tamanho_real_horizontal > pdf.w - pdf.r_margin:
                x = pdf.l_margin
                y += tamanho_real_vertical + espaco_vertical

                if y + tamanho_real_vertical > pdf.h - pdf.b_margin:
                    pdf.add_page()
                    x = pdf.l_margin
                    y = pdf.t_margin

            pdf.set_xy(x, y)
            pdf.create_domino("")

        folder_token = generate_random_token(16)
        folder_path = os.path.join("dominos", folder_token)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        pdf_filename = f"{folder_token}_dominos_{time.strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf_path = os.path.join(folder_path, pdf_filename)
        pdf.output(pdf_path, "F")

        # Agendar a exclusão dos arquivos a cada 24 horas
        schedule.every(24).hours.do(deletar_dominos)

        return send_file(pdf_path, as_attachment=True)

    return render_template('index.html')
    
# Configura logs
logging.basicConfig(filename='error.log', level=logging.INFO)

# carerga a base de dados para geolocalização GeoLite2
reader = geolite2.reader()

# Define o manipulador de erro 404
@app.errorhandler(404)
def page_not_found(e):
    # Verifica se o valor do cabeçalho "User-Agent" é None
    user_agent_string = request.headers.get('User-Agent')
    if user_agent_string is None:
        return "Pare de hackear a aplicação!", 403

    # Obtém as informações do usuário
    user_agent = user_agents.parse(user_agent_string)
    ip_address = request.remote_addr
    isp, coordinates = get_ip_info(ip_address)

    # Registra o URL solicitado, endereço IP, coordenadas, ISP, dispositivo e navegador
    log_message = f"Página não encontrada: {request.url} - IP: {ip_address} - Coordenadas: {coordinates} - ISP: {isp} - Dispositivo: {user_agent.device.family} - Navegador: {user_agent.browser.family} {user_agent.browser.version_string}"
    logging.error(log_message)

    return render_template('404.html'), 404



# Função para obter informações de IP
def get_ip_info(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()
        isp = data['isp']
        coordinates = (data['lat'], data['lon'])
    except:
        isp = "N/A"
        coordinates = "N/A"

    return isp, coordinates
 
if __name__ == '__main__':
    app.run(debug=False)
