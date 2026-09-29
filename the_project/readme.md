# The Project (under work)
 
## todo-app
 
FastAPI server that prints `Server started in port NNNN` on startup. Port is set with `PORT` (default `8000`).
 
### Deploy
 
The image is pulled from Docker Hub automatically.
 
```bash
k3d cluster start
kubectl create deployment the-project --image=tvaanane02/the_project:1.2
kubectl logs -f deployment/the-project
```