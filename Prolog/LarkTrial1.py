from lark import Lark, Transformer
import textwrap

def parseprint(p):
    #print(p.pretty())
    print(textwrap.fill(str(p), 80))


demo_grammar_1 = '''
lines: line*
line: num movie_name year
num: /\d+/
movie_name: " " /[\w:,' ]+/
year: "(" /\d{4}/ ")"
%import common.WS
%ignore WS
'''

def theParse(inp):
    p = Lark(demo_grammar_1, start='lines')
    result = p.parse(inp)
    res2 = MovieTransformer().transform(result)
    parseprint(res2)

lines = '''
1 The Shawshank Redemption (1994)
2 The Godfather (1972)
3 The Godfather: Part II (1974)
4 Pulp Fiction (1994)
5 The Good, the Bad and the Ugly (1966)
6 The Dark Knight (2008)
7 12 Angry Men (1957)
8 Schindler's List (1993)
9 The Lord of the Rings: The Return of the King (2003)
10 Fight Club (1999)
'''
def main():
    theParse(lines)

class MovieTransformer(Transformer):
    def num(self, kids):
        return int(kids[0].value)
    def year(self, kids):
        return int(kids[0].value)
    def movie_name(self, kids):
        return kids[0].value.strip()
    def line(self,kids):
        return kids
    def lines(self,kids):
        return [kid for kid in kids if kid[2] < 1990]

if __name__ == '__main__':
  main()