# -*- coding: utf-8 -*-
import json
import codecs
import util

total = 0
positions = {}    
employers = {}

def output(schools, file_name):
    # s = sorted(schools.items(), key=lambda x: -x[1][1])
    s = schools.iteritems()
    total = 0
    with codecs.open(file_name,'w','utf-8') as fo:
        for key, value in s:       
            # fo.write(key+' '+value+'\n')
            fo.write('%s\t%s\t%d\n' % (key, value[0], value[1]))
            total += value[1]
        fo.write('%d\n' % total)

            
def process(id, name, cnt=1):
    name = name.encode('utf-8')
    # print name
    name = util.no_accent_vietnamese(name)
    for s in name.split(','):        
        ss = s.strip()
        # ss = no_accent_vietnamese(ss)        
        for h,t in huyen.iteritems():
            if ss == h or ss == t:
                add_province(t,cnt)
                return
        # print '---', ss
    
    print id, name
    
def process(container, item):
    if item.has_key('name'):
        id = item['id']
        name = item['name']
        if container.has_key(id):
            container[id][1] += 1
        else:
            container[id] = [name, 1]
# """
with open('vnu_profiles.txt','r') as fi:    
    for line in fi:
        # print line
        cur = json.loads(line)
        if cur.has_key('work'):
            works = cur['work']
            for work in works:
                if work.has_key('position'):
                    position = work['position']
                    process(positions, position)
                if work.has_key('employer'):
                    employer = work['employer']
                    process(employers, employer)
                    
output(positions, 'position.txt')
output(employers, 'employer.txt')
                    
    

