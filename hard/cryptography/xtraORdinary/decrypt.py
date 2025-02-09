from itertools import product


def encrypt(ptxt, key):
	ctxt = b""
	for i in range(len(ptxt)):
		a = ptxt[i]
		b = key[i % len(key)]
		ctxt += bytes([a ^ b])
	return ctxt


with open("output.txt", "r") as f:
	encrypted_hex = f.read().strip()
	cypher = bytes.fromhex(encrypted_hex)

random_strs = [
	b"my encryption method",
	b"is absolutely impenetrable",
	b"and you will never",
	b"ever",
	b"break it",
]

secret_key = b"Africa!"  # found by decrypting with `picoCTF{`
cypher = encrypt(cypher, secret_key)

for combination in product([0, 1], repeat=len(random_strs)):
	current = cypher

	for use_str, decrypt_str in zip(combination, random_strs):
		if use_str:
			current = encrypt(current, decrypt_str)

	decoded = current.decode("ascii")
	if "picoCTF{" in decoded:
		print(decoded)
		exit(0)
