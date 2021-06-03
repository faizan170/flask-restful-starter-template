from config import api
from views.appViews import (
    TestRoute
)


api.add_resource(TestRoute, "/test")