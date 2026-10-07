from fastapi import APIRouter, HTTPException


router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def get_products():
    return {"message": "List of products"}      