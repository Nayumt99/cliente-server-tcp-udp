# Cliente TCP Simples em Python

Este é um simples cliente TCP escrito em Python, que permite a conexão a um servidor TCP especificado por um endereço IP e porta.

## Requisitos

Certifique-se de ter Python instalado em seu sistema. Este código foi testado em Python 3.x.

## Uso

1 - Clone o repositório ou baixe o arquivo cliente_tcp.py.

2 - Abra um terminal e navegue até o diretório onde o arquivo cliente_tcp.py está localizado.

3 - Execute o script Python com o seguinte comando:

````
python cliente_tcp.py
````

4- O script solicitará que você insira o endereço IP do servidor e a porta a serem conectados.

5 - Após fornecer o endereço IP e a porta, o cliente tentará estabelecer uma conexão com o servidor.

6 - Se a conexão for bem-sucedida, uma mensagem informando a conexão bem-sucedida será exibida

7 - Caso contrário, uma mensagem de erro será exibida.

Exemplo
````
$ python cliente_tcp.py
Socket criado com sucesso
Digite o Host ou IP a ser conectado: 127.0.0.1
Digite a porta a ser conectada: 8080
Cliente TCP conectado com Sucesso no Host: 127.0.0.1 e na porta: 8080
````

## Observações

Se ocorrer um erro durante a conexão, uma mensagem de erro será exibida e o programa será encerrado.
O tempo limite de espera para a conexão é de 2 segundos
