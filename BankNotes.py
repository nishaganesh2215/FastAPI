## Used to read the input variable from Swagger API, using pydantic 

from pydantic import BaseModel

class BankNote(BaseModel):
    variance : float
    skewness : float
    curtosis: float	
    entropy: float