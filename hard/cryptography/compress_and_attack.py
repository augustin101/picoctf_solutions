from pwn import remote
import argparse
import string


def get_connection(host, port):
	return remote("mercury.picoctf.net", 33976)


def get_length(conn, text):
	conn.recvuntil("encrypted:")
	conn.sendline(text)
	conn.recvline()
	conn.recvline()
	return int(conn.recvline().decode())


def compress_attack(args):
	conn = get_connection(args.host, args.port)
	flag = "picoCTF{"
	char_set = string.ascii_letters + "_}"
	length = get_length(conn, flag)

	while flag[-1] != "}":
		for c in char_set:
			if get_length(conn, flag + c) == length:
				flag += c
				print(flag)
				break


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Compression Oracle Attack Script")
	parser.add_argument("--host", type=str, default="mercury.picoctf.net", help="Target host")
	parser.add_argument("--port", type=int, required=True, help="Target port")
	args = parser.parse_args()

	compress_attack(args)
