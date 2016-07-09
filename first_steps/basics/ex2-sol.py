#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

text=raw_input("taper le texte à crypter \n")
LetterToId=dict()
IdToLetter=dict()
j=1
import string
for i in string.ascii_lowercase:
	LetterToId[i]=j
	IdToLetter[j]=i
	j+=1

SpecialChar={'/':')',':':'(',' ':'/','\"':'<','\'':'>','(':':',')':' ','<':'\"','>':'\''}

word=""
crypt=""
i=0
liste=text.split()

while i < len(liste):
	for lettre in liste[i]:
		if lettre in string.ascii_lowercase:
			word+=IdToLetter[((LetterToId[lettre]+3)%26)]
		else:
			word+=SpecialChar[lettre]
	crypt+=word+" "
	word=""
	i+=1

print(crypt)

