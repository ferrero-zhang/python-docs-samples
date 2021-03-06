# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

import load_data_from_file

DATASET_ID = 'test_dataset'
TABLE_ID = 'test_import_table'


@pytest.mark.xfail(
    strict=True,
    reason='https://github.com/GoogleCloudPlatform/gcloud-python/issues/2133')
def test_load_table(resource, capsys):
    data_path = resource('data.csv')

    load_data_from_file.load_data_from_file(
        DATASET_ID,
        TABLE_ID,
        data_path)

    out, _ = capsys.readouterr()

    assert 'Loaded 1 rows' in out
