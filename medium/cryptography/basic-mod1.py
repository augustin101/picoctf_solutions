inp = list(
	map(
		int,
		"165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138".split(),
	)
)
moded = [e % 37 for e in inp]
converted = [chr(ord("A") + e) if e < 26 else str(e - 26) if e < 36 else "_" for e in moded]
print(f"picoCTF{{{''.join(converted)}}}")
