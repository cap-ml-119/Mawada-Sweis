# To do list
## Assignment 1 : 
Create a TODO list app exposing REST endpoints for the following functionalities
- Add TODO
- Update TODO
- Update the status of TODO (PENDING, DONE, CANCELED)

## Endpoint description
- Add new task : 
  - Post method
  - link : localhost:5001/<status>/<description>
  - <status> : The status of the task (PENDING, DONE, CANCELED).
  - <description> : The discreption of the task.
- Update exist discription task by its ID :
  - Put method
  - link : localhost:5001/update/description/<id>/<updateTask>
  - <id> : Is the ID of the exist task that it was created automatically in the Add endpoint( You can show the task with its ID by Display endpoint).
  - <updateTask> : Is the update discription.
- Update exist status for task by its ID :
  - Put method
  - link : localhost:5001/update/status/<id>/<updateTask>
  - <id> : Is the ID of the exist task that it was created automatically in the Add endpoint( You can show the task with its ID by Display endpoint).
  - <updateTask> : Is the update status.
- Delete exist task by its ID :
  - Delete method
  - link : localhost:5001/delete/<id>
  - <id> : Is the ID of the exist task that it was created automatically in the Add endpoint( You can show the task with its ID by Display endpoint).
- Display to-do list :
  - Get method
  - link : localhost:5001/display