# Sink Tokens plus Sliding Window Attention for 8K Local Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `sink-tokens-plus-sliding-window-attention-for-8k-local-context-82c68822ec69`
Run ID: `sink-tokens-plus-sliding-window-attention-for-8k-local-context-82c68822ec69-20260523T232100137625+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/84a15477df72

## What looked useful

Across windows 128, 256, 512, 1024; layers 8, 16, 24, 32; and sink counts 4, 16, 64, sink-plus-sliding-window attention had the same earliest reachable non-sink token as the same-prefix sliding-window baseline in 48/48 checks. Sink tokens increased fan-in by 0.39% to 49.61% without adding causal paths from old non-sink content.

## Boundaries and scale limits

No model was trained and no GPU kernel was benchmarked. Evidence is an architecture-level graph reachability probe over 48 8K configurations, not a full language-model quality or serving study.

## Claim scope

For standard autoregressive causal masks with initial global sink tokens plus sliding-window attention, sink tokens do not extend non-sink content reachability at 8K sequence length beyond the stacked sliding-window receptive field.

## Why it stopped

Proxy/architecture-level early falsification: causal sink tokens cannot attend forward to later non-sink content, so they cannot relay old non-sink information beyond the sliding-window receptive field.

## Recommended next action

Stop this no-paper line unless the next run changes the mask or memory mechanism; ordinary causal sink tokens should not be pursued as a way to extend 8K retrievable non-sink context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny trained retrieval check for causal sink-plus-window masks
- Success threshold: Sink-plus-window must show no statistically meaningful accuracy improvement over sliding-window on unreachable non-sink keys, while both masks perform above chance on reachable keys.
- Stop condition: Stop if the trained model results match graph reachability, or if training instability prevents both masks from learning reachable-key controls.

## Evidence references

- Artifact root: `<local-path>/projects/sink-tokens-plus-sliding-window-attention-for-8k-local-context-82c68822ec69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
