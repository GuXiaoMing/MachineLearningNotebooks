
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import os


def init():
    print("Init")


def run(mini_batch):
    print(f'run method start: {__file__}, run({mini_batch})')
    print(f'total_file_count = {len(mini_batch)}')
    file_size_list = []
    total_file_size = 0
    for file_path in mini_batch:
        file_size = os.path.getsize(file_path)
        file_size_list.append(file_size)
        total_file_size += file_size
    print(f'total_file_size = {total_file_size}')

    return file_size_list
