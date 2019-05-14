## The Algorithm
The central problem is, given an integer whose digits we KNOW add up to 10, how can we easily
find the next greatest integer?

#### The Basic Process
Let's look at a subsequence of special numbers:
2331100
2332000
2340001
2340010
2340100
2341000
2350000
2400004

This sequence actually contains everything we need to know to develop an algorithm. Let's break it up even further:

---
| | A | B | C | D | E | F | G |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
(i) | 2 | 3 | 3 | 1 | 1 | 0 | 0 |
(ii) | 2 | 3 | 3 | 2 | 0 | 0 | 0 |

Here we've broken up each digit into a named column for easier reference. Row (i) contains the digits of the first number of the sequence, and row (ii) contains the second number. The transition from the first the second, in this case, is accomplished by changing column E from 1 to0, and column D from 1 to 2.

---
|| A | B | C | D | E | F | G |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
(ii)| 2 | 3 | 3 | 2 | 0 | 0 | 0 |
(iii) | 2 | 3 | 4 | 0 | 0 | 0 | 1 |

The transition from (ii) to the (iii) is more complicated. C gains 1, D loses 2, and G gains 1.

---
|| A | B | C | D | E | F | G |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
(iii)| 2 | 3 | 4 | 0 | 0 | 0 | 1 |
(iv) | 2 | 3 | 4 | 0 | 0 | 1 | 0 |

Back to the simple transition: F is incremented while G is decremented.

---
|| A | B | C | D | E | F | G |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
(iv)| 2 | 3 | 4 | 0 | 0 | 1 | 0 |
(v)| 2 | 3 | 4 | 0 | 1 | 0 | 0 |

Simple again: Now E is incremented and F is decremented.

---
|| A | B | C | D | E | F | G |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
(v)| 2 | 3 | 4 | 0 | 1 | 0 | 0 |
(vi)| 2 | 3 | 4 | 1 | 0 | 0 | 0 |

Another simple transition (you're probably noticing a pattern now). D is incremented while E is decremented.

---
|| A | B | C | D | E | F | G |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
(vi)| 2 | 3 | 4 | 1 | 0 | 0 | 0 |
(vii)| 2 | 3 | 5 | 0 | 0 | 0 | 0 |

Simple again: C is incremented and D is decremented.

---
|| A | B | C | D | E | F | G |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
(vii)| 2 | 3 | 5 | 0 | 0 | 0 | 0 |
(viii)| 2 | 4 | 0 | 0 | 0 | 0 | 4 |

This one is complicated again: B is incremented, C is reset to 0, and G is increased by 4.

---
#### General algorithm

Every time we want to find the next special number, we need to start by finding the right-most (least significant) non-zero digit. Once we've found it, we do three things:

1. Increment the digit immediately to the left of it (the next most significant digit)
2. Set the value of the one's-digit to X - 1 (where X is the value of the digit)
3. Set the value of the digit to 0
