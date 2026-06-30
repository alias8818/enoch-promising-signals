# BPE Merge Rule Guided Speculative Decoding without Draft Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `bpe-merge-rule-guided-speculative-decoding-without-draft-model-a64eed4f338c`
Run ID: `bpe-merge-rule-guided-speculative-decoding-without-draft-model-a64eed4f338c-20260526T035031038395+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f8722ba9e610

## What looked useful

BPE merge adjacency alone produced no accepted non-newline proposals in the bounded direct test. A raw distilgpt2 run showed 232 accepted proposals and 33.2% ideal call reduction, but every accepted token was GPT-2 token 198 ('\n'); with newline proposals banned, accepted proposals fell to 0/833 and call reduction to 0.

## Boundaries and scale limits

Small GPT-2-family CPU runs only: 8 tiny-gpt2 prompts x 24 generated tokens, and 16 distilgpt2 prompts x 32 generated tokens. No large LLMs, stochastic decoding, serving kernel timing, or broad benchmark prompt suite were tested.

## Claim scope

Static GPT-2 BPE merge-rule proposals, without a draft model or learned predictor, were tested for exact greedy speculative acceptance on tiny-gpt2 and distilgpt2 over fixed short prompts. The only apparent distilgpt2 speedup came from repeated newline token proposals; banning newline proposals reduced acceptance and ideal call reduction to zero.

## Why it stopped

Proxy-scale but direct acceptance testing falsified the practical mechanism for static BPE merge rules alone: non-newline exact proposal acceptance was zero in the confirmation ablation.

## Recommended next action

Stop this static BPE-merge-only line unless a future variant adds a real predictor or demonstrates non-whitespace acceptance on a larger prompt suite; this run is an early bounded falsification, not a full-scale validation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/bpe-merge-rule-guided-speculative-decoding-without-draft-model-a64eed4f338c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
