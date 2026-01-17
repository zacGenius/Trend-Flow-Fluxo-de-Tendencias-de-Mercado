project-name/
│
├── data/
│   ├── raw/              # dados brutos (API, CSV, JSON)
│   ├── bronze/           # dados ingestão
│   ├── silver/           # dados tratados
│   └── gold/             # dados analíticos
│
├── pipelines/
│   ├── ingestion/        # scripts de ingestão
│   ├── transformation/  # PySpark / dbt
│   └── orchestration/   # DAGs Airflow
│
├── analytics/
│   ├── dbt/              # models, tests, sources
│   └── sql/              # queries analíticas
│
├── app/
│   └── streamlit_app.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── tests/
│   ├── test_ingestion.py
│   └── test_transformations.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── README.md
├── requirements.txt
└── .env.example
