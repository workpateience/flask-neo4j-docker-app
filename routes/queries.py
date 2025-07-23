# routes/queries.py

from flask import Blueprint, jsonify
from models import Token, Project, File, Image, User
from neomodel import db

queries_bp = Blueprint('queries', __name__)

# List all tokens
@queries_bp.route('/tokens')
def list_tokens():
    tokens = Token.nodes.all()
    return jsonify([{'key': t.key} for t in tokens])


# List all projects
@queries_bp.route('/projects')
def list_projects():
    projects = Project.nodes.all()
    return jsonify([{'name': p.name} for p in projects])


# List all files in Project 1
@queries_bp.route('/files-in-project-1')
def list_files_in_project_1():
    project = Project.nodes.get_or_none(name="Project 1")
    if not project:
        return jsonify({"error": "Project 1 not found"}), 404

    files = File.nodes.filter(belongs_to__name="Project 1")
    return jsonify([{'name': f.name} for f in files])


# Cypher query: images with width=200 uploaded by user with specific google_id
@queries_bp.route('/images-by-google-id')
def images_by_google_id():
    query = """
    MATCH (u:User {google_id: '102718630068735143796'})<-[:UPLOADED_BY]-(img:Image)
    WHERE img.width = 200
    RETURN img.name AS name, img.width AS width
    """
    results, _ = db.cypher_query(query)
    return jsonify([{'name': row[0], 'width': row[1]} for row in results])
