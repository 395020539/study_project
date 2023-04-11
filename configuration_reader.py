#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import os


class MyConfig:
    def __init__(self):
        mypath = MyPath()
        self.return_code, self.doors_username, self.doors_password, \
            self.doors_project_path, self.new_dic_module, self.data_file \
            = self.read_config(mypath.config_path, mypath.app_dir, mypath.data_path)
        self.doors_exe_path = r'C:\Program Files (x86)\ibm\Rational\DOORS\9.5\bin\doors.exe'

    def read_config(self, config_path, app_dir, data_path):
        return_code = "0"
        doors_username = ""
        doors_password = ""
        doors_project_path = ""
        dic_module = ""
        data_suffix = ""
        new_dic_module = {}
        try:
            with open(config_path, 'r', encoding='utf - 8') as f:
                print(f)
                json_data = json.load(f)
                # print(f"json_data = \n{json_data}")
                doors_username = json_data['doors_username']
                print(f"doors_username = \n{doors_username}")
                doors_password = json_data['doors_password']
                print(f"doors_password = \n{doors_password}")
                doors_project_path = "/" + json_data['project_name']
                print(f"doors_project_path = \n{doors_project_path}")
                dic_module = json_data['dic_module']
                # print(f"dict_module = \n{dic_module}")
                data_suffix = json_data['data_suffix']
                print(f"data_suffix = \n{data_suffix}")
                new_dic_module = self.reform_dic_module(dic_module, data_suffix)
                print(f"new_dic_module = \n{new_dic_module}")
                data_file = json_data['data_file']
                data_file = os.path.join(data_path, data_file)
                print(f"data_file = \n{data_file}")
        except Exception as e:
            print("An error occurred:", e)
            return_code = "1"
        finally:
            return return_code, doors_username, doors_password, doors_project_path, new_dic_module, data_file

    def reform_dic_module(self, ori_dic_module, suffix):
        """在data module名称后面加上suffix"""
        new_dic_module = {}
        if len(ori_dic_module) > 0:
            if len(suffix) != 0:
                for key in ori_dic_module:
                    new_dic_module[key] = ori_dic_module[key] + suffix
            else:
                new_dic_module = ori_dic_module
        else:
            new_dic_module = ori_dic_module
        # print("reform_dic_module: ", new_dic_module)
        return new_dic_module


class MyPath:
    def __init__(self):
        self.app_dir, self.config_path, self.data_path = self.get_current_path()

    def get_current_path(self):
        # 获取可执行文件的路径
        if getattr(sys, 'frozen', False):
            # 如果是打包后的 exe 文件，获取可执行文件的路径
            app_dir = os.path.dirname(sys.executable)
        else:
            # 如果是源代码，获取脚本文件所在的目录
            app_dir = os.path.dirname(os.path.abspath(__file__))
        print("app_dir = ", app_dir)
        config_path = os.path.join(app_dir, 'Config\module_cfg.json')
        print("config_path = ", config_path)
        data_path = os.path.join(app_dir, 'Data')
        print("data_path = ", data_path)
        return app_dir, config_path, data_path


if __name__ == '__main__':
    mypath = MyPath()
    print(mypath.app_dir, mypath.config_path, mypath.data_path)

    myconfig = MyConfig()
    print("doors_username: ", myconfig.doors_username)
    print("doors_password: ", myconfig.doors_password)
    print("doors_project_path: ", myconfig.doors_project_path)
    print("new_dic_module: ", myconfig.new_dic_module)
    print("data_file: ", myconfig.data_file)
    print("doors_exe_path: ", myconfig.doors_exe_path)
