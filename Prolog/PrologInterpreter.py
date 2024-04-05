import copy


class symbol:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self):
        return (f"Symbol {self.name}")
    def __str__(self):
        return (self.name)
    def __hash__(self):
        return hash(f"symbol {self.name}")
    def __eq__(self, other):
        return isinstance(self, type(other)) and self.name == other.name
class Var(symbol):
    def __repr__(self):
        return (f"Variable {self.name}")
    def __str__(self):
        return (self.name)
    def __hash__(self):
        return hash(f"Var {self.name}")
class Atom(symbol):
    def __repr__(self):
        return (f"Atom: {self.name}")
    def __str__(self):
        return (self.name)
    def __hash__(self):
        return hash(f"Atom {self.name}")
class Descriptor(symbol):
    pass
class Relation:
    def __repr__(self):
        return f"Relation {self.d}, args: {self.args}"
    def __str__(self):
        return f"(Relation {self.d}, args: {self.args})"
    def __init__(self, descrip, *args, isListOfArgs = None):
        self.d = descrip
        self.args = list(args) if isListOfArgs is None else args

class Clause:
    def __repr__(self):
        return f"(Clause {self.head} with *rest: {self.rest})"
    def __str__(self):
        return f"(Clause {self.head} with *rest: {self.rest})"
    def __init__(self, head, *rest, isRestAsArray = None):
        self.head = head
        if isRestAsArray is None:
            self.rest = [] if rest is None else rest
        else:
            self.rest = rest[0]




def test_unify_recursive_bindings_7():
    dry = Descriptor("dry")
    cb = Atom("cardboard_box")
    X = Var("X")
    dry_box = Relation(dry, cb)
    dry_X = Relation(dry, X)
    answer = {X:cb}
    assert unify(dry_X, dry_box) == answer


def prove(database, the_relation, bindings=None):
    bindings = {} if bindings is None else copy.deepcopy(bindings)
    ans = []
    for clause in database:
        #print(clause, the_relation)
        if clause.head.d == the_relation.d:
            if clause.head.args == the_relation.args:  # if the relation is already in the database
                return [{}]

            newBindings = unify(clause.head, the_relation, bindings)
            if newBindings is not None:

                # print(f"\n{clause} \n with bindings:{bindings}")
                # print(f"and relation: {the_relation} \n and newBindings: {newBindings}")

                if not clause.rest:  # if clause is a fact
                    ans.append(newBindings)
                    continue

                for req in clause.rest:
                    possible_solutions = prove(database, req, newBindings)

                    if possible_solutions:
                        for binding in possible_solutions:
                            merging_bindings = newBindings.copy()
                            merging_bindings.update(binding)
                            ans.append(merging_bindings)
    return ans


def make_clause_1():
    # Statement of the fact that sand is dry.
    # dry(sand).
    d = Descriptor("dry")
    s = Atom("sand")
    rel = Relation(d, s)
    clause = Clause(rel)
    return clause


def make_clause_2():
    # Statement of rule
    # dry(X) :- stage2(X).
    dry = Descriptor("dry")
    stage2 = Descriptor("stage2")
    X = Var("X")

    rel1 = Relation(dry, X)
    rel2 = Relation(stage2, X)

    clause = Clause(rel1, rel2)
    return clause

def make_clause_3():
    # Statement of the fact that sand is dry.
    # no_water(cardboard_box).
    d = Descriptor("no_water")
    s = Atom("cardboard_box")
    rel = Relation(d, s)
    clause = Clause(rel)
    return clause
def test_prove_one_1():
    database = []
    database.append(make_clause_1())
    database.append(make_clause_2())
    database.append(make_clause_3())

    stage2 = Descriptor("stage2")
    no_water = Descriptor("no_water")
    Z = Var("Z")

    rel1 = Relation(stage2, Z)
    rel2 = Relation(no_water, Z)

    database.append(Clause(rel1, rel2))

    # dry(sand).
    # dry(X) :- stage2(X).
    # no_water(cardboard_box).
    # stage2(Z) :- no_water(Z).
    # want to prove dry(cardboard_box)

    dry = Descriptor("dry")
    noWater = Descriptor("no_water")
    cb = Atom("cardboard_box")
    sand = Atom("sand")
    dry_box = Relation(dry, cb)
    answer = prove(database, dry_box)
    assert answer == [{Var("X"): Atom("cardboard_box"), Var("Z"): Atom("cardboard_box")}]


