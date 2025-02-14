# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making GameAISDK available.

This source code file is licensed under the GNU General Public License Version 3.
For full details, please refer to the file "LICENSE.txt" which is provided as part of this source code package.

Copyright (C) 2020 THL A29 Limited, a Tencent company.  All rights reserved.
"""

from abc import ABCMeta, abstractmethod


class TaskInterface(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, task_id: int, task_name: str, **kwargs) -> tuple:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, task_id: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def alloc_id(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def get(self, task_id: int):
        raise NotImplementedError()

    @abstractmethod
    def get_all(self) -> list:
        raise NotImplementedError()

    @abstractmethod
    def load(self, task_config: dict) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def dump(self, task_config: dict) -> bool:
        raise NotImplementedError()
