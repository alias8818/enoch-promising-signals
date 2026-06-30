# N-gram Speculative Decoding for Tiny Local Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-tiny-local-models-f427e72f5e6e`
Run ID: `n-gram-speculative-decoding-for-tiny-local-models-f427e72f5e6e-20260604T084415283355+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/addd14148dd3

## What looked useful

Call-count reduction alone is insufficient for tiny local models: 73.5% median target-call reduction on the exact tiny-model matrix produced only 0.936x median wall speedup. Draft length 8 was the only consistently positive exact setting, with 1.390x median speedup. A less-tiny distilgpt2 probe showed larger speedups but uncovered exactness failures, so implementation parity is the key blocker.

## Boundaries and scale limits

Primary exact evidence is limited to sshleifer/tiny-gpt2 on CPU with 27 short cases. A bounded distilgpt2 probe was faster but failed exact greedy parity in 3 of 6 cases. No quantized runtime, GPU serving engine, sampling mode, broad prompt suite, or production batch workload was tested.

## Claim scope

A local Hugging Face cached greedy-decoding benchmark shows that prompt/context n-gram drafting can reduce target forward calls for tiny GPT-2-family models, but wall-clock gains on the exact tiny-model matrix require longer drafts and were not median-positive overall.

## Why it stopped

No-paper useful signal: exact tiny-model results are mixed for wall-clock speed, and the less-tiny confirmation probe exposed exactness failures rather than a robust exact speculative decoder.

## Recommended next action

Stop paper path for this run; run a bounded follow-up that first proves cached batched-verification parity on several real tiny local models before measuring speed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parity-audited n-gram speculative decoding on real tiny local models
- Success threshold: All benchmark cases exactly match vanilla greedy output and draft length 8 achieves at least 1.2x median wall-clock speedup with no more than 10% peak RSS increase.
- Stop condition: Stop if cached batched verification cannot be made token-exact on the first two real tiny models, or if exact runs show median wall speedup below 1.0x despite at least 50% target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-tiny-local-models-f427e72f5e6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
