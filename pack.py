#!/usr/bin/env python
# -*- encodint=utf-8 -*-


import zipfile
import os
import subprocess

__author__ = "Ricky"


class Pack(zipfile.ZipInfo):
    def __init__(self):
        self.source_dir = None
        self.des_dir = None
        self.file_name = None
        self.file_list = None
        self.pwd = None

    def set_source_dir(self, source_dir):
        """
        set source dictory
        :param source_dir: 
        :return: 
        """
        self.__exist_dir(source_dir)
        self.source_dir = source_dir

    def set_des_dir(self, des_dir, file_name):
        """
        
        :param des_dir: 
        :return: 
        """
        self.__exist_dir(des_dir)
        self.des_dir = des_dir
        self.file_name = file_name

    def set_pack_list(self, file_list):
        """
        
        :param list file_list: 
        :return: bool
        """
        self.__exist_file(file_list, self.source_dir)
        self.file_list = file_list

    def set_pwd(self, pwd):
        self.pwd = pwd

    def pack(self):
        z = zipfile.ZipFile(self.des_dir + os.path.sep + self.file_name, 'w')
        for file in self.file_list:
            file_path = self.source_dir + os.path.sep + file
            ret = subprocess.Popen('php -l D:/test.php', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
            ret.wait()
            if ret.returncode != 0:
                raise PHPSyntaxError("Syntax error:"+file)
            z.write(file_path, file)
        if self.pwd is not None:
            z.setpassword(self.pwd)
        z.close()

    def __exist_dir(self, dictory):
        if os.path.isdir(dictory) is False:
            raise DirNotFound("Path not found: %s" % dictory)
        return True

    def __exist_file(self, file_lists, path):
        """
        
        :param list file_lists: 
        :return: 
        """
        for filestr in file_lists:
            file_path = path + os.path.sep + filestr
            if os.path.exists(file_path) is False:
                raise FileNotFound("File not found: %s" % file_path)
        return True


class DirNotFound(Exception):
    def __init__(self, err):
        Exception.__init__(self)
        self.message = err


class FileNotFound(Exception):
    def __init__(self, err):
        Exception.__init__(self)
        self.message = err

class PHPSyntaxError(Exception):
    def __init__(self, err):
        Exception.__init__(self)
        self.message = err
