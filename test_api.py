import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Сценарий 1 
def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    assert response.status_code == 201
    
    response_json = response.json()
    assert response_json["title"] == "foo"
    assert response_json["body"] == "bar"
    assert "id" in response_json


# Сценарий 2 
def test_update_post():
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    
    assert response.status_code == 200
    
    response_json = response.json()
    assert response_json["title"] == "updated title"
    assert response_json["body"] == "updated body"


# Сценарий 3 
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    assert response.json() == {}


# Сценарий 4 
def test_get_post_comments():
    response = requests.get(f"{BASE_URL}/posts/1/comments")
    
    assert response.status_code == 200
    
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) > 0


# Сценарий 5 
def test_get_non_existent_post():
    response = requests.get(f"{BASE_URL}/posts/9999")
    
    assert response.status_code == 404
    
    assert response.json() == {}