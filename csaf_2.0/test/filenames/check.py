import argparse
import json
import os
import re
import sys

def read(csaffile):
	with(open(csaffile, "r")) as f:
		data = json.load(f)
	return data

def get_filename(filename):
	return os.path.basename(filename)
	
def get_basedir(filepath):
	return os.path.dirname(os.path.abspath(filepath))+'/'
	
def compute_filename(csaf):
	document_tracking_id='_invalid'
	if csaf.get('document'):
		doc=csaf.get('document')
		if doc.get('tracking'):
			track=doc.get('tracking')
			if track.get('id'):
				document_tracking_id=track.get('id')
	
	filename = re.sub(r"([^+\-_a-z0-9]+)", '_', document_tracking_id.lower())
	return filename + '.json'

def check(current, computed):
	return current == computed

def write(result, filename):
	with(open(filename, "w")) as f:
		json.dump(result, f, indent=2)

def main():
	parser = argparse.ArgumentParser(description='Checks filename of a CSAF 2.0.')
	parser.add_argument('input_file', type=str, help="CSAF input file to check filename")
	parser.add_argument('-p', '--print', dest='print', action="store_true", help="Print the correct filename")
	parser.add_argument('-v', '--verbose', dest='verbose', action="store_true", help="Print the result")
	parser.add_argument('-w','--write', dest='write', action="store_true", help="Write the file to the correct filename if necessary.")
	parser.add_argument('-r','--rename', dest='rename', action="store_true", help="Renames the file to the correct filename if necessary.")
	args = parser.parse_args()
	data=read(args.input_file)
	current_filename=get_filename(args.input_file)
	correct_filename=compute_filename(data)
	result=check(current_filename, correct_filename)
	
	if args.print:
		print(correct_filename)
	if result:
		if args.verbose:
			print("TRUE")
		exit(0)
	else:
		if args.verbose:
			print("FALSE")
		if args.write:
			write(data, get_basedir(args.input_file)+correct_filename)
		if args.rename:
			os.rename(args.input_file, get_basedir(args.input_file)+correct_filename)
		exit(1)


if __name__ == '__main__':
	main()
