from datasets import load_dataset
import time
from pathlib import Path


def save_as_csv(data, file_name: str):
    outfile = Path(f'{file_name}.csv')
    rows = ['%s,%.6f,%.6f,%i\n' % row for row in zip(*data)]

    t0 = time.time()
    with open(outfile, 'a') as csvfile:
        csvfile.writelines(rows)
    tdelta = time.time() - t0
    print(tdelta)


data = load_dataset('suchkow/uspto-ai-patent-landscape', split='train')
save_as_csv(data, 'data/data-uspto')