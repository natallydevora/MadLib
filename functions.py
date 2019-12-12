"""A collection of functions for doing my project."""

""" word types to fill in blanks of mad libs"""
# Fill each quote below with an adjective of your choice
adjective1 = ''
adj2 = ''
adj3 = ''
adj4 = ''

# Fill each quote below with a color of your choice
color = ''
color2 = ''

# Fill the quote below with a body part of your choice
body_part = ''

# Fill the quote below with a noun of your choice
noun = ''

# Fill the quote below with a number of your choice
number = ''

# Fill the quote below with animals of your choice
animals = ''

# Fill the quote below with a verb of your choice
verb = ''

# Fill each quote below with plural nouns of your choice
plural_noun = ''
p_n2 = ''
p_n3 = ''

""" functions to implement word choices """ 
"""variable prints word choice in sentence for mad lib"""

def blank_1(adjective1):
    output = 'Santa Clause is a ' + adjective1 + ' man '   
    return output 
lib1 = blank_1(adjective1)

def blank_2(adj2):
    output = 'who wears a ' + adj2 + ' '
    return output
lib2 = blank_2(adj2)

def blank_3(color):
    output = color + ' suit '
    return output
lib3 = blank_3(color)

def blank_4(adj3):
    output = 'with a ' + adj3 + ' belt '
    return output
lib4 = blank_4(adj3)

def blank_5(adj4):
    output = 'and a ' + adj4 + ' '
    return output
lib5 = blank_5(adj4)

def blank_6(color2):
    output = color2 + ' beard '
    return output
lib6 = blank_6(color2)

def blank_7(body_part):
    output = 'and his ' + body_part + ' shakes like jelly when he laughs. '
    return output
lib7 = blank_7(body_part)

def blank_8(noun):
    output = 'Every Christmas, he rides a ' + noun
    return output
lib8 = blank_8(noun)

def blank_9(number):
    output = ' full of presents, pulled by ' + number + ' '
    return output
lib9 = blank_9(number)

def blank_10(animals):
    output = animals + ' high into the night sky. '
    return output
lib10 = blank_10(animals)

def blank_11(verb):
    output = 'Santa ' + verb + ' down the chimney of homes '
    return output
lib11 = blank_11(verb)

def blank_12(plural_noun):
    output = 'to leave ' + plural_noun + ', '
    return output
lib12 = blank_12(plural_noun)

def blank_13(p_n2):
    output = p_n2 + ', '
    return output
lib13 = blank_13(p_n2)

def blank_14(p_n3):
    output = 'and ' + p_n3 + ' under Christmas trees.'
    return output
lib14 = blank_14(p_n3)

"""variable adds strings together to create mad lib story"""
xmas_mad_lib = lib1 + lib2 + lib3 + lib4 + lib5 + lib6 + lib7 + lib8 + lib9 + lib10 + lib11 + lib12 + lib13 + lib14
print(xmas_mad_lib)
