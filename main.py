from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from routers import post

app = FastAPI()

# Initialize the FastAPI app with some metadata and disable the default docs
app = FastAPI(
    title="Sonarcloud , GitHub Actions, FastAPI, Heroku",
    description="Sonarcloud , GitHub Actions, FastAPI, Heroku",
    version="2.0.0",
    docs_url=None,  # Disable default Swagger UI
    redoc_url="/redoc",  # Disable default ReDoc
)

# Mount static files
app.mount("/static", StaticFiles(directory="./static"), name="static")


# Custom Swagger UI available at the root URL
@app.get("/swagger", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


# Add CORS middleware with default configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(post.router)
