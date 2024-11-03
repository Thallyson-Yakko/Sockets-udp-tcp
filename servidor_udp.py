import socket

def servidor(host = 'localhost', port=5001):
    data_payload = 2048     #Maximo de pacotes
    sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print (f"UDP: {port}")
    
    sock.bind(server_address)
   
    while True:
        # Recebe dados e o endereço do cliente
        data, address = sock.recvfrom(data_payload)
        if data:
            mensagem = data.decode()  
            print("Mensagem recebida:", mensagem)
            
            
            resposta = f"UDP:{mensagem}"
            sock.sendto(resposta.encode(), address)  
            print("Resposta enviada ao cliente:", resposta)

    # O servidor UDP geralmente não fecha como o TCP, mas se quisesse encerrar:
    sock.close()
    print("Servidor encerrado.")

# Executa o servidor
servidor()