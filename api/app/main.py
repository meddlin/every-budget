from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import budgets, categories, envelopes, transactions

app = FastAPI()

app.include_router(budgets.router)
# app.include_router(categories.router)
# app.include_router(envelopes.router)
# app.include_router(transactions.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)