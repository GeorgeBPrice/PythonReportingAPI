from fastapi import FastAPI
from fastapi.responses import RedirectResponse
# from app.routers import asset_routes, expense_routes
from app.routers.asset_routes import router as asset_router

app = FastAPI()

# Include routers
app.include_router(asset_router, prefix="/assets", tags=["Asset Reports"])
# app.include_router(expense_routes.router, prefix="/expenses", tags=["Expenses"])

# Root route redirects to docs
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")