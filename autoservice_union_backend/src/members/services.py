import re


def fix_bad_json(bad_json_bytes):
    bad_json_str = bad_json_bytes.decode('utf-8')

    fixed_json_str = bad_json_str.replace('\\"', '"')

    fixed_json_str = re.sub(r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', '', fixed_json_str)

    return fixed_json_str