def test_prove_one_2():
    # DATABASE HAS:
    # orange(X) :- theory().
    # theory().
    # Want to prove:
    # orange(juice).

    # With this database,
    # orange(juice) is true. with bindings {X = juice}
    # summer() is false because summer() does not appear anywhere is the database.
    # theory() is true because it is in the database.
    # Book writes that: theory/0

    orange = Descriptor('orange')
    theory = Descriptor('theory')
    X = Var('X')
    orangeX = Relation(orange, X)
    theoryBlank = Relation(theory)

    factOrange = Clause(orangeX, theoryBlank)
    factTheory = Clause(theoryBlank)

    db = [factOrange, factTheory]

    juice = Atom('juice')
    orange_juice = Relation(orange, juice)
    assert prove(db, orange_juice) == [{X: juice}]

    # second test showing things not in the database cannot be proven
    baloney = Descriptor('baloney')
    baloney_relation = Relation(baloney)
    assert prove(db, baloney_relation) == []


def test_prove_one_3():
    # DATABASE HAS:
    # orange(X) :- theory(X).
    # theory(Y) :- liquid(Y).
    # liquid(Z) :- no_pulp(Z).
    # no_pulp(juice).

    # Want to prove:
    # orange(juice).

    # With this database,
    # orange(juice) is true. with bindings {X = juice}
    # summer() is false because summer() does not appear anywhere is the database.
    # theory() is true because it is in the database.
    # Book writes that: theory/0

    orange = Descriptor('orange')
    theory = Descriptor('theory')
    liquid = Descriptor('liquid')
    no_pulp = Descriptor('no_pulp')
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    juice = Atom('juice')
    orangeX = Relation(orange, X)
    theoryX = Relation(theory, X)
    liquidY = Relation(liquid, Y)
    theoryY = Relation(theory, Y)
    liquidZ = Relation(liquid, Z)
    no_pulpZ = Relation(no_pulp, Z)
    no_pulp_juice = Relation(no_pulp, juice)

    fact1 = Clause(orangeX, theoryX)
    fact2 = Clause(theoryY, liquidY)
    fact3 = Clause(liquidZ, no_pulpZ)
    factNoPulp = Clause(no_pulp_juice)

    db = [fact1, fact2, fact3, factNoPulp]


    orange_juice = Relation(orange, juice)
    assert prove(db, orange_juice) == [{X: juice, Y:juice, Z:juice}]

    # second test showing things not in the database cannot be proven
    baloney = Descriptor('baloney')
    baloney_relation = Relation(baloney)
    assert prove(db, baloney_relation) == []


def test_prove_one_4():
    # DATABASE HAS:
    # orange(X) :- theory(X).
    # theory(Y) :- liquid(Y).
    # liquid(Z) :- no_pulp(Z).
    # no_pulp(juice).
    # orange(fruit) :- no_pulp(fruit).

    # Want to prove:
    # orange(juice).

    # With this database,
    # orange(juice) is true. with bindings {X = juice}
    # summer() is false because summer() does not appear anywhere is the database.
    # theory() is true because it is in the database.
    # Book writes that: theory/0

    orange = Descriptor('orange')
    theory = Descriptor('theory')
    liquid = Descriptor('liquid')
    no_pulp = Descriptor('no_pulp')
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    fruit = Var('fruit')
    juice = Atom('juice')
    orangeX = Relation(orange, X)
    theoryX = Relation(theory, X)
    liquidY = Relation(liquid, Y)
    theoryY = Relation(theory, Y)
    liquidZ = Relation(liquid, Z)
    no_pulpZ = Relation(no_pulp, Z)
    no_pulp_juice = Relation(no_pulp, juice)
    orangeFruit = Relation(orange, fruit)
    no_pulpFruit = Relation(no_pulp, fruit)

    fact1 = Clause(orangeX, theoryX)
    fact2 = Clause(theoryY, liquidY)
    fact3 = Clause(liquidZ, no_pulpZ)
    fact4 = Clause(no_pulp_juice)
    fact5 = Clause(orangeFruit, no_pulpFruit)

    db = [fact1, fact2, fact3, fact4, fact5]

    orange_juice = Relation(orange, juice)
    assert prove(db, orange_juice) == [{X: juice, Y: juice, Z: juice}, {fruit: juice}]

    # second test showing things not in the database cannot be proven
    baloney = Descriptor('baloney')
    baloney_relation = Relation(baloney)
    assert prove(db, baloney_relation) == []

