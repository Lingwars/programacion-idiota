#!/usr/bin/env python
# coding: utf-8

# Información sobre el matcher de spacy y ejemplos de código: https://spacy.io/usage/rule-based-matching#matcher

import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

#Creo el patrón que queremos buscar y lo añado al matcher- POS = Part of Speech
pattern = [{"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADJ"}]
matcher.add("det_sust_adj", None, pattern) #arguments: match_id, on_match, *patterns

# Algunos títulos de pueba para comprobar el código más adelante.
grupos = "La monja enana, La oreja de Van Gogh, Jarabe de palo, Amaral, \
La casa azul, Los planetas, La quinta estación, Los toreros muertos, Hombres G"

# Proceso el texto usando nlp() y lo paso por el matcher.
doc = nlp(grupos)
matches = matcher(doc)

# Imprimir los nombres y otra info de los matches que se hayan encontrado
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Esto imprime el patrón al que responde el match, por si hay más de uno 
    span = doc[start:end]  # El span del match dentro del texto
    print(match_id, string_id, start, end, span.text)

"""
El resultado debería verse así:
2052584671301345654 det_sust_adj 0 3 La monja enana
2052584671301345654 det_sust_adj 16 19 La casa azul
2052584671301345654 det_sust_adj 27 30 Los toreros muertos
"""


