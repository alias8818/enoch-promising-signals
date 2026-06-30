# Small Agent Evidence Verification at Home Scale

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `small-agent-evidence-verification-at-home-scale-cf1addc607ed`
Run ID: `small-agent-evidence-verification-at-home-scale-cf1addc607ed-20260607T125438577982+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/143d4d45374d

## What looked useful

Exact-match and one-token perturbation checks can solve toy citation verification, but they collapse on real scientific claim verification. On SciFact dev with train-selected thresholds, retrieval-only cited-source reached macro-F1 0.366 while the lexical agent reached macro-F1 0.134 and failed supported/refuted detection.

## Boundaries and scale limits

CPU-only local run; no learned NLI model, embedding reranker, open-weight LLM, large corpus, or long-form web evidence was evaluated. Synthetic Wikipedia-summary benchmark was toy-scale and easy; SciFact evaluation covered 450 dev claim/evidence instances over 5,183 abstracts.

## Claim scope

A deterministic home-scale lexical verifier using citation-constrained BM25 retrieval plus entity/number mismatch rules does not outperform a calibrated retrieval-only cited-source baseline on SciFact dev, despite solving an easy synthetic perturbation benchmark.

## Why it stopped

Proxy/early falsification: the tested deterministic lexical small-agent mechanism underperformed the calibrated retrieval-only baseline on real SciFact evidence, so it is not paper-worthy as implemented.

## Recommended next action

Run a bounded follow-up with a small open-weight NLI or instruction model on the same SciFact train/dev harness and require explicit refuted-class improvement over the calibrated retrieval-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Learned Verifier on SciFact at Home Scale
- Success threshold: Dev macro-F1 at least 0.10 absolute above the calibrated retrieval-only baseline and refuted-class F1 at least 0.25 without reducing supported-class F1 below 0.60.
- Stop condition: Stop if the small learned verifier cannot exceed the calibrated retrieval-only macro-F1 by 0.05 absolute on SciFact dev or if runtime/memory exceeds home-scale constraints for the 450-claim dev run.

## Evidence references

- Artifact root: `<local-path>/projects/small-agent-evidence-verification-at-home-scale-cf1addc607ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
