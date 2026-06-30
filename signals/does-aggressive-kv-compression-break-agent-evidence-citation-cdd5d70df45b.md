# Does Aggressive KV Compression Break Agent Evidence Citation?

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `does-aggressive-kv-compression-break-agent-evidence-citation-cdd5d70df45b`
Run ID: `does-aggressive-kv-compression-break-agent-evidence-citation-cdd5d70df45b-20260629T115600921927+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/44e2a0250434

## What looked useful

Citation fidelity fell from 62.5% under full cache to 8.3-18.1% under recency-biased compression and 2.8-12.5% under uniform compression. Recency examples with zero retained target tokens had 0% citation accuracy, while oracle retention of the full target evidence span at a 6.25% budget reached 80.6% citation accuracy.

## Boundaries and scale limits

Synthetic evidence lines only; one 0.5B instruct model; likelihood-ranked candidates rather than free-form agent generation; simple cache-slicing policies rather than published production KV-compression implementations; 72 examples with contexts around 2.2k tokens.

## Claim scope

On a synthetic single-model citation task using Qwen2.5-0.5B-Instruct, direct DynamicCache slicing with blind aggressive retention sharply reduced top-1 evidence-citation accuracy versus full cache, while an equal-budget oracle policy that retained the full target evidence span preserved citation accuracy much better.

## Why it stopped

Closed as no-paper useful signal because the evidence is direct at the KV-cache level but synthetic, single-model, and not a validation of real agent traces or published compressors.

## Recommended next action

Run a bounded direct follow-up on real citation/evidence datasets or agent traces with at least one published KV-compression method, preserving citation-specific metrics and full-cache plus evidence-aware controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Evidence-Citation Benchmark for Aggressive KV Compression
- Success threshold: At least 100 real or benchmark examples showing a reproducible citation-accuracy drop of 15 percentage points or more under aggressive blind compression versus full cache, plus recovery of at least half the lost citation accuracy with evidence-aware retention at a comparable cache budget.
- Stop condition: Stop if full-cache citation accuracy is below 50% on the selected model/dataset or if blind compression does not reduce citation accuracy by at least 10 percentage points across two reasonable cache budgets.

## Evidence references

- Artifact root: `<local-path>/projects/does-aggressive-kv-compression-break-agent-evidence-citation-cdd5d70df45b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
