#! /usr/bin/python

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open("encrypted.pdf", 'rb'))

print pdfReader.isEncrypted

pdfReader.decrypt('rosebud')

print pdfReader.getPage(0)
