import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
collection = db.students

students = collection.find()

index_remove = -1

for student in students :

	scores = student['scores']

	print scores
	index = 0
	for score in scores :

		if score['type'] == 'homework' :

			if index_remove == -1 or score['score'] < scores[index_remove]['score'] :
				index_remove = index

		index = index + 1

	scores.remove(scores[index_remove])

	collection.update_one({"_id" : student['_id']}, {"$set" : {"scores" : scores}})

	print scores