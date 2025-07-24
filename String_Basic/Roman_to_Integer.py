mapp = {"I":1,
"V" :5,
"X": 10,
"L"   : 50,
"C"   : 100,
"D"   : 500,
"M"   :1000}

s = "MCMXCIV"
res  = 0

for i in range(len(s)):
    if i+1<len(s) and mapp[s[i]]<mapp[s[i+1]]:
        res-=mapp[s[i]]
    else:
        res+=mapp[s[i]]

print(res)