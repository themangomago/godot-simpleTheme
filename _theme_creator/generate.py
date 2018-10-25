#!/usr/bin/python
import sys, getopt, re
import xml.etree.ElementTree as ET


def main(argv):
	inputFile = ''
	try:
		opts, args = getopt.getopt(argv, 'hi:', ['input=', 'help'])
	except getopt.GetoptError:
		print('error: generate.py -i <xml file>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('help: generate.py -i <xml file>')
			sys.exit()
		elif opt in '-i':
			inputFile = arg

	try:
		tree = ET.parse(inputFile)
	except:
		print('cant open file: '+str(inputFile))
		sys.exit(2)
	root = tree.getroot()

	#Read from Template
	templateStr = open('_templateTheme.tpl', 'r').read()
	#RegEx Tag
	reTag = '<(.*?)>'

	for element in re.findall(reTag, templateStr):
		#print(element)
		templateStr = templateStr.replace('<'+element+'>', root.find(element).text)

	#print(templateStr)

	#Write Theme
	open('simpleTheme.tres', 'w').write(templateStr)


if __name__ == "__main__":
    main(sys.argv[1:])