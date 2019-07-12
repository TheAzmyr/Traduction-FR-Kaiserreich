import os
import argparse
import shutil
import zipfile
from time import gmtime, strftime


def get_args():
    parser = argparse.ArgumentParser(description='Update English files')
    parser.add_argument('steam', type=str, help='Steam mod directory')
    parser.add_argument('mod', type=str, help='Local mod directory')
    parser.add_argument('-unzip', type=str, help='Unzip directory (default directory upper mod directory)')
    return parser.parse_args()


def unzip(path_to_zip_file, directory_to_extract_to):
    print(f'Beginning of the extraction of {path_to_zip_file}')
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()
    print(f'End of the extraction of {path_to_zip_file}')
    print(f'{directory_to_extract_to} created.')


def main(args):
    # Compute unzip mod directory
    unzip_mod_dir = os.path.join(os.path.join(args.mod, '..', strftime("%Y_%m_%d_%H_%M_%S", gmtime())))
    if args.unzip is not None:
        unzip_mod_dir = args.unzip
        if os.path.exists(unzip_mod_dir):
            raise Exception(f'The unzip directory ({unzip_mod_dir}) already exists! Please change it.')

    # Unzip steam archive
    for file in os.listdir(args.steam):
        if file.endswith('.zip'):
            unzip(os.path.join(args.steam, file), unzip_mod_dir)

    # Remove old English files
    i = 0
    for file in os.listdir(os.path.join(args.mod, 'localisation')):
        if file.endswith('l_english.yml'):
            i += 1
            os.remove(os.path.join(args.mod, 'localisation', file))
    if os.path.exists(os.path.join(args.mod, 'localisation', 'replace')):
        for file in os.listdir(os.path.join(args.mod, 'localisation', 'replace')):
            if file.endswith('l_english.yml'):
                i += 1
                os.remove(os.path.join(args.mod, 'localisation', 'replace', file))
    print('{0} old files removed'.format(i))

    # Copy new English files
    i = 0
    for file in os.listdir(os.path.join(unzip_mod_dir, 'localisation')):
        if file.endswith('l_english.yml'):
            i += 1
            shutil.copyfile(os.path.join(unzip_mod_dir, 'localisation', file),
                            os.path.join(args.mod, 'localisation', file))
    if os.path.exists(os.path.join(unzip_mod_dir, 'localisation', 'replace')):
        for file in os.listdir(os.path.join(unzip_mod_dir, 'localisation', 'replace')):
            if file.endswith('l_english.yml'):
                i += 1
                shutil.copyfile(os.path.join(unzip_mod_dir, 'localisation', 'replace', file),
                                os.path.join(args.mod, 'localisation', 'replace', file))
    print('{0} new files copied'.format(i))


if __name__ == "__main__":
    # execute only if run as a script
    args = get_args()
    main(args)
