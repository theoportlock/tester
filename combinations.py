#!/usr/bin/env python

import IO 
import tester
import binadder

def a(arr):
    out = []
    qry = [0]*len(arr)
    for j in range(2**len(qry)-1):
        qry = binadder.a(qry)
        matches = 1
        for i in range(len(qry)):
            if qry[i] and not arr[i]:
                matches = 0
        out.append(matches)
    return out

if __name__ == "__main__":
    run = tester.run(f=a,i=IO.bitarrin,o=IO.printerout,d=IO.elementnumberdec)
    run.excecute()
