from pydantic import BaseModel


class ErrorDetail(BaseModel):
    code: str
    detail: str


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    errors: list[ErrorDetail]