def test_str_output():
    a = Atom("docmo")
    assert str(a) == "docmo"

def test_repr_output():
    a = Atom("docmo")
    assert repr(a) == "Atom: docmo"


def unifyBasic(item1, item2, bindings):  # horrible written code, just for case simplicity
    if isinstance(item1, Atom) and isinstance(item2,Atom):
        return None if item1.name != item2.name else {}
    if isinstance(item1, Var) and isinstance(item2, Var):
        return bindVarToVar(item1, item2, bindings)
    else:
        return bindVarToAtom(item1, item2, bindings)


def bindVarToAtom(input1, input2, bindings):  # this might be the worst function I have ever written
    trueValue = None
    if isinstance(input1, Atom) and isinstance(input2, Var):
        if input2 in bindings:
            trueValue = recurseUntilAtom(input2, bindings)
        if not trueValue:
            bindings[input2] = input1
            return bindings
        if input1 == trueValue:
            return bindings
        else:  # THERE IS ATOM MISMATCH
            return None
    else:
        if input1 in bindings:
            trueValue = recurseUntilAtom(input1, bindings)
        if not trueValue:
            bindings[input1] = input2
            return bindings
        if input2 == trueValue:
            return bindings
        else:  # THERE IS ATOM MISMATCH
            return None


def bindVarToVar(arg1, arg2, bindings):
    trueArg1 = None
    trueArg2 = None
    if arg1 in bindings:
        trueArg1 = recurseUntilAtom(arg1, bindings)
    if arg2 in bindings:
        trueArg2 = recurseUntilAtom(arg2, bindings)

    if trueArg1 and trueArg2:  # both vars have been assigned
        if trueArg2 != trueArg1:
            return None
    elif (not trueArg1) and (not trueArg2):  # neither var has been assigned
        bindings[arg1] = arg2
        bindings[arg2] = arg1
    elif trueArg2:  # arg 2 has been assigned
        bindings = bindVarToAtom(trueArg2, arg1, bindings)
    else:  # arg 1 has been assigned
        bindings = bindVarToAtom(trueArg1, arg2, bindings)
    return bindings


def recurseUntilAtom(cur, bindings):
    visited = set()
    while not isinstance(cur, Atom) and cur not in visited:
        # we are guaranteed for cur to be in bindings, but we can still loop on ourselves.
        #   prevent the loop by having a visited set
        cur = bindings[cur]
    return cur if isinstance(cur, Atom) else None


def recurseUnify(fact1, fact2, bindings):
    temp = unifyinner(fact1, fact2, bindings=bindings)
    return temp if temp else None


def unify(f1, f2, bindings=None):
    bindings = {} if bindings is None else copy.deepcopy(bindings)
    return unifyinner(copy.deepcopy(f1), copy.deepcopy(f2), bindings)

def unifyinner(fact1, fact2, bindings):
    if not (isinstance(fact1, Relation) and isinstance(fact2, Relation)):  # if we are not unifying relations
        return unifyBasic(fact1, fact2, bindings)
    if not (isinstance(fact1, Relation) and isinstance(fact2, Relation)):
        return unifyBasic(fact1, fact2, bindings)
    if fact1.d != fact2.d:  # different name
        return None
    if len(fact1.args) != len(fact2.args):  # length of args is different, not supposed to happen so can't do it
        return None
    if not (fact1.args and fact2.args):  # if either is empty, we are at the last recursion stage
        return bindings
    arg1 = fact1.args.pop()
    arg2 = fact2.args.pop()
    if isinstance(arg1, Atom) and isinstance(arg2, Atom):
        return recurseUnify(fact1, fact2, bindings) if arg1 == arg2 else None
    if isinstance(arg1, Atom) and isinstance(arg2,Var) or isinstance(arg2, Atom) and isinstance(arg1,Var):
        bindings = bindVarToAtom(arg1, arg2, bindings)
        return recurseUnify(fact1, fact2, bindings)
    if isinstance(arg1, Var) and isinstance(arg1, Var):
        bindings = bindVarToVar(arg1, arg2, bindings)
        return recurseUnify(fact1, fact2, bindings)
    if isinstance(arg1, Relation) and isinstance(arg2, Relation):
        if arg1.d == arg2.d:
            bindings = unify(arg1,arg2,bindings)
            return recurseUnify(fact1, fact2, bindings)
        return None
    else:
        print(f"mismatched arguments in unify() at {repr(fact1)}, {repr(fact2)} \n  arguments are: {repr(arg1)}, {repr(arg2)}")
        return None


