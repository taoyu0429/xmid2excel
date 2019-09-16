#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import logging
import sys
from xmind2xls.zentao import xmind_to_zentao_csv_file
from xmind2xls.testlink import xmind_to_testlink_xml_file
from xmind2xls.excel import xmind_to_xlsx_file
from xmind2xls.utils import get_absolute_path, xmind_testcase_to_json_file


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s  %(name)s  %(levelname)s  [%(module)s - %(funcName)s]: %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S')

def cli_main():

    if len(sys.argv) > 1 and sys.argv[1].endswith('.xmind'):
        xmind_file = sys.argv[1]
        xmind_file = get_absolute_path(xmind_file)
        logging.info('Start to convert XMind file: %s', xmind_file)

        if len(sys.argv) == 3 and sys.argv[2] == '-json':
            testlink_json_file = xmind_testcase_to_json_file(xmind_file)
            logging.info('Convert XMind file to testcase json file successfully: %s', testlink_json_file)
        elif len(sys.argv) == 3 and sys.argv[2] == '-xml':
            testlink_xml_file = xmind_to_testlink_xml_file(xmind_file)
            logging.info('Convert XMind file to testlink xml files successfully: %s', testlink_xml_file)
        elif len(sys.argv) == 3 and sys.argv[2] == '-csv':
            zentao_csv_file = xmind_to_zentao_csv_file(xmind_file)
            logging.info('Convert XMind file to zentao csv file successfully: %s', zentao_csv_file)
        elif len(sys.argv) == 3 and sys.argv[2] == '-xlsx':
            excel_xlsx_file = xmind_to_xlsx_file(xmind_file)
            logging.info('Convert XMind file to zentao csv file successfully: %s', excel_xlsx_file)
        else:
            testlink_json_file = xmind_testcase_to_json_file(xmind_file)
            testlink_xml_file = xmind_to_testlink_xml_file(xmind_file)
            zentao_csv_file = xmind_to_zentao_csv_file(xmind_file)
            logging.info('Convert XMind file successfully: \n'
                         '1、 testcase json file(%s)\n'
                         '2、 testlink xml file(%s)\n'
                         '3、 zentao csv file(%s)',
                         testlink_json_file,
                         testlink_xml_file,
                         zentao_csv_file)


    else:
        print(__doc__)
        logging.error('%s', __doc__)


if __name__ == '__main__':
    cli_main()
