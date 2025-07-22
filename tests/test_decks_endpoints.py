from unittest.mock import MagicMock
from src.app.services.decks_services import decks_services
from src.app.utils.responses.response import APIResponse

GET_ALL_DECKS_ENDPOINT = "/api/decks"

""" Testa se a rota GET_ALL_DECKS retorna 200 OK. """
def test_get_all_decks_status_codes(client, monkeypatch):
    mock_get_all_decks = MagicMock(return_value=[])
    monkeypatch.setattr(decks_services, "get_all_decks", mock_get_all_decks)
    
    response = client.get(GET_ALL_DECKS_ENDPOINT)
    assert response.status_code == 200

""" Testa se a resposta da rota GET_ALL_DECKS retorna um JSON válido. """
def test_get_all_decks_fetch(client, monkeypatch):
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
    
    response = client.get(GET_ALL_DECKS_ENDPOINT)
    data = response.get_json()
    assert data
    assert isinstance(data.get("data"), list)

""" Testa se a resposta da rota GET_ALL_DECKS contém as chaves esperadas. """
def test_api_response_success_model(app):
    with app.app_context():
        response, _ = APIResponse.success(message='Ok', data={"foo": "bar"}, status_code=200)
        data = response.get_json()

        assert data['success'] is True
        assert data['message'] == 'Ok'
        assert data['data'] == {"foo": "bar"}

""" Testa se os campos necessários do Payload da API. """
def test_get_all_decks_fetch_fields_in_data(client):
    response = client.get(GET_ALL_DECKS_ENDPOINT)
    formated_response = response.get_json()
    data = formated_response["data"]
    
    assert data[0]["id"]
    assert data[0]["title"]
    assert data[0]["description"]
    assert data[0]["tags"]
    assert data[0]["created_at"]
    assert data[0]["updated_at"]
    
"""Testa as flags do campo message """
def test_get_all_decks_response_success_flag(client):
    response = client.get(GET_ALL_DECKS_ENDPOINT)
    formated_response = response.get_json()
    field_success = formated_response["success"]
    assert field_success == True