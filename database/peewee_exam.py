import peewee
# peewee
#
# Tb.select().count()  # 统计总数
# Tb.select(Tb.Col).distinct().count() # 统计某列非重复记录总数
# Tb.select().dicts()  # 查询结果转字典
# Tb.select().get() #获取最后一行
# Tb.select().where(Tb.deleted.is_null(False)) # 非NULL
# Tb.select().order_by(Tb.id.desc()).get() # 获取最大id
# Tb.select().join(Tb2, on=(Tb.id == Tb2.id)）.where(Tb.postplatformid == union_id) # join
# Tb.select().where((Tb.Col1.is_null(True)) | (Tb.Col2 == '')) # or 逻辑

# # fn 函数
# Tb.select(fn.MAX(TbFashionBiInfo.id)).scalar() # Max id
# Tb.select(fn.SUM(Tb.Col).alias("Sum_Col")) # SUM 统计某一列总和
# Tb.select(Tb.Col,fn.COUNT(Tb.Col).alias('count_Col')).where(Tb.Col.in_([1,2,5])).group_by(Tb.Col)  # count + group_by + where in