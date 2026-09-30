# The Project (under work)

## todo-app

FastAPI server that serves a simple HTML page at `/` and prints `Server started in port NNNN` on startup. Port is set with `PORT` (default `8000`) in `manifests/deployment.yaml`.

### Deploy

The image is pulled from Docker Hub automatically.

```bash
k3d cluster start
kubectl apply -f todo-app/manifests/
kubectl logs -f deployment/the-project
```

### Open in browser

Go to http://localhost:8081.

The Ingress uses path `/`, the same as Log output's, so only one of them can be applied at a time for now.