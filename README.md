# flask-neo4j-docker-app
# Flask backend with Neo4j and Docker



# docker stop flask-neo4j-docker-app-neo4j-1



docker run --rm \
  -v $(pwd)/neo4j-dump:/var/lib/neo4j/import \
  -v neo4j_data:/data \
  neo4j:latest \
  neo4j-admin database load neo4j \
  --from-path=/var/lib/neo4j/import \
  --overwrite-destination=true



# docker start flask-neo4j-docker-app-neo4j-1



docker run --rm -v "%cd%\neo4j-dump:/var/lib/neo4j/import" -v neo4j_data:/data neo4j:latest neo4j-admin database load neo4j --from-path=/var/lib/neo4j/import --overwrite-destination=true
