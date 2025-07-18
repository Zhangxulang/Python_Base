@echo off
setlocal enabledelayedexpansion

:: 设置远程仓库地址和分支
set GITEE_URL=https://gitee.com/zhang-xulang/python_base.git
set GITHUB_URL=https://github.com/Zhangxulang/Python_Base.git
set BRANCH=master

:: 自动拉取，避免冲突
echo  正在拉取远程仓库 %BRANCH% 分支最新内容...
git pull origin %BRANCH%

:: 自动添加所有更改并提交
set TIME_STR=%date:~0,10%_%time:~0,5%
set TIME_STR=%TIME_STR: =_%
set TIME_STR=%TIME_STR::=-%
echo  自动提交中：%TIME_STR%...
git add .
git commit -m "双推自动提交更新 - %TIME_STR%" >nul 2>nul

:: 配置 origin 双 push（如果尚未设置过）
git remote remove github >nul 2>nul
git remote set-url --add --push origin %GITEE_URL%
git remote set-url --add --push origin %GITHUB_URL%

:: 显示当前远程信息
echo.
echo  当前远程仓库配置：
git remote -v

:: 推送
echo.
echo  正在推送到 Gitee 和 GitHub...
git push origin %BRANCH%

:: 自动打开网页查看
start https://gitee.com/zhang-xulang/python_base
start https://github.com/Zhangxulang/Python_Base

echo.
echo 所有操作完成！
pause