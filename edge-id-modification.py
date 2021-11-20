
# By Koushik Sarkar

from xml.dom import minidom
k=1
j=1
d={}
cnt=0
# parse an xml file by name
mydoc = minidom.parse('saltlake_intermediate.net.xml')

items = mydoc.getElementsByTagName('edge')

# all item attributes
print('\nEdge IDs are being Modified.\nPlease keep patience! Koushik will take care.')
for elem in items:
    if elem.hasAttribute("function"):
        #c=1
        x='ie_'+str(k)
        k=k+1
    else:
        x=str(elem.attributes['from'].value)+"_"+str(elem.attributes['to'].value)
        cnt+=1
    d[elem.attributes['id'].value]=x
    
myfile=open("dictionary_edge_id.csv","w")
for i in d.keys():
    myfile.write(str(i)+","+d[i]+"\n")


with open("saltlake_intermediate.net.xml",) as odoc, open("saltlake_final.net.xml","w") as ndoc:
    for line in odoc:
        nstr=""
        flg1=0
        line1=line.split('"')
        for nid,t in enumerate(line1):
            for i in d.keys():
                if str(i) == t:
                    line1[nid]=str(d[i])
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
print("\nCongrats! Edge IDs are Modified.")
print("\n----------------------------------")
print("Thanks and Regards,")
print("Koushik Sarkar")
input("\nPress press any key to exit.")

