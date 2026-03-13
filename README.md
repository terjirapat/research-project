ds-project/
│
├── README.md
├── pyproject.toml / requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/            # data ดิบ ห้ามแก้
│   ├── interim/        # data หลัง cleaning
│   ├── processed/      # data สำหรับ train
│   └── external/       # data จาก external source
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_experiment.ipynb
│
├── src/
│   ├── config/
│   │   └── config.py
│   │
│   ├── data/
│   │   ├── load_data.py
│   │   ├── preprocess.py
│   │   └── split.py
│   │
│   ├── features/
│   │   └── feature_engineering.py
│   │
│   ├── models/
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   │
│   ├── visualization/
│   │   └── plot.py
│   │
│   └── utils/
│       ├── logger.py
│       └── helpers.py
│
├── experiments/
│   ├── exp_001_baseline.yaml
│   ├── exp_002_prophet.yaml
│   └── exp_003_xgboost.yaml
│
├── models/
│   ├── trained/
│   └── artifacts/
│
├── reports/
│   ├── figures/
│   └── presentation/
│
└── tests/
    ├── test_data.py
    └── test_features.py