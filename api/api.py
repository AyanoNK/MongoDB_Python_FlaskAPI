from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient

#framework init
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'colegio'

#change colegio to your database name
app.config['MONGO_URI'] = 'mongodb://localhost:27017/schoolstudents'


mongo = PyMongo(app)

#Method to get elements from the collection
@app.route('/framework', methods=['GET'])
def get_all_students():

    students = mongo.db.students

    output = []

    for query in students.find():

        output.append({'_id': query['_id'], 'name': query['name'], 'age': query['age']})

    return jsonify({'result': output})



#Method to add students.
@app.route('/framework', methods=['POST'])
def add_student():
    
    students = mongo.db.students

    _id = request.json['_id']
    name = request.json['name']
    age = request.json['age']

    #add student to collection
    newstudent = students.insert({'_id': _id, 'name': name, 'age': age})
    getnewstudent = students.find_one({'_id': newstudent})

    #returns a query on success
    output = {'_id': getnewstudent['_id'], 'name': getnewstudent['name'], 'age': getnewstudent['age']}
    return jsonify({'result': output})


#Method to delete estudiant.
@app.route('/framework/<_id>',methods=['DELETE'])
def delete_student(_id):
    students = mongo.db.students
    
    students.delete_one({'_id': _id})
    
    output = {'message': _id + ' Has been deleted'}
    return jsonify(output)


#Method to modify student
@app.route('/framework',methods=['PUT'])
def update_student():
    
    students = mongo.db.students

    old_id = request.json['oldid']
    _id = request.json['newid']
    name = request.json['name']
    age = request.json['age']

    students.update_many({'_id': old_id}, {'$set': {
        '_id': _id,
        'name': name,
        'age': age
    }})

    output = {'message': 'Updated'}
    
    return jsonify(output)

#exec app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)