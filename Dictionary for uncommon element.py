# Programs to create a new dictionary of uncommon elements:

di1 = {1:10,2:20,3:45,4:36}
di2 = {5:42,6:33,7:14,3:39}
di3 ={}

for i in di1:
        if i not in di2:
                di3[i] = di1[i]

for i in di2:
        if i not in di1:
                di3[i] = di2[i]
        else:
                di3[i] = di1[i]+di2[i]
print(di3)
