# -*- coding: utf-8 -*-
import json
import codecs

import util

total = 0
hometown = {}
cnt_hometown = {}
location = {}
cnt_location = {}
id_map = {}
huyen = {}
home = {}
loc = {}

def add_province(container, name, cnt=1):
    if not container.has_key(name):
        container[name] = cnt
    else:
        container[name] += cnt
        
    global total
    total += cnt
    

def output(schools, file_name):
    # s = sorted(schools.items(), key=lambda x: -x[1][1])
    s = schools.iteritems()
    with codecs.open(file_name,'w','utf-8') as fo:
        for key, value in s:       
            fo.write(key+','+str(value)+','+id_map[key]+'\n')
            # fo.write('%s\t%s\t%d\n' % (key, value[0], value[1]))
            
def read_huyen():
    with open('tinh.csv','r') as fi:
        for line in fi:
            cur = line.strip().split(',')
            tinh = cur[2]
            id_map[tinh] = cur[3]
            cur = [ util.no_accent_vietnamese(s).encode('utf-8') for s in cur ]
            huyen[ cur[1] ] = tinh
            huyen[ cur[2] ] = tinh            
            # print cur
            
def process(container, id, name, cnt=1):
    name = name.encode('utf-8')
    # print name
    name = util.no_accent_vietnamese(name)
    for s in name.split(','):        
        ss = s.strip()
        # ss = no_accent_vietnamese(ss)        
        for h,t in huyen.iteritems():
            if ss == h or ss == t:
                add_province(container, t,cnt)
                return
        # print '---', ss
    
    print id, name
    
def process_province(container, container_cnt, item, keyword):
    if item.has_key(keyword):
        town = cur[keyword]
        id = town['id']
        name = town['name']
        if not container.has_key(id):
            container[id] = name
            container_cnt[id] = 1
        else:
            container_cnt[id] += 1            

read_huyen()            
# """
with open('vnu_profiles.txt','r') as fi:    
    for line in fi:
        # print line
        cur = json.loads(line)
        process_province(hometown, cnt_hometown, cur, 'hometown')
        process_province(location, cnt_location, cur, 'location')
                
for key,value in hometown.iteritems():
    process(home, key, value, cnt_hometown[key])
for key,value in location.iteritems():
    process(loc, key, value, cnt_location[key])
    
# for key,value
    
print total
output(home, 'hometown.txt')
output(loc, 'location.txt')


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
