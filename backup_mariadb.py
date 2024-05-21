import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as variáveis de ambiente
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
BACKUP_PATH = os.getenv('BACKUP_PATH')
MARIADB_DUMP_PATH = os.getenv('MARIADB_DUMP_PATH')

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
print(dump_cmd)
# Executar o comando mariadb-dump
with open(backup_file, 'w') as f:
    result = subprocess.run(dump_cmd, stdout=f, stderr=subprocess.PIPE)

# Verificar se o comando foi executado com sucesso
if result.returncode == 0:
    print(f"Backup do banco de dados {DB_NAME} realizado com sucesso em {backup_file}")
else:
    print(f"Erro ao realizar o backup: {result.stderr.decode('utf-8')}")
