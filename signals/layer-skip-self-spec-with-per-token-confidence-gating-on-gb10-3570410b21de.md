# Layer-skip self-spec with per-token confidence gating on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-skip-self-spec-with-per-token-confidence-gating-on-gb10-3570410b21de`
Run ID: `layer-skip-self-spec-with-per-token-confidence-gating-on-gb10-3570410b21de-20260629T105637188832+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d677fc24f5fe

## What looked useful

On the simplified deterministic task, full depth and layer-2 exits reached 100% eval accuracy. At confidence threshold 0.95, the primary run accepted 99.46% of tokens with 100% accepted-token agreement and an estimated 66.31% layer-work saving; seed-11 replication accepted 93.16% with 100% agreement and 62.11% estimated layer-work saving. Layer-2-only GPU microbenchmarks were about 2.90x faster than full-depth forwards.

## Boundaries and scale limits

No pretrained LLM, no natural-language corpus, no GPT-2-small-class baseline, no real dynamic fallback serving implementation, and no multi-token speculative verification. Two harder synthetic generators failed to produce a usable full-model baseline in this bounded run.

## Claim scope

Toy synthetic local-transition next-token task with a 6-layer causal transformer trained on GB10; layer-2 auxiliary exit used as the confidence-gated draft path.

## Why it stopped

Closed as no-paper useful signal: the positive evidence is toy-scoped and does not validate the original architecture idea on realistic language modeling or serving.

## Recommended next action

Run a bounded deepen follow-up on a GPT-2-small-class model or real text corpus with trained intermediate exits and end-to-end dynamic fallback latency before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text layer-skip confidence gate on a GPT-2-small-class baseline
- Success threshold: At least 25% accepted tokens at a threshold whose accepted-token disagreement with the full model is below 1%, with end-to-end decode latency at least 10% faster and quality loss below 1% relative on the chosen metric.
- Stop condition: Stop if the full-depth baseline cannot be trained/evaluated reproducibly, if accepted-token disagreement remains above 1% at accept rates above 10%, or if dynamic fallback latency is not faster than full-depth decoding.

## Evidence references

- Artifact root: `<local-path>/projects/layer-skip-self-spec-with-per-token-confidence-gating-on-gb10-3570410b21de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
