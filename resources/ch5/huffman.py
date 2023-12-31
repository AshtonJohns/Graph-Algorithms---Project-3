#https://gist.github.com/nboubakr/0eec4ea650eeb6dc21f9


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Le codage de Huffman
# Théorie de l'information et du codage
# Etudiant: Boubakr NOUR <n.boubakr@gmail.com>
# Universite Djilali Liabes (UDL) de Sidi Bel Abbes

import heapq
from collections import defaultdict


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    print(heap)
    heapq.heapify(heap)
    print(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        #print('low =', lo)
        hi = heapq.heappop(heap)
        #print('hi =', hi)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        #print('\n', heap, '\n')
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


data = "The frog at the bottom of the well drifts off into the great ocean"
frequency = defaultdict(int)
for symbol in data:
    frequency[symbol] += 1

huff = encode(frequency)
print ("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff:
    print (p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
