#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

text=input("saisir texte")
dictionnaire=dict()
alphabet="abcdefghijklmnopqrstuvwxyz"
j=1
for i in alphabet:
	dictionnaire[i]=j
	j+=1

i=0 	
score=0
maxx=score
word=""
liste=text.split()
while i < len(liste):
	for lettre in liste[i]:
  		score=(score+dictionnaire[lettre])*len(liste[i])
 	if score>maxx:
  		word=liste[i]
	i+=1

print(word)


