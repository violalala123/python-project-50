from pathlib import Path

from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name):
    return str(Path(__file__).parent / 'test_data' / file_name)


def test_generate_diff_json():
    path1 = get_fixture_path('file1.json')
    path2 = get_fixture_path('file2.json')
    
    with open(get_fixture_path('result_test.txt'), 'r') as f:
        resultfile = f.read()
    
    assert generate_diff(path1, path2) == resultfile


def test_generate_diff_yml():
    path1 = get_fixture_path('file1.yml')
    path2 = get_fixture_path('file2.yml')
    
    with open(get_fixture_path('result_test.txt'), 'r') as f:
        resultfile = f.read()
    
    assert generate_diff(path1, path2) == resultfile
