from controllers.auth import router

def register_auth_routes(app):
    app.include_router(router, prefix="/auth")