**Simple flask app REST API to practise**
- curl http://localhost:5000/tasks
- curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Read a book\"}" http://localhost:5000/tasks
- curl -X PUT -H "Content-Type: application/json" -d "{\"description\":\"Read the entire book\", \"done\":true}" http://localhost:5000/tasks/1
- curl -X DELETE http://localhost:5000/tasks/1

