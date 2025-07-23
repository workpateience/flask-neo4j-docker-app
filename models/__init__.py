from neomodel import (
    StructuredNode, StringProperty, IntegerProperty,
    RelationshipTo, RelationshipFrom, config
)
import os

# ---------------------- DATABASE CONFIGURATION ------------------------

# Set up the Neo4j database connection using environment variable or default
config.DATABASE_URL = os.getenv(
    "NEO4J_BOLT_URL", "bolt://neo4j:strongpassword123@neo4j:7687"
)

# ---------------------- NODE DEFINITIONS ------------------------

# Represents a user who can upload images
class User(StructuredNode):
    name = StringProperty()
    google_id = StringProperty(unique_index=True, required=True)

    # Relationship: Images uploaded by this user
    uploaded_images = RelationshipFrom('Image', 'UPLOADED_BY')


# Represents a project which can have multiple files and tokens
class Project(StructuredNode):
    name = StringProperty(unique_index=True)

    # Relationships
    has_files = RelationshipFrom('File', 'BELONGS_TO')      # Files belonging to this project
    has_tokens = RelationshipTo('Token', 'HAS_TOKEN')       # Tokens associated with this project


# Represents a file that belongs to a project
class File(StructuredNode):
    name = StringProperty()

    # Relationship: Points to the project this file belongs to
    belongs_to = RelationshipTo('Project', 'BELONGS_TO')


# Represents an image uploaded by a user
class Image(StructuredNode):
    name = StringProperty()
    width = IntegerProperty()

    # Relationship: Points to the user who uploaded this image
    uploaded_by = RelationshipTo('User', 'UPLOADED_BY')


# Represents a token associated with a project
class Token(StructuredNode):
    key = StringProperty()

    # Relationship: Points back to the project that owns this token
    related_project = RelationshipFrom('Project', 'HAS_TOKEN')
