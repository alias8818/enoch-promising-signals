# CPU n-gram cache speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-cache-speculative-decoding-ea2acae71d10`
Run ID: `cpu-n-gram-cache-speculative-decoding-ea2acae71d10-20260530T084143633802+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/241613175b74

## What looked useful

The mechanism is real under causal trace simulation: shuffled controls collapse to about 1.005x word-token and 1.058x byte-token verifier-call reduction, while repetitive synthetic traces reach about 3.7x at draft length 8 and byte-level Shakespeare reaches about 2.0x. Natural word-token Shakespeare reaches only about 1.11x, making the broad idea mixed and not paper-ready.

## Boundaries and scale limits

No neural verifier, no GPT/BPE tokenizer, no end-to-end serving latency, no large model, and no production workload traces. Verifier-call reduction is an idealized proxy and may overstate or understate wall-clock speedup depending on target model batch verification cost.

## Claim scope

Trace-level online CPU n-gram cache speculative decoding over project prompt text, Tiny Shakespeare word and byte token streams, synthetic repetitive streams, and shuffled controls. The cache causally drafts continuations from prior matching contexts and reduces idealized verifier calls on repetitive or byte-level traces, but only modestly on natural word-token text.

## Why it stopped

Trace-level evidence supports the repetition mechanism but is mixed and proxy-only; natural word-token gains are too small and no real neural verifier latency was measured.

## Recommended next action

Stop this run as a no-paper useful signal; next run should do a bounded model-in-loop GPT/BPE latency test on a small target model and repetition-heavy workloads before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-loop CPU n-gram speculative decoding latency on GPT/BPE workloads
- Success threshold: At least 1.15x end-to-end wall-clock speedup over greedy decoding on two repetition-heavy workloads with exact output equivalence, and no more than 5% slowdown on the natural-language control.
- Stop condition: Stop if model-in-loop speedup is below 1.05x on repetition-heavy workloads or if verifier batch overhead erases the trace-level call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-cache-speculative-decoding-ea2acae71d10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
