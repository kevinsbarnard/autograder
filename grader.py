# grader.py
# Grading app
import argparse
import glob
import os


mars_jar = 'Mars4_5.jar'


def main(directory, n):
    files = glob.glob(os.path.join(directory, '*asm'))
    files.sort()
    filenames = [file.split(os.sep)[-1] for file in files]
    base_command = 'java -jar'
    arguments = [mars_jar, 'nc']
    for i, file in enumerate(files):
        print(('[LATE] ' if '_late_' in file else '') + filenames[i].split('_')[0])
        for _ in range(n):
            exit_code = int(os.system(' '.join([base_command] + arguments + [file])))
            if exit_code != 0:
                print('Exited with code', exit_code)
        print('-----')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, help='directory to scan for files')
    parser.add_argument('-n', type=int, default=1, help='number of test cases per input')
    args = parser.parse_args()
    main(args.dir, args.n)
