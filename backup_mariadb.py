import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv
import threading
import time
import sys

# Função para monitorar o progresso do backup
def monitor_progress(backup_file, estimated_size):
    while not os.path.exists(backup_file):
        time.sleep(1)  # Esperar até que o arquivo seja criado

    while True:
        if os.path.exists(backup_file):
            current_size = os.path.getsize(backup_file)
            if current_size >= estimated_size:
                break
            progress = (current_size / estimated_size) * 100
            # Atualizar o progresso na mesma linha
            print(f"\rProgresso do backup: {progress:.2f}%", end='')
            sys.stdout.flush()
        time.sleep(5)  # Verificar a cada 5 segundos
    # Garantir que o progresso chegue a 100% ao final
    print("\rProgresso do backup: 100.00%", end='')
    sys.stdout.flush()

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as variáveis de ambiente
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
BACKUP_PATH = os.getenv('BACKUP_PATH')
MARIADB_DUMP_PATH = os.getenv('MARIADB_DUMP_PATH')

# Estimar o tamanho do banco de dados (Este valor pode ser ajustado conforme necessário)
estimated_size = 800 * 1024 * 1024  # Exemplo: 500MB

# Gerar um nome de arquivo único baseado na data e hora atuais
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = os.path.join(BACKUP_PATH, f"{DB_NAME}_backup_{timestamp}.sql")

# Comando para fazer o backup usando mariadb-dump
dump_cmd = [
    MARIADB_DUMP_PATH,
    f'--host={DB_HOST}',
    f'--user={DB_USER}',
    f'--password={DB_PASSWORD}',
    f'--databases', DB_NAME,
    '--routines',  # Inclui stored procedures e functions
    '--triggers',  # Inclui triggers
    '--events'     # Inclui eventos
]

# Iniciar a thread de monitoramento
monitor_thread = threading.Thread(target=monitor_progress, args=(backup_file, estimated_size))
monitor_thread.start()

# Executar o comando mariadb-dump
with open(backup_file, 'w') as f:
    result = subprocess.run(dump_cmd, stdout=f, stderr=subprocess.PIPE)

# Verificar se o comando foi executado com sucesso
if result.returncode == 0:
    print(f"\nBackup do banco de dados {DB_NAME} realizado com sucesso em {backup_file}")
else:
    print(f"\nErro ao realizar o backup: {result.stderr.decode('utf-8')}")

# Aguardar a conclusão da thread de monitoramento
monitor_thread.join()
