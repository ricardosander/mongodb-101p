
import pymongo

def process() :

	connection = pymongo.MongoClient("mongodb://localhost")

	db = connection.students;
	scores = db.grades;

	query = {"type" : "homework"}

	results = scores.find(query).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING )]);

	totalrRemoved = 0
	lastUserId = -1

	for student in results :

		if (lastUserId != student['student_id']) :
			lastUserId = student["student_id"]
			scores.delete_one({"_id" : student['_id']})
			totalrRemoved = totalrRemoved + 1


	print totalrRemoved;

process()