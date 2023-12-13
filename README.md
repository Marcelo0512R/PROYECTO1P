# Web Scraping Scripts

Este repositorio contiene scripts de Python para extraer datos web de tres URL diferentes. Cada script está diseñado para extraer información específica de las respectivas páginas web.

## 1. Lista Estudiantes Web Scraping

### Descripción
Este script extrae datos de la página web "http://127.0.0.1:8000/lista_estudiantes/". Extrae información sobre los estudiantes, incluidos sus nombres, edades y calificaciones. El script utiliza Selenium y BeautifulSoup para el web scraping.

### Uso
1. Instale las bibliotecas necesarias: `pip install pandas selenium beautifulsoup4`
2. Asegúrese de tener el ejecutable de ChromeDriver en la ruta de su sistema.
3. Ejecute el script: `python lista_estudiantes_scraping.py`
4. Los datos se guardarán en un archivo CSV llamado `datosEstudiantes.csv`.

## 2. Lista Cursos Web Scraping

### Descripción
Este script extrae datos de la página web "http://127.0.0.1:8000/lista_cursos/". Recopila información sobre cursos, incluidos los nombres de los cursos, créditos y profesores. Selenium y BeautifulSoup se utilizan para el web scraping.

### Uso
1. Instale las bibliotecas necesarias: `pip install pandas selenium beautifulsoup4`
2. Asegúrese de tener el ejecutable de ChromeDriver en la ruta de su sistema.
3. Ejecute el script: `python lista_cursos_scraping.py`
4. Los datos se guardarán en un archivo CSV llamado `datosCursos.csv`.

## 3. Lista Calificaciones Web Scraping

### Descripción
Este script extrae datos de la página web "http://127.0.0.1:8000/lista_calificaciones/". Extrae información sobre las calificaciones de los estudiantes, incluidos los nombres de los estudiantes y sus respectivas calificaciones. Selenium y BeautifulSoup se emplean para el web scraping.

### Uso
1. Instale las bibliotecas necesarias: `pip install pandas selenium beautifulsoup4`
2. Asegúrese de tener el ejecutable de ChromeDriver en la ruta de su sistema.
3. Ejecute el script: `python lista_calificaciones_scraping.py`
4. Los datos se guardarán en un archivo CSV llamado `datosCalificaciones.csv`.

No dude en modificar los scripts según la estructura específica de las páginas web que esté extrayendo.
