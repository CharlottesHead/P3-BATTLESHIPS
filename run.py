import random

SHIPS_LENGTH = [2, 3, 3, 4, 5]
PLR_BRD = [[" "] * 8 for i in range(8)]
CPU_BRD = [[" "] * 8 for i in range(8)]
PLR_HIDDEN = [[" "] * 8 for i in range(8)]
CPU_HIDDEN = [[" "] * 8 for i in range(8)]
CONVERT = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}