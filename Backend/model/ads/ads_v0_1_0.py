import pickle
import asyncio
from pathlib import Path
__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/ads-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


classes = [
"still not purchased",
"purchased"
]


async def predict_pipeline(
    gender: str,
    age: int,
    estimatedSalary: float
) -> str:
    pred = model.predict([[gender, age, estimatedSalary]])
    return classes[pred[0]]