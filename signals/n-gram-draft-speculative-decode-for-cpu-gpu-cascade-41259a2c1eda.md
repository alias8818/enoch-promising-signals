# N-gram draft speculative decode for CPU-GPU cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decode-for-cpu-gpu-cascade-41259a2c1eda`
Run ID: `n-gram-draft-speculative-decode-for-cpu-gpu-cascade-41259a2c1eda-20260608T143605320655+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5936459271af

## What looked useful

N-gram prompt lookup is cheap enough on CPU and can produce nontrivial accepted tokens in repeated local-context regimes, but the measured effect is context-sensitive and current evidence is insufficient for a CPU-GPU cascade paper.

## Boundaries and scale limits

No 7B+ model, no production serving stack, no custom exact verifier, no multi-request batching, and no full CPU-GPU overlap/KV-cache latency study. Direct GPT-2/Transformers prompt-lookup smoke was small and exposed output contract concerns.

## Claim scope

Bounded local mechanism probe: on GPT-2-tokenized repeated-context text traces, a CPU prompt-lookup 2-gram drafter accepted 15-28% of next tokens and improved ideal target verifier-call efficiency to about 1.18-1.39 tokens per verifier call, with Python CPU proposal throughput around 0.75-0.84M verifier steps/s.

## Why it stopped

Bounded trace and small GPU smoke evidence supports the mechanism but not a correctness-controlled, publication-grade CPU-GPU cascade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a custom exact speculative verifier benchmark that proves greedy-output equivalence before treating speedups as valid.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact n-gram speculative verifier benchmark for repeated-context GPU decoding
- Success threshold: Exact output equality on 100% of prompts, median speedup >= 1.15x on repeated-context prompts, and p10 speedup >= 0.95x on non-repeated controls.
- Stop condition: Stop if any correctness mismatch remains after verifier implementation fixes, or if median repeated-context speedup is below 1.05x with CPU proposal overhead already below 5% of total latency.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decode-for-cpu-gpu-cascade-41259a2c1eda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
