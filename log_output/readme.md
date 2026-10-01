# Log output

One pod with two containers that share a file through an `emptyDir` volume:

- **writer** creates a random string on startup and appends it with a timestamp to `log.txt` every 5 seconds.
- **reader** is a FastAPI app that returns the latest line of `log.txt` at `/`. Port is set with `PORT` (default `8000`) in `manifests/deployment.yaml`.

The Ingress is shared with the ping-pong app and routes `/pingpong` to it.

### Deploy

The images are pulled from Docker Hub automatically.

```bash
k3d cluster start
kubectl apply -f manifests/
kubectl logs -f deployment/log-output -c reader
```

### Open in browser

Go to http://localhost:8081.