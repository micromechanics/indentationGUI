@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -m sphinx
)
if "%PYTHON%" == "" (
	set PYTHON=python
)
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help
if /I "%1" == "screenshots" goto screenshots

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
echo.The Sphinx build command was not found. Make sure Python and Sphinx
echo.are installed, then set the SPHINXBUILD environment variable if needed.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:screenshots
%PYTHON% scripts\generate_analysis_tab_screenshots.py
if errorlevel 1 exit /b 1

:end
popd
