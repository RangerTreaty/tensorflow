import os
from typing import List

from wai.common.file.report.constants import EXTENSION as REPORT_EXT


def get_files_from_directory(directory: str) -> List[str]:
    """
    Recursively gets the report files from all sub-directories of the
    given directory (including itself).

    :param directory:   The top-level directory to search.
    :return:            The list of filenames.
    """
    report_files = list()

    for subdir, dirs, files in os.walk(directory):
        report_files += (os.path.join(directory, subdir, file)
                         for file in files
                         if file.endswith(REPORT_EXT))

    return report_files