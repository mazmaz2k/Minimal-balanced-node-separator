input = """
1 2 2 1 3 4
1 3 2 1 2 4
1 4 0 0
1 5 2 1 6 7
1 6 2 1 5 7
1 7 0 0
1 8 2 1 9 10
1 9 2 1 8 10
1 10 0 0
1 11 2 1 12 13
1 12 2 1 11 13
1 13 0 0
1 14 2 1 15 16
1 15 2 1 14 16
1 16 0 0
1 17 2 1 18 19
1 18 2 1 17 19
1 19 0 0
1 20 2 1 21 22
1 21 2 1 20 22
1 22 0 0
1 23 2 1 24 25
1 24 2 1 23 25
1 25 0 0
1 26 2 1 27 28
1 27 2 1 26 28
1 28 0 0
1 29 2 1 30 31
1 30 2 1 29 31
1 31 0 0
1 32 2 1 33 34
1 33 2 1 32 34
1 34 0 0
1 35 2 1 36 37
1 36 2 1 35 37
1 37 0 0
1 38 1 0 11
1 39 1 0 14
1 40 2 0 38 2
1 39 2 0 38 8
1 41 2 0 38 5
1 40 2 0 39 29
1 41 2 0 39 32
1 38 2 0 39 26
1 38 2 0 40 11
1 39 2 0 40 14
1 38 2 0 41 17
1 42 2 0 41 23
1 39 2 0 41 20
1 41 2 0 42 35
1 1 2 0 2 5
1 1 2 0 2 8
1 1 2 0 2 29
1 1 2 0 5 8
1 1 2 0 5 32
1 1 2 0 5 35
1 1 2 0 8 14
1 1 2 0 8 20
1 1 2 0 11 14
1 1 2 0 11 26
1 1 2 0 11 17
1 1 2 0 14 20
1 1 2 0 17 26
1 1 2 0 20 17
1 1 2 0 26 29
1 1 2 0 26 32
1 1 2 0 29 32
1 1 2 0 32 35
1 1 1 1 38
1 1 1 1 40
1 1 1 1 41
1 1 1 1 39
1 1 1 1 42
0
38 reached(0)
39 reached(3)
40 reached(1)
41 reached(2)
42 reached(4)
3 out_hm(0,1)
6 out_hm(0,2)
9 out_hm(0,3)
12 out_hm(1,0)
15 out_hm(1,3)
18 out_hm(2,0)
21 out_hm(2,3)
24 out_hm(2,4)
27 out_hm(3,0)
30 out_hm(3,1)
33 out_hm(3,2)
36 out_hm(4,2)
2 in_hm(0,1)
5 in_hm(0,2)
8 in_hm(0,3)
11 in_hm(1,0)
14 in_hm(1,3)
17 in_hm(2,0)
20 in_hm(2,3)
23 in_hm(2,4)
26 in_hm(3,0)
29 in_hm(3,1)
32 in_hm(3,2)
35 in_hm(4,2)
0
B+
0
B-
1
0
1
"""
output = """
{out_hm(0,1), in_hm(0,2), out_hm(0,3), in_hm(1,0), out_hm(1,3), out_hm(2,0), in_hm(2,3), in_hm(2,4), out_hm(3,0), in_hm(3,1), out_hm(3,2), out_hm(4,2), reached(0), reached(3), reached(1), reached(2), reached(4)}
{in_hm(0,1), out_hm(0,2), out_hm(0,3), out_hm(1,0), in_hm(1,3), in_hm(2,0), out_hm(2,3), in_hm(2,4), out_hm(3,0), out_hm(3,1), in_hm(3,2), out_hm(4,2), reached(0), reached(3), reached(1), reached(2), reached(4)}
"""
