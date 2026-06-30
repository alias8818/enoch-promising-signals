# CPU 5-gram Speculative Draft for Exact GPU Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `cpu-5-gram-speculative-draft-for-exact-gpu-inference-5b45f085160d`
Run ID: `cpu-5-gram-speculative-draft-for-exact-gpu-inference-5b45f085160d-20260526T032001558586+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acd2798a41c2

## What looked useful

CPU dictionary 5-gram drafting was fast, but target agreement was too low for practical exact greedy speculative speedup: the largest run accepted at least one drafted token in only 20.7% of contexts, averaged 0.266 accepted prefix tokens per 4-token draft, and fully accepted 4-token drafts in 0.1% of contexts.

## Boundaries and scale limits

Tested distilgpt2 only, WikiText-2 only, up to 1M n-gram training tokens and 1,024 validation contexts; not a full exact stochastic speculative decoder, not a production serving benchmark, and not a 7B+ target model.

## Claim scope

Early proxy falsification for a plain corpus-trained CPU 5-gram/backoff draft model evaluated against distilgpt2 greedy next-token outputs on WikiText-2 validation contexts.

## Why it stopped

Proxy early falsification: the tested 5-gram draft mechanism did not agree with the target often enough to justify a full serving validation in this run.

## Recommended next action

Stop this plain corpus 5-gram drafting line unless a future run replaces the proxy with a real exact speculative decoder and demonstrates mean accepted prefix above 1 token plus measured end-to-end speedup.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cpu-5-gram-speculative-draft-for-exact-gpu-inference-5b45f085160d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
