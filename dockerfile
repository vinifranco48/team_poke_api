# Use a imagem base do Python
FROM python:3.11

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app


# Copie o código-fonte para o contêiner
COPY . .

# Instale as dependências do Python
RUN pip install -r requirements.txt


# Exponha a porta em que a aplicação Flask será executada
EXPOSE 3000

# Comando para iniciar o servidor usando gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "run:app"]