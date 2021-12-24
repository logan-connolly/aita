import uuid


def generate_run_id() -> str:
    """Generate uuid unique identifier for fetching run id information"""
    return str(uuid.uuid4())
