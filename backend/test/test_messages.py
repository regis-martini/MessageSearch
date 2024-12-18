def test_upload_messages(client):
    # Simulate a JSON file upload
    response = client.post(
        "/api/v1/messages/upload",
        files={"file": ("messages.json", '[{"content": "Hello, World!"}]', "application/json")},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"