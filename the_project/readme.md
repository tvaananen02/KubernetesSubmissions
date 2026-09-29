# The Project (under work)

## todo-app

FastAPI server that prints `Server started in port NNNN` on startup. Port is set with `PORT` (default `8000`) in `manifests/deployment.yaml`.

### Deploy

The image is pulled from Docker Hub automatically.

```bash
k3d cluster start
kubectl apply -f todo-app/manifests/deployment.yaml
kubectl logs -f deployment/the-project
```