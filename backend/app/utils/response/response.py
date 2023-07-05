from flask import jsonify, make_response

response_insert_success = "Berhasil menyimpan data"
response_insert_fail = "Gagal menyimpan data"
response_get_success = "Behasil mengambil data"
response_get_fail = "Gagal mengambil data"
response_not_found_file = "File tidak tersedia"


def successRequest(message, values=[]):
    res = {"data": values, "message": message}

    return make_response(jsonify(res)), 200


def badRequest(message, values=[]):
    res = {"data": values, "message": message}

    return make_response(jsonify(res)), 400
