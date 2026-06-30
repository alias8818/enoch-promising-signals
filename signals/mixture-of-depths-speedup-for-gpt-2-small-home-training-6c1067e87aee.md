# Mixture-of-depths speedup for GPT-2-small home training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixture-of-depths-speedup-for-gpt-2-small-home-training-6c1067e87aee`
Run ID: `mixture-of-depths-speedup-for-gpt-2-small-home-training-6c1067e87aee-20260528T220513266360+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0390c3e9c4a0

## What looked useful

MoD routing produced a real but modest measured speedup, far below the naive 2x expectation for 50% active tokens. Capacity 0.25 improved throughput only slightly beyond cap 0.50 and degraded short-run loss on the tested seed; cap 0.75 nearly erased the speed benefit. Larger batch/sequence showed 14.8% speedup and 13.6% lower peak CUDA allocation.

## Boundaries and scale limits

Short runs only: 40-100 training steps, TinyShakespeare char-level data, small vocabulary/head, simple unfused router, no full GPT-2 BPE corpus, no convergence test, no publication-grade quality or loss-to-wall-clock validation.

## Claim scope

On an NVIDIA GB10, a simple top-k token-level MoD variant in a GPT-2-small-style 12-layer/768-wide decoder produced reproducible short-run training throughput gains of 10.3% to 14.8% versus a dense control on TinyShakespeare char-level training, with inconclusive short-run validation-loss impact.

## Why it stopped

Proxy/short-run evidence supports only a modest mechanism-level speedup and does not validate a large or full GPT-2-small home-training acceleration claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should perform a bounded GPT-2 BPE corpus loss-to-wall-clock comparison before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded GPT-2 BPE loss-to-wall-clock MoD confirmation
- Success threshold: MoD reaches the dense control's best validation loss at least 10% faster wall-clock, or has at least 0.03 lower validation loss at equal wall-clock, with no memory increase and no unstable seeds.
- Stop condition: Stop if MoD is under 5% faster to matched validation loss, if validation loss is consistently worse by more than 0.05 at equal wall-clock, or if routing overhead dominates the measured compute savings.

## Evidence references

- Artifact root: `<local-path>/projects/mixture-of-depths-speedup-for-gpt-2-small-home-training-6c1067e87aee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
