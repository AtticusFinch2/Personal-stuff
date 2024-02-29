
class symbol:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self):
        return (f"Symbol {self.name}")
    def __str__(self):
        return (self.name)
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return isinstance(self, type(other)) and self.name == other.name
class Var(symbol):
    def __repr__(self):
        return (f"Variable {self.name}")
    def __str__(self):
        return (self.name)
    def __hash__(self):
        return hash(self.name)
class Atom(symbol):
    def __repr__(self):
        return (f"(Atom: {self.name})")
    def __str__(self):
        return (self.name)
class Descriptor(symbol):
    pass
class Relation():
    def __repr__(self):
        return (f"Relation {self.d}, args: {self.args}")
    def __init__(self, descrip, *args):
        self.d = descrip
        self.args = list(args)


def test_str_output():
    a = Atom("docmo")
    assert str(a) == "docmo"

def test_repr_output():
    a = Atom("docmo")
    assert repr(a) == "(Atom: docmo)"



def unifyBasic(item1, item2, bindings): # horrible written code, just for case simplicity
    if isinstance(item1, Atom) and isinstance(item2,Atom):
        return None if item1.name != item2.name else {}
    if isinstance(item1, Var) and isinstance(item2, Var):
        return bindVarToVar(item1, item2, bindings)
    else:
        return bindVarToAtom(item1, item2, bindings)


def bindVarToAtom(input1, input2, bindings):
    trueValue = None
    if isinstance(input1, Atom) and isinstance(input2, Var):
        if input2 in bindings:
            trueValue = recurseUntilAtom(input2, bindings)
        if not trueValue:
            bindings[input2] = input1
            return bindings
        if input2 == trueValue:
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
        bindings = bindVarToAtom(trueArg2, arg1)
    else:  # arg 1 has been assigned
        bindings = bindVarToAtom(trueArg1, arg2)
    return bindings

def recurseUntilAtom(cur, bindings):
    visited = set()
    while not isinstance(cur, Atom) and cur not in visited:
        # we are guaranteed for cur to be in bindings, but we can still loop on ourselves.
        cur = bindings[cur]
    return cur if isinstance(cur, Atom) else None


def recurseUnify(fact1, fact2, bindings):
    temp = unify(fact1, fact2, bindings=bindings)
    return temp if temp else None

def unify_basic(f1, f2):
    # since python's GC will leave 'bindings' as what it was when it was last called,
    # we need to use this function as a shell when we want to only pass in 2 args
    return unify(f1, f2, bindings={})
def unify(fact1, fact2, bindings = {}):
    #print(fact1, fact2, bindings)
    if not (isinstance(fact1, Relation) and isinstance(fact2, Relation)):
        return unifyBasic(fact1, fact2, bindings)
    if fact1.d != fact2.d:  # different name
        return None
    if len(fact1.args) != len(fact2.args):  # length of args is different, not supposed to happen so throw KeyError
        return None
    if not (fact1.args and fact2.args):  # if either is empty
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
        print(f"mismatched arguments in unify() at {repr(fact1)}, {repr(fact2)}")
        return None


def test_unify_basic_1a():
    five = Atom("5")
    seven = Atom("7")
    assert unify_basic(five, seven) is None


def test_unify_basic_1b():
    fiveA = Atom("5")
    fiveB = Atom("5")
    assert unify_basic(fiveA, fiveB) == {}


def test_unify_basic_2():
    five = Atom("5")
    X = Var("X")
    assert unify_basic(five, X) == {X: five}


def test_unify_basic_3():
    Y = Var("Y")
    seven = Atom("7")
    assert unify_basic(Y, seven) == {Y: seven}


def test_unify_basic_4():
    X = Var("X")
    Y = Var("Y")
    assert unify_basic(X, Y) == {X: Y, Y: X}


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
    assert unify_basic(rel1, rel2) is None


def test_unify_recursive_bindings_4():
    five = Atom("5")
    X = Var("X")
    fact = Descriptor('fact')
    rel1 = Relation(fact, X, X)
    rel2 = Relation(fact, five, five)
    assert unify_basic(rel1, rel2) == {X: five}


def test_unify_recursive_bindings_5():
    five = Atom("5")
    six = Atom("6")
    X = Var("X")
    fact = Descriptor('fact')
    rel1 = Relation(fact, X, X)
    rel2 = Relation(fact, five, six)
    assert unify_basic(rel1, rel2) is None


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
    assert unify_basic(rel1b, rel2b) == answer


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
