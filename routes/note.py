from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database.db import notes_collection
from schemas.note import notes_serializer

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    notes = notes_serializer(notes_collection.find())
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": notes}
    )

@router.post("/add")
async def add_note(request: Request):
    form = await request.form()

    note = {
        "title": form.get("title"),
        "description": form.get("description"),
        "important": True if form.get("important") == "on" else False
    }

    notes_collection.insert_one(note)

    return RedirectResponse("/", status_code=303)
