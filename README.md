# Slow App Monitoring

## 🚀 Run the project

```bash
docker compose up -d --build --scale slow-api=3

Prometheus: http://localhost:9090

Alertmanager: http://localhost:9093

📈 Watch Metrics
Go to Prometheus → Graph → run: myapp_pending_requests

📬 Alerts
Sent via SMTP to: monitoring@dionamite.com

🧹 Stop & clean

docker compose down       # stop
docker compose down -v    # stop & delete volumes
```
