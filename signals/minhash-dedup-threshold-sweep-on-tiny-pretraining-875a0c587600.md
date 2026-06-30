# MinHash dedup threshold sweep on tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-dedup-threshold-sweep-on-tiny-pretraining-875a0c587600`
Run ID: `minhash-dedup-threshold-sweep-on-tiny-pretraining-875a0c587600-20260610T093741771194+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/75d3b4893976

## What looked useful

Across three seeds, leaked-clean NLL improved from -2.90 without dedup to -2.10 at threshold 0.50 and -1.75 at threshold 0.20, while all thresholds retained 50/50 leaked families with at least one train variant. Clean validation NLL stayed nearly flat through ordinary thresholds and only slightly worsened under aggressive thresholds.

## Boundaries and scale limits

Synthetic topical documents, add-alpha word trigram language model, three corpus seeds, CPU-only run under one minute total for main and extension sweeps; not neural pretraining and not real web-corpus evidence.

## Claim scope

In a controlled synthetic tiny language-model proxy, lowering train-train MinHash dedup thresholds reduces near-duplicate leakage strength but does not remove leaked families because greedy dedup keeps one representative per duplicate cluster.

## Why it stopped

No-paper closure: this is useful synthetic/count-LM evidence, but it is not direct neural or real-corpus validation.

## Recommended next action

Run a bounded real-corpus deepen test with known near-duplicate clusters, a tiny neural LM, and a source-aware or eval-aware dedup control that can remove whole leaked families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny neural LM dedup threshold sweep with family-level controls
- Success threshold: The follow-up is successful if train-only thresholds reduce leaked-probe advantage by at least 25% without large clean-loss regression, while family-level/source-aware removal eliminates at least 95% of leaked-family coverage and further reduces leaked-probe advantage.
- Stop condition: Stop if real-corpus duplicate clusters cannot be audited, if the tiny neural run cannot finish within the local budget, or if train-only and family-aware dedup produce indistinguishable leaked-probe and clean-loss curves across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-sweep-on-tiny-pretraining-875a0c587600`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
