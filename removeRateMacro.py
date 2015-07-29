import sys
import re

def main():

	filename = str(sys.argv[1])

	fileContents = ""

	originalFile = open(filename, 'r+')

	for line in originalFile:
		fileContents+=line
	
	match = re.sub(re.compile('(<tr>\n<th><p>Rate</p></th>\n<td>)*<ac:macro ac:name="rate" />(</td>\n</tr>)*', re.MULTILINE),"",fileContents)

	deleteContent(originalFile)
	originalFile.write(match)

	originalFile.close()

def deleteContent(afile):
    afile.seek(0)
    afile.truncate()

main()
