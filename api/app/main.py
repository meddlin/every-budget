from fastapi import FastAPI

from app.routers import budgets, categories, envelopes, transactions

app = FastAPI()

app.include_router(budgets.router)
# app.include_router(categories.router)
# app.include_router(envelopes.router)
# app.include_router(transactions.router)