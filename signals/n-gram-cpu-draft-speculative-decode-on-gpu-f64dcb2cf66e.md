# N-gram CPU draft speculative decode on GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-draft-speculative-decode-on-gpu-f64dcb2cf66e`
Run ID: `n-gram-cpu-draft-speculative-decode-on-gpu-f64dcb2cf66e-20260601T023421866418+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4c0f43dccae5

## What looked useful

CPU n-gram drafting is cheap and exact under verifier correction, but acceptance was sparse: best mean accepted length was 0.190 tokens per verifier and full two-token acceptance was 0.61%; context-specific 3-gram/4-gram keys reduced calls by only 1.6% to 4.7%.

## Boundaries and scale limits

Small model, small prompt set, full-context verifier rather than production KV-cache decoding, WikiText-2 general text only, no learned draft-model baseline, no 7B+ serving workload.

## Claim scope

On distilgpt2 with WikiText-2 prompts and a 50k-token CPU n-gram table, exact greedy GPU speculative verification preserves output and can reduce target calls by up to 15.1% for bigram drafting, but 3-gram and 4-gram drafting accept too rarely to be compelling.

## Why it stopped

Bounded local evidence shows exactness and a small call reduction, but acceptance is too sparse and the implementation too proxy-like for a paper-ready positive claim.

## Recommended next action

Stop this run as a no-paper useful signal; only deepen with a KV-cache verifier on repetition-heavy prompts and compare against a learned draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram speculative decoding on repetition-heavy prompts
- Success threshold: At least 25% end-to-end latency reduction versus greedy decoding and no worse than 90% of the learned-draft baseline speedup, with exact greedy equivalence on all prompts.
- Stop condition: Stop if mean accepted length remains below 0.5 tokens per verifier or end-to-end speedup remains below 10% after KV-cache implementation on repetition-heavy prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-draft-speculative-decode-on-gpu-f64dcb2cf66e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
