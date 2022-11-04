import json
import xmltodict
import sys
import logging


def run(inpfilename):
    filecontent=open(inpfilename).read()
	
    xmlparser=xmltodict.parse(filecontent)

    jso = json.dumps(xmlparser)
    jso = jso.replace('@',").replace('#',")

    with open('outputfile1.ndl','w') as fileto:
        fileto.write(jso)

# Just to rn this command
# bq load -autodetect=true -source_format=NEWLINE_DELIMITED_JSON ctestmigration.errortable.outputfile.ndl

if __name__=='__main__':
	filename = sys.argv[1]
	run(filename)
