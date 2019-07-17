'''

Args:
Returns:
'''
import jieba_fast as jieba
# jieba.setLogLevel(20)

# jieba.load_userdict(r'D:/repo/wugaofeng/python/userdict.txt')

seg_list = jieba.cut("我来到北京清华大学")
# D:\repo\wugaofeng\python\userdict.txt
print(list(seg_list))