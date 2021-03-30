# score1 = {'张三':98, '李四':99, '麦叔':100}
# score2 = {'王五':87, '麦叔':88}
#
# #新特性：合并字典运算符
# score3 = score1 | score2
# print(score3)
#
# score1.update(score2)
# print(score1)


#
# d = '日期：2020-10-15，星期四'
# #新特性：去掉前缀
# d.removeprefix('日期：')
# #新特性：去掉后缀
# d.removesuffix('，星期四')
# # d.lstrip()
# print(d.rstrip('星期四'))


scores = list[int]()
#添加字符串进去是不允许的，在写代码的时候IDE就会告诉我们
scores.append('88')