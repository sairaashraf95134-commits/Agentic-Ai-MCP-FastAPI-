from pydantic import BaseModel


class EmailInput(BaseModel):

    to: str

    subject: str

    body: str


class SearchInput(BaseModel):

    query: str


class AddInput(BaseModel):

    a: int

    b: int


class SubtractInput(BaseModel):

    a: int

    b: int


class MultiplyInput(BaseModel):

    a: int

    b: int


class DivideInput(BaseModel):

    a: int

    b: int