# Adaptive Prompt-Lookup Speculative Decoding with Entropy-Gated Acceptance

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-prompt-lookup-speculative-decoding-with-entropy-gated-acceptance-be2f38e67cb7`
Run ID: `adaptive-prompt-lookup-speculative-decoding-with-entropy-gated-acceptance-be2f38e67cb7-20260628T143409396526+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3a0b5f922d63

## What looked useful

Adaptive entropy gating selected low thresholds, achieved 2.18x speedup proxy on repetitive data and 1.62x on mixed data with higher acceptance rates than ungated lookup, and disabled attempts on low-repeat data. Ungated lookup still had the highest speed proxy on repetitive and mixed synthetic suites.

## Boundaries and scale limits

No real language model, tokenizer, GPU inference, KV-cache behavior, or wall-clock serving path was tested. Speedup is a target-validation-call proxy, not measured model throughput.

## Claim scope

Synthetic replay evidence over repetitive, mixed, and low-repeat token sequences shows entropy-gated prompt lookup improves accepted/proposed draft precision and suppresses low-value attempts, while preserving exact output through target fallback.

## Why it stopped

No-paper useful signal: the evidence is synthetic/proxy-only and adaptive entropy gating did not outperform ungated prompt lookup on the primary speed proxy, although it improved draft precision and waste avoidance.

## Recommended next action

Run a bounded GPT-2-small-class real-model follow-up on a repeated-context corpus measuring wall-clock tokens/s, target forward calls, accepted tokens, rejection overhead, and exact output equality against ungated prompt lookup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model entropy-gated prompt lookup on GPT-2-small-class repeated-context decoding
- Success threshold: Adaptive entropy gating reaches at least 90% of ungated prompt-lookup wall-clock throughput while reducing zero-accept attempts by at least 25% and preserving zero exact-output mismatches on the repeated-context corpus.
- Stop condition: Stop if adaptive gating is slower than ungated lookup by more than 10% without at least a 25% reduction in zero-accept attempts, or if exact output mismatches occur.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-prompt-lookup-speculative-decoding-with-entropy-gated-acceptance-be2f38e67cb7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
