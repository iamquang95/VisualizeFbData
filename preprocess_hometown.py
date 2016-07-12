# -*- coding: utf-8 -*-
import json
import codecs

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import re

ITAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐÐ"
INTAB = [ch.encode('utf8') for ch in unicode(ITAB, 'utf8')]


OUTTAB = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d" + \
         "A" * 17 + "O" * 17 + "E" * 11 + "U" * 11 + "I" * 5 + "Y" * 5 + "D" * 2

r = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))


def no_accent_vietnamese(utf8_str):   
    return r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)

total = 0
hometown = {}
cnt_hometown = {}
huyen = {}
province = {}

def add_province(name, cnt=1):
    if not province.has_key(name):
        province[name] = cnt
    else:
        province[name] += cnt
        
    global total
    total += cnt
    

def output(schools, file_name):
    # s = sorted(schools.items(), key=lambda x: -x[1][1])
    s = schools.iteritems()
    with codecs.open(file_name,'w','utf-8') as fo:
        for key, value in s:       
            fo.write(key+' '+value+'\n')
            # fo.write('%s\t%s\t%d\n' % (key, value[0], value[1]))
            
def read_huyen():
    with open('tinh.csv','r') as fi:
        for line in fi:
            cur = [no_accent_vietnamese(s).encode('utf-8') for s in line.strip().split(',')]
            huyen[ cur[1] ] = cur[2]
            # print cur
            
def process(id, name, cnt=1):
    name = name.encode('utf-8')
    # print name
    name = no_accent_vietnamese(name)
    for s in name.split(','):        
        ss = s.strip()
        # ss = no_accent_vietnamese(ss)        
        for h,t in huyen.iteritems():
            if ss == h or ss == t:
                add_province(t,cnt)
                return
        # print '---', ss
    
    print id, name

read_huyen()            
# """
with open('profiles.txt','r') as fi:    
    for line in fi:
        # print line
        cur = json.loads(line)
        if cur.has_key('hometown'):
            town = cur['hometown']
            id = town['id']
            name = town['name']
            if not hometown.has_key(id):
                hometown[id] = name
                cnt_hometown[id] = 1
            else:
                cnt_hometown[id] += 1            
                
for key,value in hometown.iteritems():
    process(key, value, cnt_hometown[key])
    
print total


# output(university, 'university.txt')
# output(high_school, 'new_high_school.csv')
# output(other, 'other.txt')
# output(hometown, 'hometown.txt')
# """
# print no_accent_vietnamese('A ă â b c d đ e ê g h i j k l m n o ô ơ ớ')
# process('Cai Mon, Bến Tre, Vietnam')
# process('Bồng Sơn, Bình Ðịnh, Vietnam')
# process('Cai Rong, Quảng Ninh, Vietnam')
# print no_accent_vietnamese('ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐĐÐĐ')
