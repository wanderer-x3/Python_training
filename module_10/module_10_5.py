import multiprocessing
import time

def read_info(name):
    all_data = []

    with open(name) as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    t_go = time.time()
    for name in filenames:
        read_info(name)
    t_end = time.time()
    print(f'{t_end - t_go} c')

    # Многопроцессный
    t_go = time.time()
    with multiprocessing.Pool(5) as pool:
        results = pool.map(read_info, filenames)
    t_end = time.time()
    print(f'{t_end - t_go} c')
