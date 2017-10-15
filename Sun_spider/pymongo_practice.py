#coding:utf-8

from pymongo import MongoClient


# 链接数据库
handle = MongoClient('127.0.0.1',27017)

# 选择一个数据库
db = handle['chuanzhi']

# 选择集合
col = db['test']

# 查询----find()结果是个游标，如果想要看到数据，必须遍历


# print (col.find_one({"c++":"python19"}))

# for i in range(13):
#     key = str(i)
#     col.insert({key:i*i+1})
# col.remove({"12":145})

col.update({"10":101},{"$set":{"10":102}})

cursor = col.find()
for data in cursor:
    print (data)