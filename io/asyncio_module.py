import asyncio
from socket import *

async def echo_server(address):
	loop = asyncio.get_event_loop()
	sock = socket(AF_INET, SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sock.bind(address)
	sock.listen(5)
	sock.setblocking(False)
	print('Server listening at', address)
	with sock:
		while True:
			client, addr = await loop.sock_accept(sock)
			print('Connection from', addr)
			loop.create_task(echo_client(loop, client))

async def echo_client(loop, client):
	with client:
		while True:
			data = await loop.sock_recv(client, 10000)
			if not data:
				break
			await loop.sock_sendall(client, b'Got:' + data)
	print('Connection closed')

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(echo_server(('', 25000)))
	loop.run_forever()