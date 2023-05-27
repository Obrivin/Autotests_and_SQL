import configuration
import requests
import data


def create_new_order(): # запрос на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_A_NEW_ORDER,  # подставялем полный url
                         json=data.order_body)  # а здесь тело



def get_orders_track(track_id): # запрос на получение заказа по его трек номеру
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_AN_ORDER_BY_ID + "?t=" + str(track_id))