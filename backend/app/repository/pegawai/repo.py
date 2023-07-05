from app.repository.pegawai.entity import Pegawai


class RepoPegawai:
    def __init__(self, db) -> None:
        self.db = db

    def save(self, ObjPegawai):
        pegawai = Pegawai()
        p = ObjPegawai()
        err = False

        try:
            pegawai.name = p.name
            pegawai.date = p.date
            pegawai.created_at = p.created_at
            self.db.session.add(pegawai)
            self.db.session.commit()
        except Exception as e:
            print(e)
            err = True
        return err, pegawai

    def get_by_name(self, name):
        pegawai = Pegawai()
        err = False

        try:
            pegawai = (
                self.db.session.query(Pegawai).filter(Pegawai.name == name).first()
            )
        except Exception as e:
            print(e)
            err = True
        return err, pegawai
