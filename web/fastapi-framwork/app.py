from fastapi import FastAPI
from app.common.response import Response
from app.common.requests import *
app = FastAPI()


@app.post("/get_bind_tel/")
async def get_bind_tel(request: GetBindTelRequest):
    request_dt = request.dict()
    # print(request_dt)
    res_data = dict(
        caller_show='',
        called_show='',
        bind_id='',
    )
    return Response.success(res_data)


@app.post("/get_call_report/")
async def get_call_report(request: GetCallReportRequest):
    request_dt = request.dict()
    DB.insert_call_report(request_dt)
    return Response.success('')
