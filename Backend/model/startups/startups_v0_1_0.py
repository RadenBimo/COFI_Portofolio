import pickle
import asyncio
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/startups-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

async def predict_pipeline(
    rd: float,
    administration: float,
    marketing: float,
    state: str
) -> float:
    pred = model.predict([[rd, administration, marketing, state]])
    return pred