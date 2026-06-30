# N-gram draft verification for CPU small-model decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-draft-verification-for-cpu-small-model-decoding-c2f6c5e38960`
Run ID: `n-gram-draft-verification-for-cpu-small-model-decoding-c2f6c5e38960-20260524T174322915309+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0e85bfeb5280

## What looked useful

The best corrected n-gram setting reduced target calls by only 4.8% with 19.9% draft acceptance and an estimated 0.497x end-to-end speed; the default min-n sweep reduced calls by only 1.8% with an estimated 0.519x speed. The mechanism needs far more accepted tokens per target call or much stronger batched verification efficiency before scale-up is justified.

## Boundaries and scale limits

This run used exact natural-text continuation traces and a compiled dense-kernel CPU proxy, not actual transformer logits, tokenizer-specific behavior, or real KV-cache serving latency. It does not rule out stronger learned drafters, domain-specific repetitive workloads, or optimized real-model verification kernels.

## Claim scope

On 96 natural-text Tiny Shakespeare windows with 12,288 evaluated continuation tokens, a simple history n-gram drafter plus CPU batch-verification proxy did not reduce estimated decoding cost for CPU small-model decoding.

## Why it stopped

Bounded proxy evidence on natural-text traces and a CPU verification kernel showed sub-baseline estimated speed; simple n-gram draft verification is not viable enough for paper writing or larger local runs.

## Recommended next action

Stop this no-paper line unless a bounded real-model CPU follow-up can show at least 1.10x wall-clock speedup with exact greedy-output equivalence; current evidence is an early proxy falsification, not a full validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Decoder N-gram Draft Verification Check
- Success threshold: At least 1.10x median wall-clock tokens/s over baseline on 1000 or more generated tokens with identical greedy outputs and no more than 5% p95 latency regression.
- Stop condition: Stop if exact-output verification cannot be implemented locally, or if target-call reduction remains below 10%, or if wall-clock speedup is below 1.05x after 1000 generated tokens.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-verification-for-cpu-small-model-decoding-c2f6c5e38960`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
