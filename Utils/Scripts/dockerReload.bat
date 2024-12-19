@echo off
setlocal

:: Set default environment if not specified
if "%APP_ENV%"=="" set APP_ENV=development

:: Container name based on environment
set CONTAINER_NAME=testapi-%APP_ENV%

:: Set port based on environment
if "%APP_ENV%"=="development" (
    set HOST_PORT=8000
) else if "%APP_ENV%"=="testing" (
    set HOST_PORT=8001
) else if "%APP_ENV%"=="production" (
    set HOST_PORT=8002
)

echo Environment: %APP_ENV%

:: Stop and remove existing container
echo Stopping existing container...
docker stop %CONTAINER_NAME% 2>nul
docker rm %CONTAINER_NAME% 2>nul

:: Build new image
echo Building new image...
docker build -t testapi .
if ERRORLEVEL 1 (
    echo Failed to build image
    exit /b 1
)

:: Run the new container with environment variable
echo Running the new container...
docker run -d -p %HOST_PORT%:8000 -v %cd%\test.db:/app/test.db -e APP_ENV=%APP_ENV% --name %CONTAINER_NAME% testapi
if ERRORLEVEL 1 (
    echo Failed to run the new container
    exit /b 1
)

echo Container is running with %APP_ENV% environment
echo You can check the logs using: docker logs %CONTAINER_NAME%

endlocal