import docx2txt as d2t

dFile = "somefile.docx"
tFile = "somefile.txt"

doc = d2t.process(dFile)

file=open(tFile, 'w')
file.write(doc)
file.close()

print('converted')

#este ejemplo sirve para convertir documentos word a txt
