from pytest import mark
from unittest.mock import MagicMock, patch
from src.app.services.decks_services import decks_services
from src.app.utils.responses.response import APIResponse
from src.app.blueprints.constants.routes import DECKS as routes
from src.app.blueprints.api.decks import controller

url_get_all_decks = routes.get("get_all_decks").get("URI")

#
@mark.integration
@mark.controllers
def test_get_all_decks_status_codes(client):
    """ Testa se a rota GET_ALL_DECKS retorna 200 OK. """
    response = client.get(url_get_all_decks)
    assert response.status_code == 200
#
@mark.integration
@mark.controllers
def test_get_all_decks_fetch(client, monkeypatch):
    """ Testa se a resposta da rota GET_ALL_DECKS retorna um JSON válido. """
    
    mock_get_all_decks = MagicMock(
        return_value=[{
                'id': "Mock - UUID", 
                'title': 'Mock - Deck 1',
                'description': 'Mock - Description for Deck 1',
                'tags': ['Mock - tag1', 'Mock - tag2'],
                'created_at': 'Mock - 2023-10-01T12:00:00Z',
                'updated_at': 'Mock - 2023-10-01T12:00:00Z'
            }])
    
    monkeypatch.setattr(decks_services, "get_all_decks", mock_get_all_decks)
    
    response = client.get(url_get_all_decks)
    data = response.get_json()
    assert data
    assert isinstance(data.get("data"), list)
#
@mark.integration
@mark.controllers
def test_api_response_success_model(app):
    """ Testa se a resposta da rota GET_ALL_DECKS contém as chaves esperadas. """
    with app.app_context():
        response, _ = APIResponse.success(message='Ok', data={"foo": "bar"}, status_code=200)
        data = response.get_json()

        assert data['success'] is True
        assert data['message'] == 'Ok'
        assert data['data'] == {"foo": "bar"}
#
@mark.integration
@mark.controllers
def test_get_all_decks_fetch_fields_in_data(client):
    """ Testa se os campos necessários do Payload da API. """
    
    response = client.get(url_get_all_decks)
    formated_response = response.get_json()
    data = formated_response["data"]
    
    assert data[0]["id"]
    assert data[0]["title"]
    assert data[0]["description"]
    assert data[0]["tags"]
    assert data[0]["created_at"]
    assert data[0]["updated_at"]
#
@mark.integration
@mark.controllers
def test_get_all_decks_empty_list(client):
    """ Testa resposta quando o deck está vazio """
    
    with patch("src.app.blueprints.api.decks.controller.get_all_decks") as mocked_get_all:
        mocked_get_all.return_value = (
            {"success": True, "message": "No decks found", "data": []}, 200
        )
        response = client.get(url_get_all_decks)
        data = response.get_json()

        assert response.status_code == 200
        assert data["success"] is True
        assert data["data"] == []
        assert isinstance(data["data"], list)
#
@mark.integration
@mark.controllers
def test_get_all_decks_response_success_flag(client):
    """ Testa as flags do campo message. """
    
    response = client.get(url_get_all_decks)
    formated_response = response.get_json()
    field_success = formated_response["success"]
    assert field_success == True