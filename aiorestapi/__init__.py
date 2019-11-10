#
#    Copyright 2019 Alessio Pinna <alessio@aiselis.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from .views import RestView
from .routers import RouteRestTableDef

__version__ = '0.1.0'

__all__ = (
    'RestView',
    'RouteRestTableDef',
)

routes = RouteRestTableDef()
