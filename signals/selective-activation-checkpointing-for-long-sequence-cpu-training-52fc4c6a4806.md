# Selective activation checkpointing for long-sequence CPU training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `selective-activation-checkpointing-for-long-sequence-cpu-training-52fc4c6a4806`
Run ID: `selective-activation-checkpointing-for-long-sequence-cpu-training-52fc4c6a4806-20260620T221452141426+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/484bed1dc205

## What looked useful

Selective activation checkpointing is a real but regime-dependent CPU memory/time tradeoff: unhelpful or worse at 256-768 tokens in this setup, useful from 1024 tokens onward, but consistently less memory-efficient than uniform whole-block checkpointing.

## Boundaries and scale limits

Synthetic one-step next-token training only; tiny 4-layer d_model=128 model; sequence lengths up to 2048; one repeat per isolated child process; no real corpus, no convergence test, no GPT-2-small-class validation, no multi-epoch throughput study.

## Claim scope

In a synthetic CPU PyTorch tiny-transformer training probe, selective checkpointing of the attention core begins reducing peak RSS at longer sequence lengths and reaches a 33.1% peak RSS delta reduction at 2048 tokens versus no checkpointing, with exact loss parity. Whole-block checkpointing saves more memory, while selective attention is only modestly faster in the largest tested cases.

## Why it stopped

No-paper useful-signal result: the local experiment directly tested the mechanism but only in a synthetic one-step tiny-model setting, so it is not full validation or paper-ready evidence.

## Recommended next action

Run a bounded deepen follow-up with a GPT-2-small-class or parameter-matched CPU model over multiple training steps on a real text corpus, comparing no checkpointing, whole-block checkpointing, and a selective policy with repeated measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-step CPU training validation for selective attention checkpointing
- Success threshold: At sequence length >=2048, selective checkpointing must reduce peak RSS by >=20% versus no checkpointing, be >=5% faster than whole-block checkpointing, and keep final loss within 1% of the no-checkpointing baseline over the bounded run.
- Stop condition: Stop if selective checkpointing is <10% lower peak RSS than no checkpointing, is not faster than whole-block checkpointing, or shows loss divergence beyond 1% in the bounded multi-step run.

## Evidence references

- Artifact root: `<local-path>/projects/selective-activation-checkpointing-for-long-sequence-cpu-training-52fc4c6a4806`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
