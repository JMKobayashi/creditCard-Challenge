# creditCard-Challenge
## Motivação

O projeto foi desenvolvido utilizando Python juntamente com Django e o Django REST Framework para a criação das APIs. Para a validação dos cartões foi utilizado a biblioteca [python-creditcard](https://github.com/MaisTodos/backend-python-creditcard) e para a realização de testes unitários foi utilizado o pytest.

## Instalação

### Requisitos:

* python-creditcard

* djangorestframework

* markdown

* pytest 

* cryptography

* httpie
  
 Para instalar separadamente:
 
 ```
 pip install <requisito> # Trocar <requisito> pelos Requisitos listados a cima
 ```
 
 Ou para instalar todos os requisitos:
 ```
 pip install -r requirements.txt
 ```
 
 **Verificar se a biblioteca python-creditcard foi instalada corretamente**
 
 Caso não tenha sido instalada realizadar o [download](https://github.com/MaisTodos/backend-python-creditcard) do código e instalar utilizando o pip.
 ```
 pip install python-creditcard-main.zip
 ```
 
 ## Banco de dados
 
 Para o banco será necessário aplicar as migrações:
 ```
 python manage.py migrate
 ```
 
 ## Rodando o servidor
 
 Utilize o seguinte comando para ativar o servidor local:
 ```
 python manage.py runserver
 ```
 ## APIs
 
 ### Token de autenticação para a utilização das outras APIs
 
 Parâmetros que serão passados para essa api são:
 ```
 username: string
 password: string
 ```
 Usuário cadastrado no banco para utilização nos testes:
 ```
 username:"admin"
 password:"123senha123"
 ```
 Requisição do token utilizando HTTPie:
 ```
 http post http://localhost:8000/token/ username="admin" password:"123senha123"
 ```
 ### Requisições GET para função
 #### API para listagem de todos os cartões cadastrados no banco
 Não será necessário passar nenhum parâmetro para a api. Somente o token de autenticação 
 ```
 http http://localhost:8000/credit-card/ 'Authorization: Token b96dc5862a760c6a860cf2366b7b028b3503390b'
 ```
 Retornará uma lista com todos os cartões salvos na banco de dados no seguinte formato:
 ```
 [
    {
      "brand":"<Marca do cartão>",
      "cvv":"<cvv do cartão>",
      "holder":"<Nome do detentor do cartão>"
      "id":"<id gerado pelo banco>"
      "number":"<Número do cartão>"
     },
     {
      "brand":"<Marca do cartão>",
      "cvv":"<cvv do cartão>",
      "holder":"<Nome do detentor do cartão>"
      "id":"<id gerado pelo banco>"
      "number":"<Número do cartão>"
     },
     .
     .
     .
 ]
 ```
 #### API para a listagem de um único cartão
 Será necessário passar o id do cartão para a api além do token de autenticação.
 ```
 # x é o id de algum cartão cadastrado no banco de dados
 http get http://localhost:8000/credit-card/?id=x 'Authorization: Token b96dc5862a760c6a860cf2366b7b028b3503390b'
 ```
 Retornará um único cartão de crédito no seguinte formato:
  ```
 [
    {
      "brand":"<Marca do cartão>",
      "cvv":"<cvv do cartão>",
      "holder":"<Nome do detentor do cartão>"
      "id":"<id gerado pelo banco>"
      "number":"<Número do cartão>"
     }
 ]
 ```
 
 ### POST
 
 #### API para cadastro de novos cartões no banco de dados
 Parâmetros que serão passados para essa api são:
 ```
 exp_date:string
 holder:string
 cvv:string
 number:string
 ```
 Requisição de cadastro de um novo cartão:
 ```
 http post http://localhost:8000/credit-card/ 'Authorization: Token b96dc5862a760c6a860cf2366b7b028b3503390b' exp_date="07/27" holder="James" number="4539578763621486" cvv=456
 ```
 Retornará o novo cartão de crédito inserido no banco no seguinte formato:
 ```
 [
    {
      "brand":"<Marca do cartão>",
      "cvv":"<cvv do cartão>",
      "holder":"<Nome do detentor do cartão>"
      "id":"<id gerado pelo banco>"
      "number":"<Número do cartão>"
    }
 ]
 ```
