from neomodel import (
    StructuredNode, StringProperty, IntegerProperty,
    RelationshipTo, RelationshipFrom, config
)
import os

# Neo4j connection using environment variables
config.DATABASE_URL = os.getenv("NEO4J_BOLT_URL", "bolt://neo4j:testpassword@neo4j:7687")

# ---------------------- Nodes ------------------------

class User(StructuredNode):
    name = StringProperty()
    google_id = StringProperty(unique_index=True, required=True)

    # Relationships
    uploaded_images = RelationshipFrom('Image', 'UPLOADED_BY')


class Project(StructuredNode):
    name = StringProperty(unique_index=True)

    # Relationships
    has_files = RelationshipFrom('File', 'BELONGS_TO')
    has_tokens = RelationshipTo('Token', 'HAS_TOKEN')


class File(StructuredNode):
    name = StringProperty()
    belongs_to = RelationshipTo('Project', 'BELONGS_TO')


class Image(StructuredNode):
    name = StringProperty()
    width = IntegerProperty()
    uploaded_by = RelationshipTo('User', 'UPLOADED_BY')


class Token(StructuredNode):
    key = StringProperty()
    related_project = RelationshipFrom('Project', 'HAS_TOKEN')
