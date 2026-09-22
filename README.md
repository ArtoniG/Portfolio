# Portfolio
Created to store data science codes

credit-risk-modelling-process/
│
├── terraform/                  # INFRASTRUCTURE & SECURITY
│   ├── secrets.tf              # GCP Secret Manager integration
│   ├── bq_policy_tags.tf       # Column-level PII data access policies
│   └── environments/
│
├── ingestion/                  # INGESTION & PERIMETER SECURITY
│   ├── anonymizer.py           # HMAC-SHA256 PII tokenization
│   └── payload_validator.py    # Strict schema validation before warehouse load
│
├── dbt_project/                # FEATURE STORE & TRANSFORMATIONS
│   └── models/                 # Mandatory partitioning & clustering configs
│
├── toolbox/                    # STABLE CORE UTILITIES (Zero-Dependency)
│   ├── metrics/                # Standard Gini, KS, IV, PSI calculations
│   └── viz/                    # Executive-ready plotting templates
│
├── ml_pipeline/                # TRAINING & STABILITY MONITORING
│   ├── train.py
│   └── drift_monitor.py        # Automated Population Stability Index (PSI) tracking
│
├── xai_and_docs/               # GOVERNANCE & AUDITABILITY
│   ├── audit_logger.py         # Immutable point-in-time decision snapshots
│   ├── explainability.py       # SHAP to Reason Codes mapping
│   └── generate_model_card.py  # Automated regulatory PDF/Markdown generator
│
├── serving/                    # DEPLOYMENT & CIRCUIT BREAKERS
│   ├── app.py                  # FastAPI server
│   ├── circuit_breaker.py      # Fallback logic for LLM API downtime
│   └── guardrails/             # Deterministic Pydantic / Instructor validation
