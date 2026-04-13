@echo off

REM =====================================
REM        Configuração do Llama.cpp
REM =====================================

REM Caminho do executável do llama.cpp
set LLAMA_EXE=C:\davi_tonon\llama.cpp\build\bin\Release\llama-server.exe

REM Caminho do modelo
set MODEL_PATH="C:\Users\Tiago Tonon\Documents\Orion\mestrado\models\foundation-sec-1.1-8b-instruct-q4_k_m.gguf"

REM Configurações de hardware (CPU)
set THREADS=8

REM Janela de contexto (máximo suportado pelo modelo: 65536)
REM Ajuste se houver limitação de memória RAM, 4096 16384, 32768, 65536
set CONTEXT=65536

REM Configurações do servidor
set HOST=127.0.0.1
set PORT=8080

echo =====================================
echo        Iniciando llama.cpp server
echo =====================================
echo Modelo: %MODEL_PATH%
echo Threads: %THREADS%
echo Contexto: %CONTEXT% tokens
echo Servidor: http://%HOST%:%PORT%
echo =====================================
echo.

REM Execução sem uso de GPU
%LLAMA_EXE% -m %MODEL_PATH% -t %THREADS% -c %CONTEXT% --host %HOST% --port %PORT%

pause