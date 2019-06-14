#!/usr/bin/env python

import json, sys

events = json.loads(sys.stdin.read())["traceEvents"]
codegens = filter(lambda x: x["name"] == "CodeGen Function", events)
frontends = filter(lambda x: x["name"] == "Frontend", events)

def is_inside(range1, range2):
    a = range1["ts"]; b = a + range1["dur"]
    c = range2["ts"]; d = c + range2["dur"]
    return (a >= c and a <= d) and (b >= c and b <= d)

if not all([any([is_inside(codegen, frontend) for frontend in frontends])
            for codegen in codegens]):
    sys.exit("Not all CodeGen blocks are inside any of Frontend blocks!")
