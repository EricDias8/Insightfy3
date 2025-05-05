from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.request import TextRequest
from app.models.database import SessionLocal
from app.models.request import Request
from app.services.insight import generate_summary_and_save

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/analyze")
def analyze_text(payload: TextRequest, db: Session = Depends(get_db)):
    result = generate_summary_and_save(payload.text)
    new = Request(
        input_text=payload.text,
        summary=result["summary"],
        category=result["category"],
        label=result["label"]
    )
    db.add(new)
    db.commit()
    return result

@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(Request).all()
