
# By Koushik Sarkar

from xml.dom import minidom
#import xml.etree.ElementTree as ET
i=1
j=1
d={}
a='a'
cnt=0
# parse an xml file by name
mydoc = minidom.parse('saltlake.net.xml')

items = mydoc.getElementsByTagName('junction')

# all item attributes
print('\nJuction IDs are being Modified.\nPlease keep patience! Koushik will take care.')
for elem in items:
    if elem.attributes['type'].value=="internal":
        x='b_'+str(j)
        j=j+1
    else:
        x=a+'_'+str(i)
        i=i+1
    d[elem.attributes['id'].value]=x
    
with open("dictionary_junction_id.csv","w") as myfile:
    for i in d.keys():
        myfile.write(str(i)+","+d[i]+"\n")
 
with open("saltlake.net.xml",) as odoc, open("saltlake_intermediate.net.xml","w") as ndoc:
    for line in odoc:
        nstr=""
        flg1=0
        line1=line.split('"')
        for nid,t in enumerate(line1):
            for i in d.keys():
                if str(i) == t:
                    line1[nid]=str(d[i])
                    cnt=cnt+1
                    flg1=1
        if flg1==1:
            nstr=line1[0]
            for t in range(1,len(line1)):
                nstr=nstr+"\""+line1[t]
            #print(nstr)
        if flg1==0:
            ndoc.write(line)
        else:
            ndoc.write(nstr)
print("\nCongrats! Junction IDs are Modified.")

