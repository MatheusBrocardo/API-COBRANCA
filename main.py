from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from db import Database
from tasks.Inadimplencia import adicionarTitulos
import uvicorn

# from controllers import Token
# # instancia o monitorramento
# sentry_sdk.init(
#         dsn="https://b879fb2efdf9369b874dcdae282430b9@o1221283.ingest.us.sentry.io/4507487931727872",
#         # Set traces_sample_rate to 1.0 to capture 100%
#         # of transactions for performance monitoring.
#         traces_sample_rate=1.0,
#         # Set profiles_sample_rate to 1.0 to profile 100%
#         # of sampled transactions.
#         # We recommend adjusting this value in production.
#         profiles_sample_rate=1.0,
#)

app = FastAPI()

# Permitir todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app)

