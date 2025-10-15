from controllers.createTasks import router

def register_task_routes(app):
    app.include_router(router, prefix="/tasks", )