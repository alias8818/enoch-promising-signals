# Curriculum Ordering Sensitivity at 50M Tokens

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `curriculum-ordering-sensitivity-at-50m-tokens-f1a5b4ca4230`
Run ID: `curriculum-ordering-sensitivity-at-50m-tokens-f1a5b4ca4230-20260629T011758490403+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f57fe012b74

## What looked useful

Three replicated local GPU runs show strong recency-driven forgetting under contiguous curricula and much lower mixture loss under interleaving at an approximately 50M-token budget.

## Boundaries and scale limits

Synthetic domains only; tiny model; held-out cross-entropy only; equal expected domain distributions rather than exact identical token multisets; 49,987,584 tokens per schedule due integer-step rounding; no real corpus or GPT-2-small-class validation.

## Claim scope

In a controlled synthetic three-domain causal-LM setup with a 478,720-parameter Transformer, equal domain step counts, three seeds, and 49,987,584 training tokens per schedule, curriculum ordering materially changed final held-out loss; batch-level interleaving outperformed contiguous domain curricula by at least 4.41 mean held-out loss points.

## Why it stopped

No-paper useful signal: synthetic local evidence supports the mechanism, but real-corpus direct evidence is required to make the 50M-token curriculum-ordering claim publication-grade.

## Recommended next action

Run a bounded real-corpus 50M-token replication with exact token-multiset matching across schedules before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-multiset real-corpus curriculum ordering at 50M tokens
- Success threshold: Interleaved schedule beats the best contiguous schedule by at least 0.10 mean held-out loss points and reduces worst-domain forgetting in at least 2 of 3 seeds.
- Stop condition: Stop if exact-multiset schedule construction is not possible locally, if calibration projects beyond the allowed worker budget, or if the first two seeds show less than 0.05 mean-loss separation.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-sensitivity-at-50m-tokens-f1a5b4ca4230`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
