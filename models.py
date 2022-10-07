from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")



class ProducerResponse(BaseModel):

    left_shoe: int
    right_shoe: int
    tilt: int
    speed: int
    EventProcessedUtcTime: str
    EventEnqueuedUtcTime: str


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "left_shoe": 0,
                "right_shoe": 0,
                "tilt": 0,
                "speed": 0,
                "EventProcessedUtcTime": "2022-10-06T21:05:42.4203693Z",
                "EventEnqueuedUtcTime": "2022-10-06T21:04:57.1320000Z"
            }
        }