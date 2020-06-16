from pydantic import BaseModel


class GetBindTelRequest(BaseModel):
    corp_key: str
    ts: int
    sign: str
    called: str
    caller: str
    recorder_id: str


class GetCallReportRequest(BaseModel):
    corp_key: str
    ts: int
    sign: str
    recorder_id: str
    called: str
    caller: str
