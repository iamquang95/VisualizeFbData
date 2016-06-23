# -*- coding: utf-8 -*-
import json
import codecs

university = {}
high_school = {}
other = {}

def output(schools, file_name):
    s = sorted(schools.items(), key=lambda x: -x[1][1])
    with codecs.open(file_name,'w','utf-8') as fo:
        for key, value in s:       
            #print value
            fo.write('%s\t%s\t%d\n' % (key, value[0], value[1]))

with open('vnu_profiles.txt','r') as fi:
    print high_school
    for line in fi:
        # print line
        cur = json.loads(line)
        if cur.has_key('education'):
            education = cur['education']                       
            for edu in education:
                school = edu['school']
                id = school['id']
                name = school['name']                
                if edu['type'] == 'College':
                    university[school['id']] = school['name']
                elif edu['type'] == 'High School':                    
                    cur = high_school.get(id)
                    if cur is None:                        
                        high_school[id] = (name, 1)
                        # print high_school
                    else:                        
                        (ss, tmp) = cur                        
                        high_school[id] = (name, tmp+1)
                    # high_school[school['id']] = school['name']
                else:
                    other[school['id']] = school['name']


# output(university, 'university.txt')
output(high_school, 'new_high_school.csv')
# output(other, 'other.txt')


"""
fo1 = codecs.open('vnu.txt','w','utf-8')
fo2 = codecs.open('non-vnu.txt','w','utf-8')
for key, value in university.iteritems():    
    s = value.lower()
    s = s.encode('utf-8')
    ss = ['dhqghn', 'vnu', 'dai hoc quoc gia ha noi', 'dh quoc gia ha noi', 'dai hoc qghn',
         'đhqghn', 'vietnam national university', 'đại học quốc gia hà nội', 'đh quốc gia hà nội', 'đại học qghn'] 
         
    check = False    
    for tmp in ss:
        print s
        print tmp
        if s.find(tmp) != -1:
            check = True
    if check:
        fo1.write('%s %s\n' % (key, value))
    else:
        fo2.write('%s %s\n' % (key, value))

fo1.close()
fo2.close()
""" 
                
                