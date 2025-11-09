
from flask import Flask, render_template, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gerar')
def gerar_pdf():
    try:
        # Executa o script que gera o PDF
        subprocess.run(["python", "Checklist_Invest53App_Premium_Resumo_Leve.py"], check=True)

        # Caminho do arquivo gerado
        pdf_path = "Invest53App_Checklist.pdf"
        if os.path.exists(pdf_path):
            return send_file(pdf_path, as_attachment=True)
        else:
            return "⚠️ Erro: PDF não encontrado.", 500

    except Exception as e:
        return f"❌ Erro ao gerar o PDF: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
