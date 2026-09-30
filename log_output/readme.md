# Log output

FastAPI app that creates a random string on startup, logs it with a timestamp every 5 seconds, and returns the current status at `/`. Port is set with `PORT` (default `8000`) in `manifests/deployment.yaml`.

The Ingress is shared with the ping-pong app and routes `/pingpong` to it.

### Deploy

The image is pulled from Docker Hub automatically.

```bash
k3d cluster start
kubectl apply -f manifests/
kubectl logs -f deployment/log-output
```

### Open in browser

Go to http://localhost:8081.