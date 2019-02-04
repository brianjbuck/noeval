#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
MIT License

Copyright (c) 2019 Brian Buck

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import argparse
import subprocess
import sys


CMD = r"""grep -rn --include="*.py" -E '\beval\s*\((.*|\s*\))' {filename}"""


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    status_code = 0
    lines = []
    for filename in args.filenames:
        try:
            output = subprocess.check_output(
                [CMD.format(filename=filename)], shell=True
            )
        except subprocess.CalledProcessError:
            # `grep returned non-zero exit status 1.` ie:
            # Indicates that the pattern returned zero results.
            status_code |= 0
        else:
            for line in output.decode("utf-8").split("\n"):
                if line:
                    lines.append(line)
            status_code |= 1

    for line in lines:
        print(line)
    return status_code


if __name__ == "__main__":
    sys.exit(main())
