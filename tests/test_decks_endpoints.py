
def test_get_all_decks(client):
    response = client.get("/api/decks")
    
    data = response.get_json()
    
    assert response.status_code == 200
    assert 'message' in data
    assert 'data' in data
    assert 'success' in data
