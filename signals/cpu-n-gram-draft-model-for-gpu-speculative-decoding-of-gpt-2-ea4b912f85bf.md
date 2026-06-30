# CPU N-Gram Draft Model for GPU Speculative Decoding of GPT-2

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `cpu-n-gram-draft-model-for-gpu-speculative-decoding-of-gpt-2-ea4b912f85bf`
Run ID: `cpu-n-gram-draft-model-for-gpu-speculative-decoding-of-gpt-2-ea4b912f85bf-20260608T155956421688+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9b056dfa36f3

## What looked useful

The CPU n-gram draft path was exact against greedy decoding but accepted only 4.66% of drafted tokens in the main order-4/k-4 run; ablations reached at most 9.87% mean acceptance. Ideal target-call reduction stayed around 14-18%, too low to justify scale-out or a paper.

## Boundaries and scale limits

Test used GPT-2-small, WikiText-2 slices, 16 main prompts, 48 generated tokens per prompt, and a correctness-first prototype rather than an optimized production KV-cache verifier.

## Claim scope

Bounded GPT-2-small/WikiText-2 test of a plain CPU n-gram draft model for greedy speculative decoding on GB10.

## Why it stopped

Proxy/early falsification: direct small GPT-2 evidence showed exact decoding but very low draft acceptance and no practical speed path for the plain CPU n-gram draft model.

## Recommended next action

Stop this vanilla n-gram draft line unless a bounded follow-up first demonstrates much higher acceptance, for example above 50% at k>=4 on GPT-2-small-class held-out prompts.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-model-for-gpu-speculative-decoding-of-gpt-2-ea4b912f85bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
