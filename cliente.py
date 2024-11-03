import socket

def cliente():
    # Solicita ao usuário o protocolo e a mensagem
    protocolo = input("Escolha o protocolo (TCP/UDP): ").strip().upper()
    mensagem = input("Digite a mensagem a ser enviada: ")

    if protocolo == "TCP":
        # Configuração para o protocolo TCP
        host = 'localhost'
        port = 5000
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))  # Conecta ao servidor
            sock.sendall(mensagem.encode())  # Envia a mensagem
            resposta = sock.recv(2048).decode()  # Recebe a resposta do servidor
            print("Resposta do servidor:", resposta)

    elif protocolo == "UDP":
        # Configuração para o protocolo UDP
        host = 'localhost'
        port = 5001
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(mensagem.encode(), (host, port))  # Envia a mensagem
            resposta, _ = sock.recvfrom(2048)  # Recebe a resposta do servidor
            print("Resposta do servidor:", resposta.decode())

    else:
        print("Protocolo inválido. Escolha 'TCP' ou 'UDP'.")

# Executa o cliente
cliente()