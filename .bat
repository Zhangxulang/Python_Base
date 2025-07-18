@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: ����Զ�ֿ̲��ַ�ͷ�֧
set GITEE_URL=https://gitee.com/zhang-xulang/python_base.git
set GITHUB_URL=https://github.com/Zhangxulang/Python_Base.git
set BRANCH=master

:: �Զ���ȡ�������ͻ
echo  ������ȡԶ�ֿ̲� %BRANCH% ��֧��������...
git pull origin %BRANCH%

:: �Զ�������и��Ĳ��ύ
set TIME_STR=%date:~0,10%_%time:~0,5%
set TIME_STR=%TIME_STR: =_%
set TIME_STR=%TIME_STR::=-%
echo  �Զ��ύ�У�%TIME_STR%...
git add .
git commit -m "˫���Զ��ύ���� - %TIME_STR%" >nul 2>nul

:: ���� origin ˫ push�������δ���ù���
git remote remove github >nul 2>nul
git remote set-url --add --push origin %GITEE_URL%
git remote set-url --add --push origin %GITHUB_URL%

:: ��ʾ��ǰԶ����Ϣ
echo.
echo  ��ǰԶ�ֿ̲����ã�
git remote -v

:: ����
echo.
echo  �������͵� Gitee �� GitHub...
git push origin %BRANCH%

:: �Զ�����ҳ�鿴
start https://gitee.com/zhang-xulang/python_base
start https://github.com/Zhangxulang/Python_Base

echo.
echo ���в�����ɣ�
pause