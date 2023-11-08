"""HadObs data portal."""

import subprocess

from cmatools.io.common import check_url, compliance_checker, list_files_from_html


def check_hadobs_dataset_netcdfs(dataset, test_logs):
    """Run compliance checker on hadobs netcdfs."""
    files = list_files_from_html(dataset, filetype=".nc")
    test_logs.mkdir(parents=True, exist_ok=True)

    for file in files:
        access = check_url(file)
        print(f"File: {file}, accessible: {access}")
        try:
            out = compliance_checker(file, criteria="lenient", logs=test_logs)
        except subprocess.CalledProcessError as err:
            print(f"Test failed for {file}")
            print(err)
            print(out)
            # TODO refactor
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/canned_data/test_canned_data.py
    # integration: b_integration/canned_data/test_canned_data.py
    # ---------------------------------------------------------------------------


def check_hadobs_file_access(dataset, filetype, test_logs):
    """Check file access for hadobs netcdfs."""
    files = list_files_from_html(dataset, filetype=filetype)
    test_logs.mkdir(parents=True, exist_ok=True)
    failed = []
    for file in files:
        access = check_url(file)
        print(f"File: {file}, accessible: {access}")
        if access is not True:
            failed.append(file)
    if failed:
        return False
    else:
        return True
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/canned_data/test_canned_data.py
    # integration: b_integration/canned_data/test_canned_data.py
    # ---------------------------------------------------------------------------
