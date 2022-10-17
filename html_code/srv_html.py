# сервак ловит данные которые кидает в него форма
import socket

addr = ('127.0.0.1', 63490)  # 192.168.200.210, 178.170.193.78, 63490
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(addr)
srv.listen(1)

while True:
    client, addres = srv.accept()
    data = client.recv(1024)  # от клиента получить данные, длина в 1 килобайт
    print(f'Connect: {addres}')
    print(data.decode('utf8'))
    client.send('Status: 200 OK'.encode('utf8'))
    client.close()
