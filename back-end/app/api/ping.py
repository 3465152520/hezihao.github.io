from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    """
    用于测试前端vue与后端flask api的连通性
    :return:
    """
    return jsonify('Pong!!!')

