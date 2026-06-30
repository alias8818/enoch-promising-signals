# N-Gram Suffix Draft for CPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-draft-for-cpu-speculative-decoding-6b4f17df4a28`
Run ID: `n-gram-suffix-draft-for-cpu-speculative-decoding-6b4f17df4a28-20260529T221853753424+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9cb0c1dbbdea

## What looked useful

Best recent-suffix setting n=2,k=12 achieved 11.16x mean ideal target-call reduction on copy-heavy prompts and 1.84x mean on sampled natural prompts, but sampled-natural token acceptance was only 0.23 and full-accept rate 0.10.

## Boundaries and scale limits

No end-to-end CPU speculative decoding latency was measured; model was distilgpt2 only; data was Tiny Shakespeare only; sampled-natural evidence used 12 prompts of 96 generated tokens per condition; larger models, chat/code tasks, KV-cache behavior, and exact speculative sampling semantics remain unvalidated.

## Claim scope

Offline verifier on distilgpt2 continuations from Tiny Shakespeare prompts: n-gram suffix drafting reduces ideal target verification calls strongly in copy-heavy/repetitive contexts and modestly on sampled natural prompts.

## Why it stopped

Closed as no-paper useful signal because evidence is an offline target-call simulation, not direct serving latency or broad model/task validation.

## Recommended next action

Implement the same suffix drafter inside a real CPU speculative decoding loop and measure end-to-end tokens/sec against no-draft and neural-draft baselines on sampled natural, copy-heavy, chat, and code prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End CPU Latency Test for N-Gram Suffix Drafting
- Success threshold: At least 1.15x median end-to-end tokens/sec improvement over no-draft on copy-heavy prompts without more than 5% regression on sampled natural prompts, with acceptance and call-count logs explaining the result.
- Stop condition: Stop if n-gram suffix drafting fails to improve median end-to-end tokens/sec by 1.05x on copy-heavy prompts or causes more than 10% median slowdown on sampled natural prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-for-cpu-speculative-decoding-6b4f17df4a28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
