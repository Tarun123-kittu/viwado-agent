from fastapi import APIRouter
from app.models.response import ApiResponse
from app.core.context import get_request_id

router = APIRouter()


@router.get("/health")
async def health():
    """Health endpoint."""

    return ApiResponse(
        message="Health check successful",
        data={
            "status": "healthy",
            "request_id": get_request_id(),
        },
    )