@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: 设置远程地址
set GITEE_URL=https://gitee.com/zhang-xulang/python_base.git
set GITHUB_URL=https://github.com/Zhangxulang/Python_Base.git
set BRANCH=master

:: 清理旧的 remote
git remote remove origin >nul 2>nul
git remote remove github >nul 2>nul

:: 添加远程仓库
git remote add origin %GITEE_URL%
git remote add github %GITHUB_URL%

:: 添加 origin 的双 push（可选）
git remote set-url --add --push origin %GITEE_URL%
git remote set-url --add --push origin %GITHUB_URL%

:: 查看远程信息
echo.
echo 远程仓库配置如下：
git remote -v

:: 推送前检查是否有提交
echo.
echo  正在添加与提交更改...
git add .
git commit -m "双推自动提交更新" || echo 无需提交（已是最新）

:: 开始推送
echo.
echo  推送到 Gitee (origin)...
git push origin %BRANCH%

echo  推送到 GitHub (github)...
git push github %BRANCH%

echo.
echo  推送完成！
pause