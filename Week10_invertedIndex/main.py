"""
    This program show the three operation of inverted index
"""

txt1 = None
txt2 = None

def load():
    global txt1
    global txt2
    with open('text1.txt', 'r') as f:
        txt1 = f.readline().split()
    with open('text2.txt', 'r') as f:
        txt2 = f.readline().split()

def conjunction(order1, order2):
    """
        Return the intersection of two list
        The time complexity is O( len(order1) + len(order2) )

        Arg:    order1  - The words list of the txt1
                order2  - The words list of the txt2
        Ret:    The intersection list result
    """
    orderList1 = list(sorted(set(order1)))
    orderList2 = list(sorted(set(order2)))
    i = 0
    j = 0
    res = []
    while True:
        if i >= len(orderList1) or j >= len(orderList2):
            break
        if orderList1[i] == orderList2[j]:
            res.append(orderList1[i])
            i += 1
            j += 1
        else:
            if orderList1[i] > orderList2[j]:
                j += 1
            else:
                i += 1
    return res

def negation(order1, order2):
    """
        Return the negation result
        The result would include the element of order1 except the element that also appear in order2
        The time complexity is O( len(order1) + len(order2) )

        Arg:    order1  - The words list of the txt1
                order2  - The words list of the txt2
        Ret:    The negation list result
    """
    orderList1 = list(sorted(set(order1)))
    orderList2 = list(sorted(set(order2)))
    i = 0
    j = 0
    res = []
    while True:
        if i >= len(orderList1) or j >= len(orderList2):
            if i < len(orderList1):
                res.append(orderList1[i])
            break
        if orderList2[j] < orderList1[i]:
            j += 1
        else:
            if orderList2[j] > orderList1[i]:
                res.append(orderList1[i])
                i += 1
            else:
                i += 1
                j += 1
    return res

def disjunction(order1, order2):
    """
        Return the union of two list
        The time complexity is O( len(order1) + len(order2) )

        Arg:    order1  - The words list of the txt1
                order2  - The words list of the txt2
        Ret:    The union list result
    """
    orderList1 = list(sorted(set(order1)))
    orderList2 = list(sorted(set(order2)))
    i = 0
    j = 0
    res = []
    while True:
        # Escape condition
        if i >= len(orderList1):
            if j < len(orderList2):
                for k in range(j, len(orderList2)):
                    res.append(orderList2[k])
            break
        if j >= len(orderList2):
            if i < len(orderList1):
                for k in range(i, len(orderList1)):
                    res.append(orderList1[k])
            break

        # Add the element in valid condition
        if orderList1[i] < orderList2[j]:
            res.append(orderList1[i])
            i += 1
        elif orderList1[i] == orderList2[j]:
            res.append(orderList1[i])
            i += 1
            j += 1
        elif orderList1[i] > orderList2[j]:
            res.append(orderList2[j])
            j += 1
    return res


if __name__ == "__main__":
    load()
    print "txt1 words: ", txt1
    print "txt2 words: ", txt2
    print "\n--------------------------------------\n"
    print "conjunction: ", conjunction(txt1, txt2)
    print "disjunction: ", disjunction(txt1, txt2)
    print "negation1  : ", negation(txt1, txt2)
    print "negation2  : ", negation(txt2, txt1)