from pydantic import BaseModel


# What the caller sends when designating a transporter to a task.
class TransporterCreate(BaseModel):
    name: str


# What the API sends back after reading from the database.
class TransporterOut(BaseModel):
    id: int
    name: str
    status: str
    model_config = {"from_attributes": True}
