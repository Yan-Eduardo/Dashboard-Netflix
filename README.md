# :chart_with_upwards_trend: Dashboard de Assinaturas Netflix
Este repositório contém a implementação de um dashboard de assinaturas da plataforma de streaming Netflix. Seu desenvolvimento é para fins acadêmicos, exemplificando os recursos exigidos pelo Desafio Python do [Projeto Desenvolve](http://projetodesenvolve.com.br).

### Instruções de uso
Este projeto foi desenvolvido usando a versão 3.12 do Python em conjunto das bibliotecas Streamlit, Pandas e Plotly. Para execução do script, todas as versões utilizadas podem ser encontradas em `requirements.txt`. <br>
O dashboard pode ser executado através do seguinte comando no terminal:
```
streamlit run app.py
```
A execução iniciará o servidor local do Streamlit e abrirá o dashboard no seu navegador padrão.

### Estrutura do Projeto
| Arquivo   | Descrição |
| :-------- | :------- |
| `app.py`  | Este é o arquivo principal do projeto. Ele contém as funcionalidades do dashboard, entre elas a manipulação de dados com Pandas, criação das visualizações e gráficos com Plotly, e manipulação e estruturação de widgets do Streamlit.    |
| `style.css` | A estilização de elementos com CSS. Note que o nome das classes está associada aos nomes gerados pelos widgets do Streamlit |
| `dataset.csv`   | Base de dados utilizada no projeto. Maiores detalhes a seguir.   |
| `config.toml` | Arquivo contendo configurações de tema do streamlit

### Dados
O arquivo `dataset.csv` é uma base de dados de usuários fictícios da netflix, onde cada linha contem informações da conta. Descreveremos a seguir apenas as colunas relevantes para o nosso painel.
* Subsctiption: O nível da assinatura do cliente.
* Join Date: A data em que o cliente realizou a sua assinatura.
* County: Em qual país o assinante reside
* Device: Em qual dispositivo o assinante utiliza a plataforma.

### Yan Eduardo Carneiro Cruz
Atualmente estudando desenvolvimento fullstack pelo [Projeto desenvolve](https://projetodesenvolve.com.br)<br>
:camera: [Meu instagram](https://www.instagram.com/okamii_yan/) <br>
✉️E-mail para contato: contato.yaneduardo@outlook.com
