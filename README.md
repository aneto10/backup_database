# MariaDB Backup Script

Este é um script em Python para realizar backups de bancos de dados MariaDB. O script faz backup da estrutura, dados, triggers, stored procedures e eventos do banco de dados especificado.

## Pré-requisitos

1. Python 3.x
2. Biblioteca `python-dotenv` para carregar variáveis de ambiente a partir de um arquivo `.env`
3. Executável `mariadb-dump.exe` (parte da instalação do MariaDB)

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu_usuario/backup_mariadb.git
    cd backup_mariadb
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Para Linux/macOS
    .venv\Scripts\activate     # Para Windows
    ```

3. Instale as dependências:

    ```sh
    pip install python-dotenv
    ```

4. Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente conforme o exemplo abaixo:

    ```env
    DB_HOST=localhost
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_NAME=nome_do_banco
    BACKUP_PATH=/caminho/para/salvar/o/backup
    MARIADB_DUMP_PATH=C:\\Program Files\\MariaDB 10.5\\bin\\mariadb-dump.exe
    ```
## Explicação das Variáveis de Ambiente
    
    DB_HOST: O endereço do servidor MariaDB (por exemplo, localhost).
    DB_USER: O nome do usuário do banco de dados.
    DB_PASSWORD: A senha do usuário do banco de dados.
    DB_NAME: O nome do banco de dados que você deseja fazer backup.
    BACKUP_PATH: O caminho onde o arquivo de backup será salvo.
    MARIADB_DUMP_PATH: O caminho completo para o executável mariadb-dump.exe.
    
    
## Funcionalidades

    1. Backup Completo: Inclui estrutura do banco de dados, dados, stored procedures, triggers e eventos.
    2. Progresso do Backup: Exibe o progresso do backup no terminal, atualizado em tempo real


## Uso

Execute o script para fazer o backup do banco de dados:

```sh
python backup_mariadb.py
```


## Instruções Adicionais

- **Estimativa do Tamanho do Banco de Dados**:
  - A estimativa do tamanho do banco de dados (`estimated_size`) é configurada no script Python. Este valor pode ser ajustado conforme necessário para melhorar a precisão do progresso exibido.
- **Atualização em Tempo Real**:
  - O progresso do backup é atualizado em intervalos regulares (a cada 5 segundos por padrão). Você pode ajustar esse intervalo modificando o valor do `time.sleep(5)` na função de monitoramento.
