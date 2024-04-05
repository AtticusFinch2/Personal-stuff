from lark import Lark, Transformer
import textwrap
import PrologInterpreter

def parseprint(p):
    #print(p.pretty())
    print(textwrap.fill(str(p), 160))


databaseGrammar = '''
lines: clause*
clause: fact "."
        | condition 
condition: relation " :- " body+ "."
body: relation ", "
      | relation
fact: relation

term: (", " | "," | ) (atom | var | num | relation)
atom: /[a-z][\w\d_]*/
var: /[A-Z][\w\d_]*/
num: /\d+/

relation: descriptor | descriptor "(" term+ ")"
descriptor: /[a-z][\w\d_]*/


%import common.WS
%ignore WS
'''
queryGrammar = '''
query: "?" relation "."

term: (", " | "," | ) (atom | var | num | relation)
atom: /[a-z][\w\d_]*/
var: /[A-Z][\w\d_]*/
num: /\d+/

relation: descriptor | descriptor "(" term+ ")"
descriptor: /[a-z][\w\d_]*/


%import common.WS
%ignore WS
'''

def parseDatabase(inp):
    p = Lark(databaseGrammar, start='lines')
    result = p.parse(inp)
    res2 = PrologTransformer().transform(result)
    print(f"==================database====================\n{result.pretty()}")
    return res2
def parseQuery(inp):
    p = Lark(queryGrammar, start='query')
    result = p.parse(inp)
    res2 = QueryTransformer().transform(result)
    print(f"\n===================queries===================\n{result.pretty()}")
    return res2


def main():
    global db
    db = parseDatabase(databaseLines)
    #print(db)
    bindings = parseQuery(queryLines)
    print(f"resulting bindings {bindings}")

class PrologTransformer(Transformer):
    def atom(self, kids):
        return PrologInterpreter.Atom(kids[0].value)
    def var(self, kids):
        return PrologInterpreter.Var(kids[0].value)
    def descriptor(self, kids):
        return PrologInterpreter.Descriptor(kids[0].value)
    def term(self, kids):
        return kids[0]
    def relation(self, kids):
        head, *arguments = kids
        #print(head, *arguments, kids)
        rel = PrologInterpreter.Relation(head, *arguments)
        #print(rel)
        return rel
    def body(self,kids):
        #print(f"body{kids}")
        return kids[0]
    def fact(self, kids):
        return PrologInterpreter.Clause(kids[0])
    def condition(self, kids):
        head, *body = kids
        #print("     ", head, *body)
        return PrologInterpreter.Clause(head, body, isRestAsArray=True)
    def clause(self,kids):
        #print(kids[0])
        return kids[0]
    def lines(self,kids):
        return kids  # this is a database

class QueryTransformer(Transformer):
    def atom(self, kids):
        return PrologInterpreter.Atom(kids[0].value)
    def var(self, kids):
        return PrologInterpreter.Var(kids[0].value)
    def descriptor(self, kids):
        return PrologInterpreter.Descriptor(kids[0].value)
    def term(self, kids):
        return kids[0]
    def relation(self, kids):
        head, *arguments = kids
        rel = PrologInterpreter.Relation(head, *arguments, isListOfArgs=None)
        return rel
    def query(self,kids):
        resultBindings = PrologInterpreter.prove(db, kids[0])
        return resultBindings


databaseLines = '''
dry(sand).
dry(X) :- stage2(X).
no_water(cardboard_box).
stage2(Z) :- no_water(Z).
'''
queryLines = '''
?dry(cardboard_box).
'''
if __name__ == '__main__':
  main()