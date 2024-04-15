import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) ##primeiro utiliza protocolo ip, em seguida TCP
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com Sucesso no Host: " + HostAlvo + " e na porta: " + PortaAlvo)
        s.shutdown(2) ## para não ficar em loop, adicionamos o shutdown para reiniciar e colocamos (2s) de tempo de espera
    except socket.error as e:
        print("Não foi possível conectar no Host: " + HostAlvo + " e na porta: " + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit() ##se apresentar erro, utilizamos o sys para sair da aplicação

if __name__ == "__main__": ##se a função for main, chame main
    main()


