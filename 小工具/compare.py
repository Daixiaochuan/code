import csv
import os
from fuzzywuzzy import fuzz
from multiprocessing import Process


def process(start, end):
    # print(start)
    # 筛选剩下的种子对象
    file_path = "D:\\Web crawler Data\\Twitter2021\\apartment_no_all_80.csv"
    row_list0 = []
    row_list = []
    # 匹配度
    ppd = 70
    with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as fr:
        csv_reader = csv.reader(fr)
        for row in csv_reader:
            row_list0.append(row)
        # print('row_list0:', row_list0)
    with open("D:\\Web crawler Data\\Twitter2021\\apartment_search_all.csv", 'r', encoding='utf-8-sig', errors='ignore') as fr:
        csv_reader = csv.reader(fr)
        for row in csv_reader:
            row_list.append(row)
        # print('row_list:', row_list)
    do_crawl_row = []
    row_list = row_list[start: end+1]
    for row0 in row_list0:
        if len(row0[0].replace(' ', '')) == 0:
            continue
        for row in row_list:
            compare = fuzz.token_sort_ratio(row[1], row0[0])
            compare_id = fuzz.token_sort_ratio(row[2].lower(), row0[0].replace(' ', '').lower())
            # print('\n', compare, "<-", row[1], " : ", row0[0])
            if compare_id >= ppd or compare >= ppd:
                if row not in do_crawl_row:
                    print('\n', compare, "<-", row[1], " : ", row0[0])
                    print('\n', compare_id, "<--", row[2], " : ", row0[0].replace(' ', '').lower())
                    row.append(row0[0])
                    do_crawl_row.append(row)
    # 符合设定匹配度的种子对象
    with open("D:\\Web crawler Data\\Twitter_apart\\do_apartment"+str(start)+".csv", 'w', encoding='utf-8-sig', newline='') as fw:
        csvwrite = csv.writer(fw)
        csvwrite.writerows(do_crawl_row)
    print('do_crawl_row:', do_crawl_row)


def main():
    processnum = 16
    startnum = 0
    process_list = []
    # 根据已知信息（部门等）获取的所有对象
    with open("D:\\Web crawler Data\\Twitter2021\\apartment_search_all.csv", 'r', encoding='utf-8-sig', errors='ignore') as fr:
        reader = csv.reader(fr)
        column = [row[0] for row in reader]
    row = len(column)
    shengyu = row - startnum
    countnum = int(shengyu / processnum) + 1
    for i in range(processnum):
        startnum = startnum + countnum
        p1 = Process(target=process, args=(startnum - countnum, startnum - 1))
        print(startnum - countnum, startnum - 1)
        p1.start()
        process_list.append(p1)
    for t in process_list:
        t.join()


if __name__ == '__main__':
    main()
