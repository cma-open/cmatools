from pathlib import Path

from cmatools.io.io_common import (extract_archive_singlefile,
                                   write_source_config,
                                   datadir_inputs_dir)


def test_extract_archive_singlefile():

    filename = "eobs.tgz"
    extractedfile = extract_archive_singlefile(filename)
    file = Path(datadir_inputs_dir() / extractedfile)
    print("Test ouput")
    print(extractedfile)
    print(file)

    assert file.is_file()


def test_write_source_config():

    archivename = 'arcfile'
    extractfilename = 'extfile'

    write_source_config(archivename,extractfilename)

