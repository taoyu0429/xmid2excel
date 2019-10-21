from openpyxl import Workbook
import datetime
import os
import xmind
import logging
from xmind2xls.utils import get_xmind_testcase_list, get_absolute_path

def xmind_to_xlsx_file(xmind_file):
    """Convert XMind file to a excel xlsx file"""
    xmind_file = get_absolute_path(xmind_file)
    logging.info('Start converting XMind file(%s) to xlsx file...', xmind_file)
    testcases = get_xmind_testcase_list(xmind_file)

    fileheader = ["功能点", "案例编号", "测试意图", "要素组合",  "前置条件", "测试步骤",  "预期结果", "案例性质", "案例级别", "案例来源"]

    xlsx_testcase_rows = [fileheader]
    i = 1
    for testcase in testcases:
        row = gen_a_testcase_row(i, testcase)
        xlsx_testcase_rows.append(row)
        i = i+1
    wb = Workbook()
    dest_filename = xmind_file[:-6] + '.xlsx'
    ws1 = wb.active
    ws1.title = "分析单元名称"
    for row in range(0,len(xlsx_testcase_rows)):
        for col in range(0, len(xlsx_testcase_rows[row])):
            _ = ws1.cell(column=col+1, row=row+1, value=xlsx_testcase_rows[row][col])

    wb.save(filename=dest_filename)
    """
       zentao_file = xmind_file[:-6] + '.xlsx'
    if os.path.exists(zentao_file):
        logging.info('The zentao csv file already exists, return it directly: %s', zentao_file)
        return zentao_file
   
 

    with open(zentao_file, 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(zentao_testcase_rows)
        logging.info('Convert XMind file(%s) to a zentao csv file(%s) successfully!', xmind_file, zentao_file)

    return zentao_file
    
 """

def gen_a_testcase_row(serialnumber, testcase_dict):
    case_module = gen_case_module(testcase_dict['suite'])
    case_title = testcase_dict['function']+"-"+testcase_dict['checkpoint']
    case_precontion = testcase_dict['preconditions']
    case_step, case_expected_result = gen_case_step_and_expected_result(testcase_dict['steps'])
    case_id = 'TC-'+testcase_dict['id']+"-"+str(serialnumber)
    '''
    case_keyword = '功能测试'
    case_apply_phase = '迭代测试'
    
    '''
    case_summary = testcase_dict['summary']
    case_submodel = testcase_dict['module']
    case_function = testcase_dict['function']
    case_priority = gen_case_priority(testcase_dict['importance'])
    case_type =testcase_dict['execution_type']
    case_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    row = [case_function, case_id, case_title, case_summary, case_precontion, case_step, case_expected_result, case_type, case_priority]
    return row


def gen_case_module(module_name):
    if module_name:
        module_name = module_name.replace('（', '(')
        module_name = module_name.replace('）', ')')
    else:
        module_name = '/'
    return module_name


def gen_case_step_and_expected_result(steps):
    case_step = ''
    case_expected_result = ''

    for step_dict in steps:
        case_step += str(step_dict['step_number']) + '. ' + step_dict['actions'].replace('\n', '').strip() + '\n'
        '''
         case_expected_result += 'check[{0}]'.format(step_dict['step_number']) + \
            step_dict['expectedresults'].replace('\n', '').strip() + '\n' \
            if step_dict.get('expectedresults', '') else ''
        '''
        case_expected_result +=step_dict['expectedresults'].replace('\n', '').strip() + '\n' \
        if step_dict.get('expectedresults', '') else ''

    return case_step, case_expected_result


def gen_case_priority(priority):
    mapping = {1: '高', 2: '中', 3: '低'}
    if priority in mapping.keys():
        return mapping[priority]
    else:
        return '中'


def gen_case_type(case_type):
    mapping = {1: '手动', 2: '自动'}
    if case_type in mapping.keys():
        return mapping[case_type]
    else:
        return '手动'