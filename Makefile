

gen:
	cat header.md > README.md
	echo "\n ## Active projects\n" >> README.md
	./gen_table.py >> README.md
