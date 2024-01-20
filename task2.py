# task2.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
import pandas as pd
import numpy as np

app = FastAPI()

def calculate_volatility(data: pd.DataFrame) -> dict:
    data.columns = data.columns.str.strip()
    data['Daily Returns'] = data['Close'].pct_change()
    daily_volatility = np.std(data['Daily Returns'])
    annualized_volatility = daily_volatility * np.sqrt(len(data))
    return {"Daily Volatility": daily_volatility, "Annualized Volatility": annualized_volatility}

@app.post("/calculate_volatility")
async def calculate_volatility_endpoint(
    file: Optional[UploadFile] = File(None)
):
    if file is None:
        raise HTTPException(
            status_code=400, detail="No file provided"
        )
    contents = await file.read()
    data = pd.read_csv(pd.compat.StringIO(contents.decode("utf-8")))
    result = calculate_volatility(data)
    return JSONResponse(content=result)
