### Extração de Dados do Mercado Livre com DynamoDB e Streamlit
Visão Geral do Projeto
Este projeto tem como objetivo criar uma aplicação Python que realiza a extração de dados de ofertas do Mercado Livre e os armazena em um banco de dados DynamoDB. Além disso, disponibiliza uma interface web utilizando o Streamlit para visualização dos dados extraídos. Todo o ambiente, incluindo o banco de dados DynamoDB, é configurado e executado dentro de contêineres Docker, garantindo facilidade de uso e portabilidade.

#### Funcionalidades Principais
Extração de Dados do Mercado Livre: O projeto utiliza o framework Scrapy para realizar a extração das informações das ofertas no Mercado Livre de forma eficiente e escalável.

Armazenamento no Banco de Dados DynamoDB: Os dados extraídos são armazenados de forma persistente no DynamoDB, um banco de dados NoSQL altamente escalável e gerenciado pela AWS.

Interface Web com Streamlit: Os dados armazenados no DynamoDB são disponibilizados por meio de uma interface web interativa construída com o Streamlit, onde os usuários podem visualizar as informações de maneira amigável.

Ambiente Dockerizado: O uso de Docker e Docker Compose simplifica a configuração do ambiente e garante que a aplicação seja facilmente executada em qualquer sistema compatível.
### Pré-requisitos

Certifique-se de ter os seguintes componentes instalados em seu ambiente de desenvolvimento:

- Docker
- Docker Compose

### Configuração

1. Clone o repositório do projeto:

   ```shell
   git clone https://github.com/seu-nome-de-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

### Uso

1. Inicie o banco de dados DynamoDB e o aplicativo usando o Docker Compose:

   ```shell
   docker-compose up --build database
   ```

   Aguarde até que o banco de dados esteja pronto para aceitar conexões.

2. Em uma nova janela do terminal, inicie o aplicativo:

   ```shell
   docker-compose up --build app
   ```

3. Acesse a aplicação Streamlit:

   Abra um navegador da web e vá para `http://localhost:8501`. Você será redirecionado para a página inicial da aplicação, onde poderá visualizar os dados extraídos do Mercado Livre.

#### Acesse a aplicação Streamlit:

Abra um navegador da web e vá para http://localhost:8501. Você será redirecionado para a página inicial da aplicação.

Acionando a Extração de Dados:

Clique no botão "Extrair Dados" para iniciar o processo de extração de dados do Mercado Livre. Aguarde até que a extração seja concluída.

Visualizando os Dados Extraídos:

Clique no botão "