# Ping-pong

FastAPI app that responds `pong N` at `/pingpong`, where `N` counts the requests. Port is set with `PORT` (default `8000`) in `manifests/deployment.yaml`.

It is reached through Log output's Ingress, so apply both.

### Deploy

The image is pulled from Docker Hub automatically.

```bash
k3d cluster start
kubectl apply -f manifests/
kubectl apply -f ../log_output/manifests/
```
### Open in browser
Go to http://localhost:8081/pingpong. On refresh the pong goes up