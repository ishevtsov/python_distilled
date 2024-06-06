import argparse

def main(argv):
	p = argparse.ArgumentParser(description='Process some data.')

	# A positional argument
	p.add_argument("infile")

	# An option taking an argument
	p.add_argument("-o", "--output", action="store")

	# An option that sets a Boolean flag
	p.add_argument("-d", "--debug", action="store_true", default=False)

	# Parse the command line
	args = p.parse_args(args=argv)

	# Retrieve the option settings
	infile = args.infile
	output = args.output
	debugmode = args.debug

	print(infile, output, debugmode)

if __name__ == '__main__':
	import sys
	main(sys.argv[1:])