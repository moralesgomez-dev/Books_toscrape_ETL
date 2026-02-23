from scraper import scrape_books
from transform import clean_books
from db import get_connection, create_table, insert_books

def main():
    print("Scraping...")
    raw_books = scrape_books()
    print(f"Extraídos: {len(raw_books)}")

    print("Transformando...")
    clean = clean_books(raw_books)

    print("Conectando a DB...")
    conn = get_connection()
    create_table(conn)

    print("Insertando...")
    insert_books(conn, clean)
    conn.close()

    print("Proceso terminado.")

if __name__ == "__main__":
    main()