def test_unify_basic_1a():
    five = Atom("5")
    seven = Atom("7")
    assert unify(five, seven) is None


def test_unify_basic_1b():
    fiveA = Atom("5")
    fiveB = Atom("5")
    assert unify(fiveA, fiveB) == {}


def test_unify_basic_2():
    five = Atom("5")
    X = Var("X")
    assert unify(five, X) == {X: five}


def test_unify_basic_3():
    Y = Var("Y")
    seven = Atom("7")
    assert unify(Y, seven) == {Y: seven}


def test_unify_basic_4():
    X = Var("X")
    Y = Var("Y")
    assert unify(X, Y) == {X: Y, Y: X}


def test_unify_basic_bindings_1():
    five = Atom("5")
    six = Atom("6")
    X = Var("X")
    bindings = {X: five}
    assert unify(X, five, bindings) == bindings


def test_unify_basic_bindings_2():
    five = Atom("5")
    six = Atom("6")
    X = Var("X")
    bindings = {X: five}
    assert unify(X, six, bindings) is None
def test_unify_recursive_bindings_3():
    five = Atom("5")
    six = Atom("6")
    X = Var("X")
    fact = Descriptor('fact')
    rel1 = Relation(fact, X, X)
    rel2 = Relation(fact, five, six)
    assert unify(rel1, rel2) is None


def test_unify_recursive_bindings_4():
    five = Atom("5")
    X = Var("X")
    fact = Descriptor('fact')
    rel1 = Relation(fact, X, X)
    rel2 = Relation(fact, five, five)
    assert unify(rel1, rel2) == {X: five}


def test_unify_recursive_bindings_5():
    five = Atom("5")
    six = Atom("6")
    X = Var("X")
    fact = Descriptor('fact')
    rel1 = Relation(fact, X, X)
    rel2 = Relation(fact, five, six)
    assert unify(rel1, rel2) is None


def test_unify_recursive_bindings_6():
    facta = Descriptor('facta')
    factb = Descriptor('factb')
    ten = Atom('10')
    thirty = Atom('30')
    fifty = Atom('50')
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    rel1a = Relation(factb, ten, fifty)
    rel1b = Relation(facta, X, Y, rel1a)
    rel2a = Relation(factb, X, Z)
    rel2b = Relation(facta, ten, thirty, rel2a)
    answer = {X: ten, Y: thirty, Z: fifty}
    assert unify(rel1b, rel2b) == answer





def test_unify_nested_relation_1():
    # facta(X, Y, factb(10, 50)) Unify this with:
    # facta(10, 30, factb(X, Z)) Yes
    # facta(80, 30, factb(X, Z)) No
    facta = Descriptor('facta')
    factb = Descriptor('factb')
    ten = Atom('10')
    thirty = Atom('30')
    eighty = Atom('80')
    fifty = Atom('50')
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    rel1 = Relation(facta, X, Y, Relation(factb, ten, fifty))
    rel2 = Relation(facta, ten, thirty, Relation(factb, X, Z))
    assert unify(rel1, rel2, bindings={}) == {X: ten, Y: thirty, Z: fifty}


def test_unify_nested_relation_2():
    # facta(X, Y, factb(10, 50)) Unify this with:
    # facta(10, 30, factb(X, Z)) Yes
    # facta(80, 30, factb(X, Z)) No
    facta = Descriptor('facta')
    factb = Descriptor('factb')
    ten = Atom('10')
    thirty = Atom('30')
    eighty = Atom('80')
    fifty = Atom('50')
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    rel1 = Relation(facta, X, Y, Relation(factb, ten, fifty))
    rel3 = Relation(facta, eighty, thirty, Relation(factb, X, Z))
    assert unify(rel1, rel3, bindings={}) is None
