import sys, os
import sets

def X(list1, list2):
    """
        Do the cartesian product toward 2 list
        For example, two list [A, B] [C, B] want to merge.
        The result: [AC, AB, BC, BB]

        Arg:    The two list want to merge
        Ret:    The result list
    """
    res = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            res.append(list1[i]+list2[j])
    return res

class CNF(object):
    """
        The class define the tuple and operation of chomskey normal form
    """
    alpha = []  # The start symbol of the rule
    beta  = []  # The endding symbol of the rule

    def rule(self, _r = "S -> A|B"):
        """
            Enter the grammar rule
            The keyin grammar should follow the format:
            <one_non_terminal_symbol><space>"->"<space>
            <symbol>"|"<symbol>"|"<symbol>"|"<symbol>

            Notice:
            1. There're only 2 space near the '->' symbol
            2. Each right symbol split just by '|' symbol

            Arg:    The string description of the grammar rule  
        """
        _alpha = []
        _beta  = []

        # Split the main character and '->' symbol
        _r = _r.split(' ')
        if not _r[1] == '->':
            print "Not the CFG format: ", _r[1]
            return None

        # Split the rest symbol at the right hand side
        terminal = _r[2].split('|')
        for i in range(len(terminal)):
            _alpha.append(_r[0])
        for i in range(len(terminal)):
            _beta.append(terminal[i])

        # Merge into the origin
        for i in range(len(terminal)):
            self.alpha.append(_alpha[i])
        for i in range(len(terminal)):
            self.beta.append(_beta[i])

        """
        print self.alpha
        print self.beta
        """

    def reverse(self, _list):
        """
            Reverse the origin symbol by the known rules
            For example, if there're 2 rules A -> B and S -> A
            Besides, the input list is like [A, B]
            Thus, the output list is [S, A]

            Arg:    The list contain the symbols want to reverse
            Ret:    The reversed list
        """
        _res = []
        for i in range(len(_list)):
            for j in range(len(self.beta)):
                if _list[i] == self.beta[j]:
                    _res.append(self.alpha[j])
        if len(_res) == 0:
            return [' ']
        else:
            return _res

class Table(object):
    """
        The 2D square array table object to deal with the CYK
    """
    size = -1   # The size of the array
    table = []

    def __init__(self, length):
        self.size = length

        # Create the origin table list with the specific length
        for i in range(self.size):
            _ = []
            for j in range(self.size):
                _.append([' '])
            self.table.append(_)

    def _set(self, i, j, _list):
        """
            Set the list information to the corresponding position

            Arg:    The coordination(i, j) and the list want to insert
            Ret:    None
        """
        if (len(self.table[i][j]) == 1 and self.table[i][j] == [' '])\
            or len(self.table[i][j]) == 0:
                self.table[i][j] = _list
                #print "set ( ", i, " , ", j, " )", _list
        elif not _list[0] == ' ':
            _set = set(self.table[i][j])
            for c in _list:
                _set.add(c)
            self.table[i][j] = list(_set)
            #print "append ( ", i, " , ", j, " )", _list
        

    def _get(self, i, j):
        """
            Get the list information from the corresponding position

            Arg:    The coordination(i, j)
            Ret:    The contain list
        """
        return self.table[i][j]

    def show(self):
        """
            Print the table object in the better format
        """
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                print self.table[i][j],
                for k in range(0, 3-len(self.table[i][j])):
                    print "\t",
            print ""


def test_addRule():
    """
        Test function to add the grammar rules
    """
    cnf = CNF()
    cnf.rule("S -> AB|BC")
    cnf.rule("A -> BA|a")
    cnf.rule("B -> CC|b")
    cnf.rule("C -> AB|a")

def CYK(cnf, string):
    """
         Cocke-Younger-Kasami algorithm implementation

         Arg:   The CNF object and the string want to test
    """
    # Initialize the variable
    table = Table(len(string)+1)

    # Insert the origin string
    for i in range(1, len(string)+1):
        table._set(i, 0, string[i-1])
    

    # Calculate the first level
    for i in range(1, len(string)+1):
        origin = cnf.reverse( table._get(i, 0) )
        table._set(i, 1, origin)
    print " -----------> Origin"
    table.show()

    # CYK O(n^3) algorithm
    length = len(string)
    for i in range(2, length+1):
        print " -----------> Row = ", i
        for j in range(1, length+2-i):
            for k in range(0, i-1):
                #print "( ", j, " , ", k+1, " ) => ", table._get(j, k+1)
                #print "( ", j+k+1, " , ", i-k-1, " ) => ", table._get(j+k+1, i-k-1)
                mul = X(table._get(j, k+1), table._get(j+k+1, i-k-1))
                _mul = cnf.reverse(mul)
                table._set(j, i, _mul)
        print ""
        table.show()
        print ""

    # Tell the result
    print "---------- CYK Result ----------"
    if table._get(1, length) == [' ']:
        print "String ( ", string, " ) is invalid CFG format"
    else:
        print "String ( ", string, " ) is valid CFG format"
        print "Origin String: ", table._get(1, length)
    

if __name__ == "__main__":
    # Construct the rule of chomskey normal form
    cnf = CNF()
    cnf.rule("S -> AB|BC")
    cnf.rule("A -> BA|a")
    cnf.rule("B -> CC|b")
    cnf.rule("C -> AB|a")

    # Judge if the string is a valid CFG format string
    strWantToParse = "baaba"
    CYK(cnf, strWantToParse)