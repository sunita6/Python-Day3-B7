#Assignment 3

#1.Pilot Plan(if else)

alt=int(input("enter the current altitude"))
print(alt)
if(alt<=1000):
  print("safe to land")
elif(alt>=1000 and alt<=5000):
    print("come down to 1000ft")
else:
      print("turn around")			

#output

enter the current altitude1000
1000
safe to land			


#2.prime numbers from 1-200


for num in range(2,201):
    if all(num%i!=0 for i in range(2,num)):
            print(num)
			
#output
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199



