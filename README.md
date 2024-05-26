# Chatbot com modelo Mixtral via api Groq

Este repositório contém um aplicativo web desenvolvido com Streamlit que utiliza os modelos de linguagem Mixtral e Groq para diversas tarefas de processamento de linguagem natural (PLN). O aplicativo permite a interação com esses modelos de maneira intuitiva, proporcionando funcionalidades como geração de texto, resumo de textos longos, tradução e muito mais.

## Visão Geral

O aplicativo fornece uma interface simples e interativa para explorar as capacidades dos modelos LLM Mixtral e Groq. Utilizamos Streamlit para criar um front-end amigável e responsivo que permite aos usuários acessar rapidamente as funcionalidades de PLN.

## Funcionalidades

- **Geração de Texto**: Gere texto de forma criativa com base em prompts fornecidos pelo usuário.
- **Resumo de Texto**: Resuma textos longos em poucos parágrafos ou frases.
- **Tradução**: Traduza textos entre diferentes idiomas suportados pelos modelos.
- **Análise de Sentimento**: Analise o sentimento de textos fornecidos.
- **Perguntas e Respostas**: Obtenha respostas para perguntas baseadas em um contexto fornecido.

## Tecnologias Utilizadas

- **Streamlit**: Framework para construção de aplicativos web interativos em Python.
- **Mixtral**: Modelo de linguagem de última geração utilizado para diversas tarefas de PLN.
- **Groq**: Hardware e software de aceleração de IA para otimizar o desempenho dos modelos LLM.

## Instalação

Siga os passos abaixo para configurar o ambiente e executar o aplicativo:

1. Clone o repositório:
    ```sh
    git clone https://github.com/viniciusds2020/app_grog_mixtral.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python3 -m venv env
    source env/bin/activate  # No Windows, use `env\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure as credenciais e parâmetros necessários para acessar os modelos Mixtral e Groq. Isso pode envolver a criação de um arquivo `.env` com variáveis de ambiente específicas.

5. Execute o aplicativo:
    ```sh
    streamlit run app.py
    ```

## Estrutura do Repositório

- `app.py`: Arquivo principal do aplicativo Streamlit.
- `requirements.txt`: Arquivo de requisitos com as dependências do projeto.
- `README.md`: Este arquivo.

## Como Contribuir

1. Faça um fork do projeto.
2. Crie uma nova branch com a sua feature ou correção de bug:
    ```sh
    git checkout -b minha-nova-feature
    ```
3. Commit suas mudanças:
    ```sh
    git commit -m 'Adicionei minha nova feature'
    ```
4. Envie para o branch original:
    ```sh
    git push origin minha-nova-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

Agradecemos a todos os colaboradores e às equipes de desenvolvimento dos modelos Mixtral e Groq por fornecerem tecnologias incríveis que tornam este aplicativo possível.

---

Sinta-se à vontade para contribuir com melhorias e novas funcionalidades. Esperamos que este aplicativo seja útil para suas necessidades de processamento de linguagem natural!

