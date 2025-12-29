def note_serializer(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "description": note["description"],
        "important": note.get("important", False)
    }

def notes_serializer(notes) -> list:
    return [note_serializer(note) for note in notes]
