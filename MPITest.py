import sys
fp=open(sys.argv[1],"r")
lis=fp.readlines()
fp.close()
dic={}
lis=map(lambda a:a.replace("\n",""),lis)

for item in lis:
  if not item in dic.keys():
    dic[item]=1
  else:
    dic[item]+=1
fp=open(sys.argv[2],"w")
for key in sorted(dic.keys()):
  fp.write(key+" "+str(dic[key])+"\n")
fp.close()
