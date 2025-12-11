from backend.app.main import create_app


def test_health_route_returns_ok():
    app = create_app()
    health_route = next(r for r in app.router.routes if getattr(r, "path", "") == "/health")
    assert health_route.endpoint() == {"status": "ok"}
