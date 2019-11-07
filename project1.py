# python -m spacy download en_core_web_lg

import spacy

nlp = spacy.load("en_core_web_lg")
doc = nlp(u"This is a sentence.")
# doc 
# This is a sentence.
"""
>>> doc[0]
This
>>> doc[0].pos
90
>>> doc[0].pos_
'DET'
"""


print([(w.text, w.pos_) for w in doc])

