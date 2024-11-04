import socket
import threading

def handle_tcp_client(client, addr):
    """Função para gerenciar um cliente TCP."""
    print(f"Conexão recebida de {addr}")
    with client:
        while True:
            data = client.recv(2048)  # Recebe até 2048 bytes
            if not data:
                break  # Sai do loop se não houver dados
            mensagem = data.decode()
            print(f"Mensagem recebida de {addr}: {mensagem}")
            resposta = f"TCP: {mensagem}"
            client.send(resposta.encode())  # Envia a resposta ao cliente
    print(f"Conexão encerrada com {addr}")

def handle_udp_client(sock):
    """Função para gerenciar clientes UDP."""
    while True:
        data, addr = sock.recvfrom(2048)  # Recebe até 2048 bytes
        if data:
            mensagem = data.decode()
            print(f"Mensagem recebida de {addr}: {mensagem}")
            resposta = f"UDP: {mensagem}"
            sock.sendto(resposta.encode(), addr)  # Envia a resposta ao cliente
            print("Resposta enviada ao cliente:", resposta)

def main():
    host = 'localhost'

    # Configuração do servidor TCP
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind((host, 5000))
    tcp_server.listen()  # Permite múltiplas conexões
    print("Servidor TCP escutando na porta 5000...")

    # Configuração do servidor UDP
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind((host, 5001))
    print("Servidor UDP escutando na porta 5001...")

    # Iniciar a thread para o servidor UDP
    threading.Thread(target=handle_udp_client, args=(udp_server,), daemon=True).start()

    try:
        while True:
            client, addr = tcp_server.accept()
            threading.Thread(target=handle_tcp_client, args=(client, addr), daemon=True).start()
    except KeyboardInterrupt:
        print("Servidor encerrado.")
    finally:
        tcp_server.close()
        udp_server.close()

if __name__ == "__main__":
    main()
