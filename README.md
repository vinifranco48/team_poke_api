# API de Registro de Times Pokémon

A Poke-Api é um desafio proposto pela empresa Triagil, com o objetivo de criar e gerenciar times de Pokémon utilizando a [PokeAPI](https://pokeapi.co/). A API registra e gerencia esses times e utiliza o MongoDB para armazenar os dados. Isso permite a recuperação dos dados pelo ID de cada time. A decisão de utilizar o MongoDB como banco de dados foi motivada pela facilidade de recuperação dos dados no formato JSON, uma vez que se trata de um banco de dados orientado a documentos.


Na criação da API, foi utilizado o Docker Compose para gerenciar as imagens do banco de dados MongoDB (mongo-api) e da API (poke-api). Elas se comunicam por meio da rede net-api, que estabelece uma conexão entre as duas imagens. A imagem da API é exposta na porta 3000, e a imagem do MongoDB é exposta na porta 27018:27017.

## Como usar

### Pré-requisitos

- Docker e Docker Compose instalados em seu sistema.

### Instruções de Uso

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/vinifranco48/team_poke_api.git

2. Execute o comando a seguir para iniciar os serviços Docker

    ```bash
    docker-compose up -d

3. Agora você pode acessar a API através de http://localhost:3000 na raiz do projeto está a documentação com todas as rotas.

### Endpoints da API
- GET /api/teams: Retorna informações sobre todos os times registrados.
- GET /api/teams/{user}: Retorna informações sobre o time do usuário pelo ID.
- POST /api/teams: Registra um novo time de Pokémon.
