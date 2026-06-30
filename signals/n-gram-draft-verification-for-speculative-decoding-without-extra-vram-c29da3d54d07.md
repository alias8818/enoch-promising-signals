# N-gram Draft Verification for Speculative Decoding Without Extra VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-draft-verification-for-speculative-decoding-without-extra-vram-c29da3d54d07`
Run ID: `n-gram-draft-verification-for-speculative-decoding-without-extra-vram-c29da3d54d07-20260611T133733900797+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a96dbb23f832

## What looked useful

DistilGPT-2 reduced verifier passes from 1024 to 542 (47.1%) with a 21.8 KiB estimated draft table; GPT-2 reduced passes from 1024 to 426 (58.4%) with a 21.5 KiB table. GPT-2 shuffled-continuation control fell to 1.9% pass reduction, supporting dependence on real local n-gram structure.

## Boundaries and scale limits

Tested only distilgpt2 and gpt2 on 8 prompts with 128 generated tokens each; measured verifier-pass counts and CUDA generation calibration, not production KV-cache wall-clock latency, batching behavior, larger chat models, or long-context serving.

## Claim scope

Small GPT-family greedy trace replay shows that CPU n-gram prompt/output lookup can reduce exact greedy verifier passes without adding draft-model VRAM.

## Why it stopped

No-paper useful signal: trace replay supports the mechanism but does not directly validate production latency or larger-model behavior.

## Recommended next action

Run a bounded deepen follow-up that implements exact greedy n-gram speculative decoding with KV-cache verification and measures wall-clock latency against greedy decoding on a 100-prompt corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache latency benchmark for n-gram speculative verification
- Success threshold: At least 15% median wall-clock latency reduction or tokens/s improvement on 100 prompts with exact greedy output equality and less than 1% additional GPU memory.
- Stop condition: Stop as unsupported if speedup is below 5%, exactness fails, or CPU lookup/verification overhead erases pass-count gains.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-verification-for-speculative-decoding-without-extra-vram-c29da3d54d07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
