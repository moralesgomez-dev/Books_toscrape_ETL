# books-toscrape-etl

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-orange)
![ETL](https://img.shields.io/badge/Pipeline-ETL-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Pipeline ETL que extrae información de libros de [books.toscrape.com](https://books.toscrape.com), la transforma y la carga en una base de datos PostgreSQL.

---

## Objetivo del proyecto

Practicar el desarrollo de un pipeline ETL completo usando Python, automatizando:

- **Extract** → Scraping de todas las páginas de books.toscrape.com
- **Transform** → Limpieza y normalización de precios, disponibilidad y ratings
- **Load** → Inserción de los datos en PostgreSQL

---

## Instalación

### Requisitos previos

- Python 3.8+
- PostgreSQL en local o remoto
- pip

### Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/moralesgomez-dev/books-toscrape-etl.git
cd books-toscrape-etl

# 2. Crea un entorno virtual
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.\.venv\Scripts\activate       # Windows

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Configura las variables de entorno
cp .env.example .env
# Edita .env con tus credenciales de PostgreSQL
```

---

## Configuración

Crea un archivo `.env` en la raíz del proyecto con tus datos:

```env
DB_NAME=books_db
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

> ⚠️ El archivo `.env` está en `.gitignore` — nunca lo subas a GitHub.

---

## Uso

```bash
python src/main.py
```

La ejecución hace lo siguiente:
1. Scraping de todas las páginas de books.toscrape.com (~1000 libros)
2. Limpieza y transformación de los datos
3. Conexión a la base de datos
4. Creación de la tabla `books` si no existe
5. Inserción de todos los registros

**Salida esperada:**
```
Scraping...
Extraídos: 1000
Transformando...
Conectando a DB...
Insertando...
Proceso terminado.
```

---

## Estructura de la base de datos

Tabla `books`:

| Columna | Tipo | Descripción |
|---|---|---|
| `id` | SERIAL PRIMARY KEY | ID autoincremental |
| `title` | TEXT UNIQUE | Título del libro |
| `price` | NUMERIC | Precio en libras (£) |
| `availability` | BOOLEAN | True si está en stock |
| `rating` | INTEGER | Valoración del 1 al 5 |
| `loaded_at` | TIMESTAMP | Fecha de inserción |

---

## Estructura del proyecto

```
books-toscrape-etl/
│
├── src/
│   ├── main.py          # Orquestador del pipeline ETL
│   ├── scraper.py       # Extracción de datos (requests + BeautifulSoup)
│   ├── transform.py     # Limpieza y transformación
│   └── db.py            # Conexión y operaciones con PostgreSQL
│
├── .env.example         # Plantilla de variables de entorno
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Contribución

1. Haz un fork del proyecto
2. Crea tu rama (`git checkout -b feature/mejora`)
3. Haz commit de tus cambios (`git commit -am 'Añade mejora'`)
4. Haz push (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## Autor

**AlejandroMoralesGomezDev**
- GitHub: [moralesgomez-dev](https://github.com/moralesgomez-dev)
- Kaggle: [moralesgomez](https://www.kaggle.com/moralesgomez)

---

## 📄 Licencia

MIT License - consulta el archivo [LICENSE](LICENSE) para más detalles.