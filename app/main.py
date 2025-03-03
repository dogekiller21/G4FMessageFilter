from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from starlette.requests import Request

from app.logs import get_logger
from app.predictions.client import get_client
from app.predictions.config import SYSTEM_PROMPT
from app.predictions.models import G4FModel
from app.predictions.prompts import execute_prompt

logger = get_logger()
app = FastAPI()

app.client = get_client()  # pyright: ignore [reportAttributeAccessIssue]


templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "models": G4FModel.all(),
            "default_system_prompt": SYSTEM_PROMPT
        }
    )

@app.post("/execute", response_class=HTMLResponse)
async def execute_prompt_request(request: Request, model: G4FModel = Form(...), prompt: str = Form(...), system_prompt: str = Form(...), ):
    logger.info("Executing prompt with model %s", model)
    result = await execute_prompt(
        client=request.app.client,
        model=model, prompt=prompt,
        system_prompt=system_prompt
    )

    return templates.TemplateResponse("result.html", {"request": request, "result": result})
