MOD = 41
inp = list(
	map(
		int,
		"432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63".split(),
	)
)
moded = [e % MOD for e in inp]


def find_inverse(e):
	for i in range(MOD):
		if (e * i) % MOD == 1:
			return i
	return -1


mod_inverse = [find_inverse(e) for e in moded]
converted = [
	chr(ord("a") + e - 1) if e < 27 else str(e - 27) if e < 37 else "_" for e in mod_inverse
]
print(f"picoCTF{{{''.join(converted)}}}")
