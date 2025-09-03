#!/usr/bin/env python3
"""
Testes para Flask App
"""

import pytest
import json
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    """Testa rota principal"""
    response = client.get("/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "running"
    assert "message" in data


def test_health_route(client):
    """Testa rota de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "healthy"


def test_info_route(client):
    """Testa rota de informações"""
    response = client.get("/info")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["framework"] == "Flask"
    assert "pipeline" in data
