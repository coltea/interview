from database.test_model import Grade
import random
name = ["小a", "小b", "小c", "小d", "小f", "小e", "小t", "小g", "小u", "小i"]
insert_data = []
for i in name:
    for i2 in ["math","eng","art","info"]:
        insert_data.append(dict(
            name=i,
            class_=i2,
            score=random.choice(range(60,85))
        ))
print(insert_data)
Grade.insert_many(insert_data).execute()