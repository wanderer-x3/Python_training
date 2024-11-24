from time import sleep, time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for nut_ in range(word_count):
            nut_ = str(nut_ + 1)
            file.write("Какое-то слово №" + nut_ + "\n")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")


if __name__ == "__main__":
    st = time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    et = time()
    dt = et - st
    print(f'Работа потоков: {dt} сек.')
    st = time()
    thread5 = threading.Thread(target=write_words, args=(10, "example5.txt",)).start()
    thread6 = threading.Thread(target=write_words, args=(30, "example6.txt",)).start()
    thread7 = threading.Thread(target=write_words, args=(200, "example7.txt",))
    thread8 = threading.Thread(target=write_words, args=(100, "example8.txt",)).start()
    thread7.start()
    thread7.join()
    et = time()
    dt = et - st
    print(f'Работа потоков: {dt} сек.')
