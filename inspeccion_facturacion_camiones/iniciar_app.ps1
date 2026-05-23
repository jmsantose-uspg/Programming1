$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonExe = Join-Path $env:LOCALAPPDATA "Programs\Python\Python314\python.exe"
$dbPassword = $env:IMPALA_DB_PASSWORD

if (-not $pythonExe) {
    Write-Host "No se encontro una instalacion de Python." -ForegroundColor Red
    Write-Host "Instala Python o ejecuta esta app desde Codex." -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path $pythonExe)) {
    Write-Host "La ruta configurada de Python no existe:" -ForegroundColor Red
    Write-Host "  $pythonExe" -ForegroundColor Yellow
    exit 1
}

if (-not $dbPassword) {
    Write-Host "No se encontro la variable IMPALA_DB_PASSWORD." -ForegroundColor Red
    Write-Host "Configura la contrasena de MariaDB antes de iniciar la app." -ForegroundColor Yellow
    exit 1
}

Set-Location $projectRoot
Write-Host "Iniciando Inspeccion de camiones en http://127.0.0.1:5000" -ForegroundColor Cyan
$env:IMPALA_DB_HOST = "localhost"
$env:IMPALA_DB_USER = "impala_app"
$env:IMPALA_DB_PASSWORD = $dbPassword
$env:IMPALA_DB_NAME = "inspeccion_camiones"
$env:IMPALA_DB_PORT = "3306"

$listener = Get-NetTCPConnection -LocalPort 5000 -State Listen -ErrorAction SilentlyContinue
if ($listener) {
    Write-Host "La app ya esta ejecutandose en el puerto 5000." -ForegroundColor Yellow
    exit 0
}

& $pythonExe "serve_app.py"
