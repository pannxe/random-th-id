#!/usr/bin/env python

import random

# First digit is [1,8]
th_id = str(random.randint(1, 8))

# 2nd - 12th digits are [0,9]
th_id += "".join([str(random.randint(0, 9)) for i in range(11)])

# Check sum equation is 11 - sum(13*i1 + 12*i2 + ... + 2*i12)%11
th_id += str(11 - sum([i * int(th_id[13 - i]) for i in range(13, 1, -1)]) % 11)

print(th_id)
