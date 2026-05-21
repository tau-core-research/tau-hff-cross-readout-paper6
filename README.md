# Paper 6: HFF/CLASH Cross-Readout Enrichment Audit

This repository is the public reproducibility package for:

**A Controlled Lensing/X-ray Cross-Readout Enrichment Audit in HFF and CLASH Clusters**

The package is intentionally small. It contains only the files needed to
rebuild the paper source package, verify the publication-facing derived tables,
and compile the manuscript from the included LaTeX source and figures.

## Theory Context

This paper is an observational phenomenology paper. It does not require
accepting Tau Core, HDDA-DTL, or any new-gravity interpretation. Projection- or
Tau-Core-like frameworks may use the result later as an empirical constraint,
but they are not part of the central claim of this repository.

## Main Claim

The paper tests whether controlled Chandra X-ray structure is enriched inside
high lensing-readout regions above matched nulls.

The publication-facing result is deliberately narrow:

```text
HFF and external CLASH cluster data support a model-sensitive lensing/X-ray
cross-readout enrichment statistic under declared controls.
```

It does not claim:

```text
Tau Core is proven;
dark matter is disproven;
all lensing observables agree;
the candidate maps are final physical fields;
a new gravitational mechanism is derived.
```

## Main Files

```text
LICENSE
CITATION.cff
requirements.txt
README.md
paper6_submission_source/main.tex
paper6_submission_source/refs.bib
paper6_submission_source/main.pdf
paper6_submission_source/figures/
figures/
data/derived/
scripts/build_arxiv_source.py
scripts/reproduce.py
tests/
```

## Included Data

The repository includes derived CSV artifacts needed for claim checks:

```text
data/derived/tau_hff_cluster_level_meta_summary_v1.csv
data/derived/tau_hff_all_six_channel_falsifiers_v1.csv
data/derived/tau_hff_all_six_model_channel_sensitivity_v1.csv
data/derived/tau_hff_all_six_hierarchical_fit_summary_v2.csv
data/derived/tau_hff_external_clash_blind_prefilter_runner_v1.csv
data/derived/tau_hff_external_clash_cluster_summary_v1.csv
data/derived/tau_hff_external_clash_hierarchical_fit_summary_v1.csv
```

Raw HFF, CLASH, and Chandra data products are not redistributed here. This is a
paper-level public reproducibility package, not the full private research
workbench.

## Reproduce

Create an environment with Python 3.10 or newer, then install the lightweight
test dependency:

```bash
python -m pip install -r requirements.txt
```

Run the paper6 reproduction check:

```bash
python scripts/reproduce.py
```

This compiles `paper6_submission_source/main.tex` with `tectonic`, builds the
arXiv source ZIP, and runs the public package tests.

## arXiv Source Package

Build the arXiv source package directly with:

```bash
python scripts/build_arxiv_source.py
```

This writes:

```text
arxiv_submission_source.zip
```

The ZIP is built from `paper6_submission_source/` and excludes the compiled PDF
and temporary LaTeX build files, matching the Paper 1 packaging pattern.

## Scope

This repository is a reproducibility package for Paper 6 only. It excludes
private development notes, raw data downloads, intermediate FITS products, CIAO
working directories, and broader Tau Core theory material that is not required
to verify the paper package.
