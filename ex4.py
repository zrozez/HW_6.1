palindromes = ['hello', 'sentences where punctuation', 45,
            'Able was I, ere I saw Elba', 34.0, 78.87, 'found', 
            'level', '12/11/21', 'radar','stats']

pal = list(filter(lambda x:(str(x).upper()==str(x).upper()[::-1]), palindromes))

