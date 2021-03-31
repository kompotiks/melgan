from glob import glob
from tqdm import tqdm
import os
from sklearn.model_selection import train_test_split
import sys


def convert(path_dir, path_save='data'):
    for fpath in tqdm(glob(os.path.join(path_dir, '**', '*.wav'))):
        split_fpath =fpath.split(os.path.sep)
        if not os.path.exists(os.path.join(path_save, split_fpath[-2])): os.mkdir(os.path.join(path_save, split_fpath[-2]))
        os.system(f"ffmpeg -i {fpath} -loglevel quiet -ar 22050 -ac 1 {os.path.join(path_save, split_fpath[-2], split_fpath[-1])}")
        os.remove(fpath)


def train_test(path_data='data', final_data='mozilla_data'):
    if not os.path.exists(final_data): os.mkdir(final_data)
    if not os.path.exists(os.path.join(final_data, 'train')): os.mkdir(os.path.join(final_data, 'train'))
    if not os.path.exists(os.path.join(final_data, 'valid')): os.mkdir(os.path.join(final_data, 'valid'))

    data = os.listdir(path_data)
    train, valid, _, _ = train_test_split(data, range(len(data)), test_size=0.1, random_state=42)
    [os.system(f"mv {os.path.join(path_data, sample)} {os.path.join(final_data, 'train', sample)}") for sample in train]
    [os.system(f"mv {os.path.join(path_data, sample)} {os.path.join(final_data, 'valid', sample)}") for sample in valid]


if __name__ == '__main__':
    convert(sys.argv[1])
    train_test()