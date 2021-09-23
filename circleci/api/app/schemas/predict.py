from typing import Any, List, Optional

from pydantic import BaseModel
from deploy_chk.processing.validation import HouseDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[Any]


#class HouseDataInputSchema1(BaseModel):
#    Store: Optional[int]
#    DayOfWeek: Optional[int]
#    Date: Optional[str]
#    Open: Optional[float]
#    Promo: Optional[int]
#    StateHoliday: Optional[str]
#    SchoolHoliday: Optional[int]
#    StoreType: Optional[str]
#    Assortment: Optional[str]
#    CompetitionDistance: Optional[float]
#    CompetitionOpenSinceMonth: Optional[float]
#    CompetitionOpenSinceYear: Optional[float]
#    Promo2: Optional[int]
#    Promo2SinceWeek: Optional[float]
#    Promo2SinceYear: Optional[float]
#    PromoInterval: Optional[str]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Store": 1,
                        "DayOfWeek": 5,
                        "Date": "31-07-2015",
                        "Open": 1,
                        "Promo": 1,
                        "StateHoliday": "0",
                        "SchoolHoliday": 1,
                        "StoreType": "c",
                        "Assortment": "a",
                        "CompetitionDistance": 1270,
                        "CompetitionOpenSinceMonth": 9,
                        "CompetitionOpenSinceYear": 2008,
                        "Promo2": 0,
                        "Promo2SinceWeek": 13.0,
                        "Promo2SinceYear": 2010.0,
                        "PromoInterval": "Jan,Apr,Jul,Oct",

                    }
                ]
            }
        }
