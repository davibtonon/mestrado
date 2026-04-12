@echo off

REM Caminho do executável do llama.cpp
set LLAMA_EXE=D:\davi_tonon\llama.cpp\build\bin\Release\llama-server.exe

REM Caminho do modelo
@REM set MODEL_PATH="D:\davi_tonon\mestrado\models\foundation-sec-8b-reasoning-q4_k_m.gguf"
set MODEL_PATH="D:\davi_tonon\mestrado\models\foundation-sec-1.1-8b-instruct-q4_k_m.gguf"

REM Configurações de hardware
set NGL=35
set THREADS=8
set CONTEXT=4096

REM Rede local
set HOST=127.0.0.1
set PORT=8080

echo =====================================
echo   Iniciando llama.cpp server
echo =====================================
echo.

%LLAMA_EXE% -m %MODEL_PATH% -ngl %NGL% -t %THREADS% -c %CONTEXT%

pause