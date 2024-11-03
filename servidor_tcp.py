import socket

def servidor(host = 'localhost', port=5000):
    data_payload = 2048     #Maximo de pacotes
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print (f"TCP: {port}")
    
    sock.bind(server_address)
    sock.listen(1) #Recebe apenas uma conexão
    client, address = sock.accept()
    data = client.recv(data_payload)
   
    if data:
        mensagem = data.decode()  # Decodifica os bytes recebidos para string
        print("Mensagem recebida:", mensagem)
        
        # Envia de volta a mensagem com o prefixo "TCP:"
        resposta = f"TCP: {mensagem}"
        client.send(resposta.encode())  # Envia a resposta ao cliente
        
        
    # Fecha a conexão
    client.close()
    print("Conexão encerrada.")

    sock.close()
    print("Servidor encerrado.")

servidor()


           