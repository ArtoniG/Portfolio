import argparse
import json
import shutil
import os
from pathlib import Path

PROFILES_DIR = Path("profiles")
ROOT_DIR = Path(__file__).parent

def initialize_project(profile_name: str, client_name: str):
    profile_path = PROFILES_DIR / f"{profile_name}.json"
    
    if not profile_path.exists():
        raise FileNotFoundError(f"Profile '{profile_name}' not found in profiles/")

    with open(profile_path, "r") as f:
        config = json.load(f)

    keep_dirs = set(config.get("keep_directories", []))
    all_target_dirs = {
        "terraform", "ingestion", "dbt_project", 
        "notebooks", "ml_pipeline", "xai_and_docs", "serving"
    }

    remove_dirs = all_target_dirs - keep_dirs

    # Prune unnecessary modules
    for dir_name in remove_dirs:
        target_path = ROOT_DIR / dir_name
        if target_path.exists():
            shutil.rmtree(target_path)
            print(f"[-] Pruned unused module: {dir_name}")

    # Remove profile configs from generated project
    if PROFILES_DIR.exists():
        shutil.rmtree(PROFILES_DIR)
        os.remove(ROOT_DIR / "init_project.py")

    print(f"\n[✓] Project successfully initialized for '{client_name}' using profile '{profile_name}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a tailored client repository.")
    parser.add_argument("--profile", required=True, choices=["eda_audit", "clustering", "ml_scoring", "full_engine"])
    parser.add_argument("--client", required=True, help="Client identifier name")
    
    args = parser.parse_args()
    initialize_project(args.profile, args.client)