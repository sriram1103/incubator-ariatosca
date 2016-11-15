# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import  # so we can import standard 'json'

import json
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from .reader import Reader
from .exceptions import ReaderSyntaxError


class JsonReader(Reader):
    """
    ARIA JSON reader.
    """

    def read(self):
        data = self.load()
        try:
            data = unicode(data)
            return json.loads(data, object_pairs_hook=OrderedDict)
        except Exception as e:
            raise ReaderSyntaxError('JSON: %s' % e, cause=e)
