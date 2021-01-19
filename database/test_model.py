from peewee import *

database = MySQLDatabase('interview-sort', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost', 'port': 3306, 'user': 'root', 'password': 'coltea123'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Grade(BaseModel):
    class_ = CharField(column_name='class', null=True)
    created_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    score = IntegerField(null=True)
    updated_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'grade'

