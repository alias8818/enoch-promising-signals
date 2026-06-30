# Predictive Operator-Update Memory: Learning When Memory Helps

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `predictive-operator-update-memory-learning-when-memory-helps-2e2ee7ba5249`
Run ID: `predictive-operator-update-memory-learning-when-memory-helps-2e2ee7ba5249-20260610T145844451001+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3efcd0e635c

## What looked useful

Predictive gating suppressed memory in anti-predictive regimes and improved NLL by 0.160 mean versus always-memory while reducing harmful memory uses by 0.117, but top-1 accuracy was 0.0106 lower than always-memory.

## Boundaries and scale limits

24-seed CPU-only synthetic proxy with 10,800 events per seed; no transformer-scale training, natural-language data, long-context model, GPU kernel, or publication-grade robustness validation.

## Claim scope

On a controlled synthetic online nonstationary key-value prediction benchmark, a lightweight learned memory gate reduced harmful memory use and improved NLL versus unconditional memory, but did not improve aggregate top-1 accuracy.

## Why it stopped

Proxy-only mixed result: useful mechanism signal for calibrated memory gating, but not a direct/full validation and not paper-ready because unconditional memory retained better aggregate top-1 accuracy.

## Recommended next action

Run a bounded neural sequence-model follow-up that separates read gating from write gating and compares against parameter-matched dense, always-memory, and fixed-threshold controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Read/Write Gating for Nonstationary Memory
- Success threshold: Learned gating must beat always-memory on NLL by at least 0.05 and reduce harmful memory-use rate by at least 25% without losing more than 0.5 percentage points of top-1 accuracy across at least 10 seeds.
- Stop condition: Stop as a negative if learned gating still trails always-memory by more than 0.5 percentage points top-1 accuracy or fails to reduce NLL/harmful-use rate in paired seed comparisons.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-update-memory-learning-when-memory-helps-2e2ee7ba5249`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
