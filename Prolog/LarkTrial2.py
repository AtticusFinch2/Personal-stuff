from lark import Lark, Transformer
import textwrap
import PrologInterpreter

def parseprint(p):
    #print(p.pretty())
    print(textwrap.fill(str(p), 160))


databaseGrammar = '''
lines: clause*
clause: fact "."
        | relation " :- " body+
body: relation ", "
      | relation "."
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
    print(res2)
    return res2
def parseQuery(inp):
    p = Lark(queryGrammar, start='query')
    result = p.parse(inp)
    res2 = QueryTransformer().transform(result)
    print(result.pretty(), db)
    #return res2


def main():
    global db
    db = parseDatabase(databaseLines)
    parseQuery(queryLines)

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
        return PrologInterpreter.Relation(head, *arguments)
    def body(self,kids):
        head, *k =kids
        return (head, *k)
    def fact(self, kids):
        return kids[0]
    def clause(self,kids):
        head, *body = kids
        return PrologInterpreter.Clause(head, *body)
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
        return PrologInterpreter.Relation(head, *arguments)
    def query(self,kids):
        resultBindings = PrologInterpreter.prove(db, kids[0])
        return resultBindings


databaseLines = '''
fact.
rule(X) :- requirement.
ruleB(X,Y) :- rule(X), rule(Y).
requirement.
'''
queryLines = '''
?ruleB(A,B).
'''
if __name__ == '__main__':
  main()