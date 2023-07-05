from app.repository.pegawai.repo import RepoPegawai
from app.utils.response.response import *
from app import db


class ServicePegawai:
    def __init__(self) -> None:
        self.repo = RepoPegawai(db)

    def get_by_name(self, name):
        err, data = self.repo.get_by_name(name)
        if not err:
            data = self.formatted_data(data)
            return successRequest(values=data, message=response_get_success)
        return badRequest(message=response_get_success)

    def formatted_data_single(self, data):
        tmp = []
        tmp.append(
            {
                "name": data.name,
                "date": data.date,
            }
        )
        return tmp

    def formatted_data_multi_single(self, data):
        tmp = []
        for data in data:
            tmp.append(
                {
                    "name": data.name,
                    "date": data.date,
                }
            )
        return tmp

    def formatted_data(self, data):
        if isinstance(data, list):
            return self.formatted_data_multi_single(data)
        return self.formatted_data_single(data)
