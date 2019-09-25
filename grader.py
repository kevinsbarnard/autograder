# grader.py
# Grading app
import argparse
import glob
import os


mars_jar = 'Mars4_5.jar'
extension = 'asm'


def main(directory, n):
    all_files = glob.glob(os.path.join(directory, '*'))
    files = glob.glob(os.path.join(directory, '*{}'.format(extension)))
    non_asm_files = list(set(all_files) - set(files))
    if non_asm_files:
        print('WARNING - {} file(s) found in directory without extension {}:'.format(len(non_asm_files), extension))
        for non_asm in non_asm_files:
            print(os.path.basename(non_asm))
        print('--/!\\--')
    files.sort()
    filenames = [file.split(os.sep)[-1] for file in files]
    base_command = 'java -jar'
    arguments = [mars_jar, 'nc']
    for i, file in enumerate(files):
        print(('[LATE] ' if '_late_' in file else '') + filenames[i].split('_')[0])
        for _ in range(n):
            exit_code = int(os.system(' '.join([base_command] + arguments + ["\"{}\"".format(file)])))
            if exit_code != 0:
                print('Exited with code', exit_code)
        print('-----')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, help='directory to scan for files')
    parser.add_argument('-n', type=int, default=1, help='number of test cases per input')
    args = parser.parse_args()
    main(args.dir, args.n)
