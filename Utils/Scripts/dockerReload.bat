@echo off
setlocal

:: Define the container name
set CONTAINER_NAME=testapi-container

:: Check if the container exists and stop/remove it
for /f "tokens=*" %%i in ('docker ps -aq -f "name=%CONTAINER_NAME%"') do (
    echo Stopping and removing old container: %CONTAINER_NAME%
    docker stop %%i
    if ERRORLEVEL 1 (
        echo Failed to stop container %%i
        exit /b 1
    )
    docker rm %%i
    if ERRORLEVEL 1 (
        echo Failed to remove container %%i
        exit /b 1
    )
)

:: Build the Docker image
echo Building the Docker image...
docker build -t testapi .
if ERRORLEVEL 1 (
    echo Docker build failed
    exit /b 1
)

:: Run the new container
echo Running the new container...
docker run -p 8001:8000 -v %cd%\test.db:/app/test.db --name %CONTAINER_NAME% testapi
if ERRORLEVEL 1 (
    echo Failed to run the new container
    exit /b 1
)

endlocal