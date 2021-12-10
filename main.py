'''This is the app entry point.
 This means that the application can be invoked by this file '''

from flask import Flask
import uuid

# create an object of the flask class
app = Flask(__name__)

# list for to-do status
to_do = []


# make route for add new task to the to-do list
@app.route('/<status>/<description>', methods=['POST'])
def add_task(status, description):
    # add the object to the to-do list status
    to_do.append({"id": uuid.uuid4().int,
                  "task": description,
                  "status": status})
    return "Added the task to completed label successfuly!"


# update spacific task in the to-do list by its id
@app.route('/update/description/<int:id>/<updateTask>', methods=['PUT'])
def update_description(id, updateTask):
    for item in to_do:
        if item["id"] == id:
            item["task"] = updateTask
            return "Updated description successfly"
    return "Not found"


# update spacific task in the to-do list by its id
@app.route('/update/status/<int:id>/<updateStatus>', methods=['PUT'])
def update_status(id, updateStatus):
    for item in to_do:
        if item["id"] == id:
            item["status"] = updateStatus
            return "Updated status successfly"
    return "Not found"


# delete spacific task in the to-do list by its id
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_task(id):
    for item in to_do:
        if item["id"] == id:
            to_do.remove(item)
            return "deleted successfly"
    return "Not found"


# check if the post method is successfuly operating
@app.route('/display', methods=['Get'])
def display_toDo(status):
    return str(to_do)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
