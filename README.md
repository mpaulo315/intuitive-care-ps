# Iniciando o projeto

Cada teste pode ser avaliado individualmente. Para isso, basta seguir as seguintes instruções:

## Teste 1 e 2

**Tecnologias utilizadas**: **Python** :snake:

Para executar o projeto, basta seguir os seguintes passos:
```powershell
## Acessando o diretório do projeto
cd Teste_<número_do_teste>\

## Criando o ambiente virtual
python -m venv <nome_do_ambiente>

## Ativação se estiver no Windows
.\<nome_do_ambiente>\Scripts\activate

## Ativação se estiver no Linux
source ./<nome_do_ambiente>/bin/activate

## Instalando as dependências
pip install -r requirements.txt

## Executando o projeto
python main.py
```

## Teste 3
**Banco utilizado**: **MySQL** :dolphin:

**Arquitetura das pastas implementada no código:**

<ul>
    <li>:open_file_folder: Teste_3</li>
    <li>
    <ul>
        <li>:page_facing_up: main.sql</li>
        <li>:open_file_folder: 2023
        <ul>
            <li>:green_book: 1T2023.csv</li>
            <li>:green_book: 2t2023.csv</li>
            <li>:green_book: 3T2023.csv</li>
            <li>:green_book: 4T2023.csv</li>
        </ul>
    </li>
    <li>:open_file_folder: 2024
        <ul>
            <li>:green_book: 1T2024.csv</li>
            <li>:green_book: 2T2024.csv</li>
            <li>:green_book: 3T2024.csv</li>
            <li>:green_book: 4T2024.csv</li>
        </ul>
    </li>
    </ul>
    </li>
</ul>

## Teste 4

### Backend
**Tecnologias:** **Python** :snake:
* FastAPI
* SQLite3
* Caribou

#### Instruções para execução

```powershell
cd Teste_4\backend

## Criando o ambiente virtual
python -m venv <nome_do_ambiente>

## Se estiver no Windows
.\<nome_do_ambiente>\Scripts\activate

## Se estiver no Linux
source ./<nome_do_ambiente>/bin/activate

pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:
```env
DATABASE=<nome_do_banco>
```

Por fim
```powershell
python api/main.py
```

Uma vez que o servidor estiver rodando, basta acessar a rota `http://0.0.0.0:8000/docs` para visualizar a documentação da API.