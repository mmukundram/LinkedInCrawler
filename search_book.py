# Import NLTK books and search for words

from nltk.book import *

text7.concordance("shares")

text7.similar("shares")

text7.common_contexts(["shares","stocks"])

text7.dispersion_plot(["shares","stocks"])
