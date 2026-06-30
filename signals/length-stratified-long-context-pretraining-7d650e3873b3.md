# Length-Stratified Long Context Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `length-stratified-long-context-pretraining-7d650e3873b3`
Run ID: `length-stratified-long-context-pretraining-7d650e3873b3-20260525T174111937355+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9dc65dc46b70

## What looked useful

Length-stratified curriculum reached 0.9063 mean long-bin accuracy versus 0.0426 for fixed-long and 0.0628 for uniform-mixed controls, suggesting curriculum length order can be an optimization scaffold for long-context retrieval behavior in this toy setting.

## Boundaries and scale limits

Synthetic single-position recall only; no natural-text pretraining, no GPT-2-small-class baseline, no equal-token-budget ablation, no long-document benchmark, no large-model or datacenter-scale validation.

## Claim scope

On a synthetic causal key-value recall proxy with a 2-layer d_model=96 transformer and 67-token maximum context, short-to-long length-stratified training solved long-bin recall substantially better than fixed-long-only and uniformly mixed-length controls across three seeds.

## Why it stopped

Closed as no-paper useful signal: the result is a synthetic proxy confirmation, not full validation of length-stratified long-context pretraining.

## Recommended next action

Run a bounded deepen follow-up using a small real-text language-model pretraining setup with length buckets, equal-token-budget controls, and held-out long-context evaluations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text equal-token length-stratified pretraining probe
- Success threshold: Length-stratified training must improve long-bin held-out perplexity or retrieval accuracy by at least 5 percent relative over both controls without degrading short-bin perplexity by more than 2 percent.
- Stop condition: Stop if equal-token real-text runs show no long-bin improvement over uniform-mixed controls in at least two seeds or if gains disappear after curriculum-order ablation.

## Evidence references

- Artifact root: `<local-path>/projects/length-stratified-long-context-pretraining-7d650e3873b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
