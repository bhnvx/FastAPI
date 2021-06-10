from dataclasses import asdict

from fastapi import FastAPI
import uvicorn

from app.setting.config import conf
from app.DB.conn import db
from app.routes import index, auth


def create_app():
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # 라우터 정의
    # app.include_router(index.router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host= "0.0.0.0", port= 8000, reload= True)