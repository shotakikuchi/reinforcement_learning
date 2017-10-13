
# n bandit arms
reference url : [http://yamaimo.hatenablog.jp/entry/2015/08/21/200000]()

# Required Libraries
- numpy

# Run
```
python bandit.py
```
will be like this
```
python bandit.py 
input 0 - 10, or 'q'
1
-0.966544977912
1
-4.25224047997
1
-1.4013823122
2
-0.0823011210873
2
-1.24808183068
3
1.88714467284
4
0.813601293067
5
0.283486026058
6
1.64770136225
7
0.409356559357
8
0.643938015677
9
0.238753567242
q
expected values
[ 0.67010658 -1.20222063  0.12922596  1.06250271  0.49534293 -0.67429474
 -0.18700492 -0.10246359 -0.38649231 -0.629311  ]

```
In this case, 3th arm is the best reward.
