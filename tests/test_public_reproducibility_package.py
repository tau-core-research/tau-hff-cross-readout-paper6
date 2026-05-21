import csv
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "paper6_submission_source"
DATA = ROOT / "data/derived"


def read_single_row_csv(path: Path) -> dict[str, str]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1
    return rows[0]


def test_publication_files_exist():
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CITATION.cff",
        ROOT / "requirements.txt",
        SOURCE / "main.tex",
        SOURCE / "refs.bib",
        SOURCE / "main.pdf",
        SOURCE / "figures",
        ROOT / "figures",
        ROOT / "scripts/build_arxiv_source.py",
        ROOT / "scripts/reproduce.py",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    assert missing == []


def test_paper_source_is_observationally_scoped():
    source = (SOURCE / "main.tex").read_text(encoding="utf-8")
    assert "cross-readout enrichment" in source
    assert "dark-matter replacement proof" in source
    assert "paper's central claim" in source
    assert "Tau Core is proven" not in source
    assert "\\includegraphics" in source
    assert "\\bibliography{refs}" in source


def test_derived_claim_numbers_match_paper6_summary():
    hff = read_single_row_csv(DATA / "tau_hff_all_six_hierarchical_fit_summary_v2.csv")
    clash = read_single_row_csv(DATA / "tau_hff_external_clash_hierarchical_fit_summary_v1.csv")
    assert int(hff["row_count"]) == 92
    assert int(hff["cluster_count"]) == 6
    assert round(float(hff["population_ratio"]), 3) == 1.630
    assert int(clash["row_count"]) == 96
    assert int(clash["cluster_count"]) == 12
    assert round(float(clash["population_ratio"]), 3) == 1.231
    assert round(float(clash["population_ratio_ci95_low"]), 3) == 1.119
    assert round(float(clash["population_ratio_ci95_high"]), 3) == 1.353
    assert clash["frozen_external_pass"] == "True"


def test_external_clash_cluster_summary():
    path = DATA / "tau_hff_external_clash_cluster_summary_v1.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 12
    assert min(float(row["median_residual_null_ratio"]) for row in rows) > 1.0
    assert max(float(row["median_residual_null_ratio"]) for row in rows) > 1.3


def test_arxiv_source_package_exists_and_is_source_only():
    archive_path = ROOT / "arxiv_submission_source.zip"
    assert archive_path.exists()
    with zipfile.ZipFile(archive_path) as archive:
        names = set(archive.namelist())
    assert "main.tex" in names
    assert "refs.bib" in names
    assert "main.pdf" not in names
    assert "figures/external_clash_cluster_validation_summary_v1.png" in names
    assert not any(name.endswith((".aux", ".log", ".out", ".toc", ".blg", ".bbl")) for name in names)
