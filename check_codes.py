"""Check every code in codes.json (plain Python, no dependencies).
GC table: words of length n over ACGT, distinct, exactly w letters in {C,G}, pairwise Hamming distance >= d.
GCRC table: additionally Hamming(x, revcomp(y)) >= d for ALL codewords x, y including x == y.
usage: python check_codes.py [codes.json]"""
import json, os, sys
from itertools import combinations

COMP = {"A": "T", "T": "A", "C": "G", "G": "C"}


def ham(a, b):
    return sum(x != y for x, y in zip(a, b))


def rc(s):
    return "".join(COMP[c] for c in reversed(s))


path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "codes.json")
bad = 0
for name, c in json.load(open(path)).items():
    W, n, d, w = c["words"], c["n"], c["d"], c["w"]
    ok = len(W) == len(set(W)) == c["size"]
    ok &= all(len(x) == n and set(x) <= set("ACGT") and sum(ch in "CG" for ch in x) == w for x in W)
    ok &= min(ham(a, b) for a, b in combinations(W, 2)) >= d
    if c["table"] == "GCRC":
        R = [rc(y) for y in W]
        ok &= min(ham(x, r) for x in W for r in R) >= d
    bad += not ok
    print(f"{name}: size {len(W)} {'OK' if ok else 'FAILED'}", flush=True)
print("all codes valid" if not bad else f"{bad} codes FAILED")
