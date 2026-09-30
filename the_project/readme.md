# The Project (under work)

## todo-app

FastAPI server that serves a simple HTML page at `/` and prints `Server started in port NNNN` on startup. Port is set with `PORT` (default `8000`) in `manifests/deployment.yaml`.

### Deploy

The image is pulled from Docker Hub automatically.

```bash
k3d cluster start
kubectl apply -f todo-app/manifests/deployment.yaml
kubectl logs -f deployment/the-project
```
### Open in browser

```bash
kubectl port-forward deployment/the-project 8000:8000
```
Then go to http://localhost:8000.