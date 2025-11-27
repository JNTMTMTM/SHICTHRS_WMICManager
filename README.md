# SHICTHRS WMIC Manager

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)](https://www.microsoft.com/windows)

SHICTHRS WMIC Manager 是一个用于管理 Windows 系统中 WMIC (Windows Management Instrumentation Command-line) 工具的 Python 库。它提供了一组简单易用的函数，用于检查 WMIC 的可用性以及在 Windows 10 和 Windows 11 系统上安装/卸载 WMIC 功能。

## 特性

- 检查系统中 WMIC 的可用性
- 在 Windows 10 上安装 WMIC 功能
- 在 Windows 11 上安装/卸载 WMIC 功能
- 提供友好的异常处理和错误报告
- 支持 subprocess 终端窗口显示
- 彩色控制台输出

## 安装

```bash
pip install SHICTHRSWMICManager
```

或者从源码安装：

```bash
git clone https://github.com/JNTMTMTM/SHICTHRS_WMICManager.git
cd SHICTHRS_WMICManager
pip install -e .
```

## 快速开始

```python
from SHICTHRSWMICManager import *

# 检查 WMIC 是否可用
is_available, return_code = SHRWMICManager_check_is_wmic_available()
if is_available:
    print("WMIC 可用")
else:
    print("WMIC 不可用")

# 在 Windows 10 上安装 WMIC
try:
    result, return_code = SHRWMICManager_install_wmic_win10()
    print("WMIC 安装成功")
except SHRWMICManagerException as e:
    print(f"安装失败: {e}")

# 在 Windows 11 上安装 WMIC
try:
    result, return_code = SHRWMICManager_install_wmic_win11()
    print("WMIC 安装成功")
except SHRWMICManagerException as e:
    print(f"安装失败: {e}")

# 在 Windows 11 上卸载 WMIC
try:
    result, return_code = SHRWMICManager_uninstall_wmic_win11()
    print("WMIC 卸载成功")
except SHRWMICManagerException as e:
    print(f"卸载失败: {e}")
```

## API 文档

### SHRWMICManager_check_is_wmic_available()

检查系统中 WMIC 的可用性。

**返回值:**
- `tuple`: (is_available, return_code)
  - `is_available` (bool): WMIC 是否可用
  - `return_code` (int): 返回代码

### SHRWMICManager_install_wmic_win10()

在 Windows 10 系统上安装 WMIC 功能。

**返回值:**
- `tuple`: (success, return_code)
  - `success` (bool): 安装是否成功
  - `return_code` (int): 返回代码

**异常:**
- `SHRWMICManagerException`: 安装失败时抛出

### SHRWMICManager_install_wmic_win11()

在 Windows 11 系统上安装 WMIC 功能。

**返回值:**
- `tuple`: (success, return_code)
  - `success` (bool): 安装是否成功
  - `return_code` (int): 返回代码

**异常:**
- `SHRWMICManagerException`: 安装失败时抛出

### SHRWMICManager_uninstall_wmic_win11()

在 Windows 11 系统上卸载 WMIC 功能。

**返回值:**
- `tuple`: (success, return_code)
  - `success` (bool): 卸载是否成功
  - `return_code` (int): 返回代码

**异常:**
- `SHRWMICManagerException`: 卸载失败时抛出

## 系统要求

- Python 3.6 或更高版本
- Windows 10 或 Windows 11 操作系统
- 管理员权限（用于安装/卸载 WMIC 功能）
- 依赖项：colorama==0.4.6

## 错误处理

本库使用自定义的 `SHRWMICManagerException` 异常类来处理所有错误。每个错误都有唯一的错误代码，便于调试：

- ERROR.7000: 检查 WMIC 可用性时出错
- ERROR.7001: 在 Windows 10 上安装 WMIC 时出错
- ERROR.7002: Windows 10 WMIC 安装过程中的错误
- ERROR.7003: 在 Windows 11 上安装 WMIC 时出错
- ERROR.7004: Windows 11 WMIC 安装过程中的错误
- ERROR.7005: 在 Windows 11 上卸载 WMIC 时出错
- ERROR.7006: Windows 11 WMIC 卸载过程中的错误

## 贡献

欢迎贡献代码！请提交 Pull Request 或创建 Issue 来报告问题或提出新功能建议。

## 许可证

本项目采用 GPL-3.0 许可证。详细信息请查看 [LICENSE](LICENSE) 文件。

## 作者

**SHICTHRS** - contact@shicthrs.com

## 版权

© 2025-2026 SHICTHRS, Std. All rights reserved.


**注意**: 使用此库需要管理员权限，因为 WMIC 功能的安装和卸载需要对系统进行修改。