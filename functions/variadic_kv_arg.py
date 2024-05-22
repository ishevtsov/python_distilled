def make_table(data, **parms):
	# Get configuration parameters from parms (a dict)
	fgcolor = parms.pop('fgcolor', 'black')
	bgcolor = parms.pop('bgcolor', 'white')
	width = parms.pop('width', None)

	# No more options
	if parms:
		raise TypeError(f'Unsupported config option {list(parms)}')

make_table('items',fgcolor='black', bgcolor='white', border=1,
borderstyle='grooved', cellpadding=10,
width=400)