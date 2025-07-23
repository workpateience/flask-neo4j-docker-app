# routes/queries.py

from flask import Blueprint, jsonify
from models import Token, Project, File, Image, User
from neomodel import db

# Define a Blueprint for query-related routes
queries_bp = Blueprint('queries', __name__)

# ---------------------- TOKEN ROUTES ----------------------

# Endpoint to list all tokens
@queries_bp.route('/tokens')
def list_tokens():
    try:
        tokens = Token.nodes.all()
        return jsonify([{'key': t.key} for t in tokens])
    except Exception as e:
        print(f"An error occurred: {e}")

# ---------------------- PROJECT ROUTES ----------------------

# Endpoint to list all projects
@queries_bp.route('/projects')
def list_projects():
    try:
        projects = Project.nodes.all()
        return jsonify([{'name': p.name} for p in projects])
    except Exception as e:
        print(f"An error occurred: {e}")


# ---------------------- FILE ROUTES ----------------------

# Endpoint to list all files related to project named "Project 1"
@queries_bp.route('/files-in-project-1')
def list_files_in_project_1():
    # Fetch project by name
    try:
        project = Project.nodes.get_or_none(name="Project 1")
        if not project:
            return jsonify({"error": "Project 1 not found"}), 404

        # Traverse the 'has_files' relationship to get associated files
        files = project.has_files.all()
        return jsonify([{'name': f.name} for f in files])
    except Exception as e:
        print(f"An error occurred: {e}")

# ---------------------- IMAGE ROUTES ----------------------

# Endpoint to return images uploaded by a specific Google ID with width = 200
@queries_bp.route('/images-by-google-id')
def images_by_google_id():
    try:
        query = """
        MATCH (u:User {google_id: '102718630068735143796'})<-[:UPLOADED_BY]-(img:Image)
        WHERE img.width = 200
        RETURN img.name AS name, img.width AS width
        """
        # Run raw Cypher query
        results, _ = db.cypher_query(query)
        
        # Format and return query results
        return jsonify([{'name': row[0], 'width': row[1]} for row in results])
    except Exception as e:
        print(f"An error occurred: {e}")
