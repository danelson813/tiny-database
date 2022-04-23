from tinydb import TinyDB, Query

db = TinyDB('todo_db.json')

new_item = {"name": "Book", "quantity": 5}
# db.insert(new_item)
items = [
    {"name": "Cake", "quantity": 1},
    {"name": "Candles", "quantity": 10},
    {"name": "Balloons", "quantity": 50}
]
# db.insert_multiple(items)
# print(db.all())
# for item in db:
#     print(item)

Todo = Query()
# print(db.search(Todo.name == 'Book'))
# print(db.search(Todo.name == 'Copies'))
# print(db.all())
# print(db.get(Todo.name == 'Book'))
# print(db.get(Todo.name == 'Copies'))
# print(db.contains(Todo.name == 'Copies'))
# print(db.contains(Todo.name == 'Book'))
# db.insert({"name": "Balloons", "quantity": 500})
# for item in db:
#     print(item)
# print(db.count(Todo.name == 'Balloons'))
# print(len(db))
# db.update({'name': 'Books'}, Todo.name == 'Book')
# for item in db:
#     print(item)
# db.update({'quantity': 10})
# print('*'*50)
# for item in db:
#     print(item)
# db.remove(Todo.name == 'Cake')
# db.remove(Todo.name == 'Copies')
# db.remove(doc_ids=[4,5])
# for item in db:
#     print(item)

db.truncate()
print(db.all())