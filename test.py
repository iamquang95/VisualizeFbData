import sys
reload(sys)
sys.setdefaultencoding('utf-8')

s = "THPT Chuy\xc3\xaan H\xc6\xb0ng Y\xc3\xaan"
s = unicode(s, 'utf-8')

print s
print type(s)
