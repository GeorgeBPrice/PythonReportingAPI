from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routers.asset_routes import router as asset_router

# Create FastAPI app
app = FastAPI()

# Include routers
app.include_router(asset_router, prefix="/assets", tags=["Asset Reports"])

# Root route redirects to docs
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")