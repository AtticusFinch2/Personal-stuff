
class symbol:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self):
        return (f"Symbol {self.name}")
    def __str__(self):
        return (f"Symbol {self.name}")
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return isinstance(self, type(other)) and self.name == other.name
class Var(symbol):
    def __repr__(self):
        return (f"Variable {self.name}")
    def __str__(self):
        return (f"Variable {self.name}")
    def __hash__(self):
        return hash(self.name)
class Atom(symbol):
    def __repr__(self):
        return (f"Atom {self.name}")
    def __str__(self):
        return (f"Atom {self.name}")
class descriptor(symbol):
    pass
class Relation():
    def __repr__(self):
        return (f"Relation {self.d}, args: {self.args}")
    def __init__(self, descrip, *args):
        self.d = descrip
        self.args = list(args)


def unifyBasic(item1, item2): # horrible written code, just for case simplicity
    if isinstance(item1, Var) and isinstance(item2,Atom):
        return {item1:item2}
    if isinstance(item2, Var) and isinstance(item1,Atom):
        return {item2:item1}
    if isinstance(item1, Atom) and isinstance(item2,Atom):
        return None if item1.name != item2.name else {}
    if isinstance(item1, Var) and isinstance(item2, Var):
        return {item1:item2, item2:item1}


def test_unify_basic_1a():
    five = Atom('5')
    seven = Atom('7')
    assert unifyBasic(five, seven) is None

def test_unify_basic_1b():
    five1 = Atom('5')
    five2 = Atom('5')
    assert unifyBasic(five1, five2) == {}

def test_unify_basic_2():
    five = Atom('5')
    X = Var('X')
    assert unifyBasic(five, X) == {X:five}

def test_unify_basic_3():
    X = Var('X')
    five = Atom('5')
    assert unifyBasic(X, five) == {X:five}

def test_unify_basic_4():
    X = Var('X')
    Y = Var('Y')
    assert unifyBasic(X, Y) == {X:Y, Y:X}

def bindVarToAtom(input1, input2, bindings):
    if isinstance(input1, Atom) and isinstance(input2, Var):
        if input2 in bindings:
            trueValue = recurseUntilAtom(input2, bindings)
        else:
            bindings[input2] = input1
            return bindings
        if input2 == trueValue:
            return bindings
        else:  # THERE IS ATOM MISMATCH
            return None
    else:
        if input1 in bindings:
            trueValue = recurseUntilAtom(input1, bindings)
        else:
            bindings[input1] = input2
            return bindings
        if input2 == trueValue:
            return bindings
        else:  # THERE IS ATOM MISMATCH
            return None

def recurseUntilAtom(cur, bindings):
    visited = set()
    while not isinstance(cur, Atom) and cur not in visited:
        # we are guaranteed for cur to be in bindings, but we can still loop on ourselves.
        cur = bindings[cur]
    return cur

def recurseUnify(fact1, fact2, bindings):
    temp = unify(fact1, fact2, bindings)
    if not temp:
        return None
    return temp

def unify(fact1 : Relation, fact2: Relation, bindings: map):
    if fact1.descriptor != fact2.descriptor:  # different name
        return None
    if len(fact1.args) != len(fact2.args):  # length of args is different, not supposed to happen so throw KeyError
        return None
    if not (fact1.args and fact2.args):  # if either is empty
        return bindings
    arg1 = fact1.args.popleft()
    arg2 = fact1.args.popleft()
    if isinstance(arg1, Atom) and isinstance(arg2, Atom):
        if arg1 == arg2:
            recurseUnify(fact1, fact2, bindings)
        else:
            return None
    if isinstance(arg1, Atom) and isinstance(arg2,Var) or isinstance(arg2, Atom) and isinstance(arg1,Var):
        bindVarToAtom(arg1, arg2, bindings)
        temp = unify(fact1, fact2, bindings)
        if not temp:
            return None
        return temp
    if isinstance(arg1, Var) and isinstance(arg1, Var):
        trueArg1 = None
        trueArg2 = None
        if arg1 in bindings:
            trueArg1 = recurseUntilAtom(arg1, bindings)
        if arg2 in bindings:
            trueArg2 = recurseUntilAtom(arg2, bindings)

        if trueArg1 and trueArg2:  # both vars have been assigned
            if trueArg2 != trueArg1:
                return None
            temp = unify(fact1, fact2, bindings)
            if not temp:
                return None
            return temp
        if (not trueArg1) and (not trueArg2):  # neither var has been assigned
            bindings[arg1] = arg2
            bindings[arg2] = arg1




