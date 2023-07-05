from app.services.pegawai.service import ServicePegawai
from app import app

pegawai = ServicePegawai()

@app.route("/pegawai/<string:name>",methods=["GET"])
def get_pegawai_Byname(name):
    return pegawai.get_by_name(name)
    

