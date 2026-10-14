# Improved lower bounds for DNA codes with constant GC-content (2026-10-14)

39 new lower bounds for the tables of Gaborit and King (https://rambutan.umassmed.edu/king/dnacodes.html, last updated
2010-06-23): codes of length n over {A,C,G,T} with minimum Hamming distance d and exactly w = floor(n/2) letters in {C,G}
(table A4^GC), and additionally d(x, rc(y)) >= d for all codewords x, y including x = y, where rc is the reverse
complement (table A4^GC,RC).

| parameters (n,d,w) | King table (2010) | best later value found in the literature | new |
|---|---:|---:|---:|
| A4^GC(7,3,3) | 288 | - | **292** |
| A4^GC(7,4,3) | 78 | - | **80** |
| A4^GC(8,3,4) | 1056 | - | **1120** |
| A4^GC(8,4,4) | 256 | - | **272** |
| A4^GC(9,3,4) | 3012 | - | **3072** |
| A4^GC(9,4,4) | 555 | - | **613** |
| A4^GC(9,5,4) | 134 | - | **158** |
| A4^GC(9,6,4) | 48 | - | **54** |
| A4^GC(10,6,5) | 116 | 144 (Aboluion 2011) | **152** |
| A4^GC(10,7,5) | 34 | - | **44** |
| A4^GC(11,4,5) | 7392 | - | **7552** |
| A4^GC(11,7,5) | 75 | - | **80** |
| A4^GC(11,8,5) | 32 | - | **33** |
| A4^GC(12,9,6) | 24 | - | **28** |
| A4^GC(13,8,6) | 134 | - | **137** |
| A4^GC(13,9,6) | 46 | - | **48** |
| A4^GC(13,10,6) | 20 | - | **21** |
| A4^GC,RC(7,3,3) | 135 | - | **138** |
| A4^GC,RC(8,3,4) | 528 | - | **560** |
| A4^GC,RC(8,4,4) | 128 | - | **136** |
| A4^GC,RC(8,5,4) | 28 | - | **30** |
| A4^GC,RC(9,3,4) | 1354 | - | **1536** |
| A4^GC,RC(9,4,4) | 275 | - | **314** |
| A4^GC,RC(9,5,4) | 67 | - | **75** |
| A4^GC,RC(10,4,5) | 855 | 860 (Aboluion 2011/2012) | **980** |
| A4^GC,RC(10,6,5) | 54 | - | **64** |
| A4^GC,RC(10,7,5) | 17 | - | **20** |
| A4^GC,RC(11,3,5) | 14405 | - | **14784** |
| A4^GC,RC(11,4,5) | 2457 | - | **2662** |
| A4^GC,RC(11,5,5) | 477 | - | **572** |
| A4^GC,RC(11,6,5) | 117 | - | **132** |
| A4^GC,RC(12,7,6) | 87 | - | **100** |
| A4^GC,RC(12,8,6) | 29 | - | **62** |
| A4^GC,RC(13,7,6) | 206 | - | **209** |
| A4^GC,RC(13,8,6) | 62 | - | **67** |
| A4^GC,RC(14,9,7) | 49 | - | **52** |
| A4^GC,RC(14,10,7) | 20 | - | **26** |
| A4^GC,RC(15,8,7) | 347 | - | **395** |
| A4^GC,RC(16,12,8) | 24 | - | **26** |

Literature checked: Chee-Ling 2008, Montemanni-Smith 2008/2009 (already in the 2010 table), Aboluion's 2011 thesis /
Aboluion-Smith-Perkins, Discrete Math. 312 (2012) (via the thesis tables), Montemanni-Smith-Koul 2014 (as reported in the
thesis), Sangroniz-Martinez 2019, and later algebraic/metaheuristic papers (most use different constraints and are not
comparable). Cells where a later paper already had a larger code were left out.

## Construction
Each code is a union of orbits of a group G of symmetries that preserve GC-content and distance (coordinate permutations
such as cyclic, dihedral and affine maps, the letter swaps A<->T and C<->G, and reverse-complement), found by exact orbit
enumeration, a maximum-weight clique search on the orbit compatibility graph, and word-level polishing. The group used for
each code is recorded in codes.json ("construction").

## Files and verification
- codes/<table>_n<n>_d<d>.txt: one codeword per line; codes.json: all codes with parameters.
- check_codes.py: plain-Python checker (GC weight, pairwise Hamming distance, and the reverse-complement condition).
  Run `python check_codes.py` (checks every code in codes.json; the largest codes take a few minutes in plain Python).
All codes were verified by two independently written checkers.

## Credit
Oscar (GitHub owhs), using an automated search harness built with Claude (Anthropic); the search code for this table was
written and run by a Claude (Opus) agent within that harness.
