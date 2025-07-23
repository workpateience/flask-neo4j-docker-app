# 🚀 Flask + Neo4j + Docker App

A fully containerized Flask backend application integrated with a Neo4j graph database using Docker.

---

## 📦 Features

- ✅ Flask backend for building APIs
- ✅ Neo4j for graph-based data storage
- ✅ Docker for easy setup and containerization
- ✅ Database import/export via Neo4j dump
- ✅ Cross-platform commands (macOS/Linux/Windows)

---

## 🛠️ Project Setup

```bash
docker compose up --build
```

##  stop contaiiner

```bash
  docker stop flask-neo4j-docker-app-neo4j-1
```

##  neo4j dump command for macOS

```bash
docker run --rm \
  -v $(pwd)/neo4j-dump:/var/lib/neo4j/import \
  -v neo4j_data:/data \
  neo4j:latest \
  neo4j-admin database load neo4j \
  --from-path=/var/lib/neo4j/import \
  --overwrite-destination=true
```

##  neo4j dump command for window

```bash
docker run --rm -v "%cd%\neo4j-dump:/var/lib/neo4j/import" -v neo4j_data:/data neo4j:latest neo4j-admin database load neo4j --from-path=/var/lib/neo4j/import --overwrite-destination=true
```

##  start contaiiner

```bash
 docker start flask-neo4j-docker-app-neo4j-1
```
