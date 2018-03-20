# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The test file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""
import glob
import os
import xlrd
import xlsxwriter
import xlwt


def main(in_files, to_dir):
    for in_file in glob.glob(in_files):
        to_file = to_dir + "/" + os.path.split(in_file)[-1]
        print("%s -> %s" % (in_file, to_file))
        workbook = xlrd.open_workbook(in_file)
        table = workbook.sheets()[0]
        nrows = table.nrows
        header = None
        susp_rows = []
        conf_rows = []
        for i in range(nrows):
            row = table.row_values(i)
            if i == 0:
                header = row
            else:
                susp_prob = row[7]
                if float(susp_prob) != 0.0:
                    query_id = str(int(float(row[6])))
                    row[6] = query_id
                    predict_id = str(int(float(row[9])))
                    row[9] = predict_id
                    if query_id == predict_id:
                        row[7] = 0
                        conf_rows.append(row)
                    else:
                        susp_rows.append(row)
                else:
                    conf_rows.append(row)

        conf_rows = sorted(conf_rows, key=lambda x: x[8])

        _write_rows_to_excel(header, susp_rows + conf_rows, to_file)


def _write_rows_to_excel(header, rows, to_file):
    workbook = xlsxwriter.Workbook(to_file)
    sheet = workbook.add_worksheet()
    row_index = 0
    row_index = _write_row_in_sheet(row_index, header, sheet)
    for row in rows:
        row_index = _write_row_in_sheet(row_index, row, sheet)
    workbook.close()


def _write_row_in_sheet(row_index, row, sheet):
    for i, item in enumerate(row):
        sheet.write(row_index, i, item)
    return row_index + 1


if __name__ == '__main__':
    main("data/*.xlsx", to_dir="output")