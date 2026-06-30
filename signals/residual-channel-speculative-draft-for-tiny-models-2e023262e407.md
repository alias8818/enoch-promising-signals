# Residual-channel speculative draft for tiny models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-speculative-draft-for-tiny-models-2e023262e407`
Run ID: `residual-channel-speculative-draft-for-tiny-models-2e023262e407-20260522T114008478507+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4286aa1c5b71

## What looked useful

Mid-layer residual-channel probes consistently beat embedding controls: at 128 channels top1 agreement was 0.431 vs 0.343 and distribution-overlap acceptance proxy was 0.313 vs 0.262; at 256 channels top1 was 0.472 vs 0.374 and overlap was 0.340 vs 0.300. Final-residual ceilings remained higher, indicating the residual probe captures useful but incomplete teacher information.

## Boundaries and scale limits

This is a single-teacher, single-corpus, offline probe. It does not measure end-to-end speculative decoding speed, multi-token acceptance, latency overhead, training robustness, or GPT-2-small-class/full-scale generality.

## Claim scope

On distilgpt2 over 24,576 Tiny Shakespeare token positions, linear heads trained on variance-selected intermediate residual channels predict the frozen teacher's next-token distribution better than unigram and embedding-channel controls at matched widths.

## Why it stopped

No-paper closure: this run produced a useful offline proxy signal, but not direct serving evidence or enough model/corpus breadth for publication-grade validation.

## Recommended next action

Run a bounded deepen test with an actual speculative decoding loop, wall-clock latency, and acceptance metrics on at least GPT-2-small or comparable tiny LMs before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end residual-channel speculative decoding for GPT-2-small-class models
- Success threshold: Residual-channel drafting must improve end-to-end tokens/second by at least 10% over no-draft decoding while matching verifier output exactly and achieving acceptance competitive with a parameter-matched draft baseline.
- Stop condition: Stop if residual-channel draft acceptance is below 0.25, if overhead eliminates throughput gains, or if gains disappear across a second prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-speculative-draft-for-tiny-models-2e023262e407`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
