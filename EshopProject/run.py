from app import create_app, create_tables_and_seed

app = create_app()

create_tables_and_seed(app) # Manually create tables & seed before the first request ever comes in:

if __name__ == '__main__':
    app.run(debug=True)