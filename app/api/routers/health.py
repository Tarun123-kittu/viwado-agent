from fastapi import APIRouter
from app.models.response import ApiResponse

router = APIRouter()


@router.get("/health")
async def health():
    """Health endpoint."""

    return ApiResponse(
        message="Health check successful",
        data={
            "status": "healthy",
        },
    )