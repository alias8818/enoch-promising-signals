# Byte-Anchored Needle-in-Haystack at 64k on Consumer GPU

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `68`
Project ID: `byte-anchored-needle-in-haystack-at-64k-on-consumer-gpu-f208782b64a0`
Run ID: `byte-anchored-needle-in-haystack-at-64k-on-consumer-gpu-f208782b64a0-20260628T163551964937+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce0d1b354178

## What looked useful

Byte anchors are usable by a capable 8B model at 16k in this harness but did not beat the semantic NEEDLE control; a smaller 1.2B long-context model failed byte-anchor retrieval at 4k and all retrieval at 32k. The 64k consumer-GPU claim remains unvalidated under this worker execution window.

## Boundaries and scale limits

No completed 64k generation result. Llama 8B 64k attempts terminated after shard load before trial checkpoint; LFM 64k tokenized to 67832 prompt tokens but terminated during generation. Synthetic filler only, one seed per mode/position, no natural-document or adversarial robustness.

## Claim scope

Synthetic one-needle retrieval with fixed-width byte anchors was supported for Llama-3.1-8B-Instruct at 16k tokens (6/6 including semantic controls), failed for LFM2.5-1.2B at 32k (0/6), and was not completed at 64k because generation attempts were SIGTERM-limited before answers.

## Why it stopped

Target 64k evidence was execution-limited: two Llama 8B attempts were SIGTERM'd after model load before JSONL trial output, and the LFM 64k byte-anchor trial tokenized to 67832 prompt tokens but was SIGTERM'd during generation. Lower-context evidence is useful but not a 64k validation.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next action is a longer-window direct 64k rerun that keeps Llama-3.1-8B-Instruct loaded and checkpoints each early/middle/late byte-anchor and semantic trial.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/byte-anchored-needle-in-haystack-at-64k-on-consumer-gpu-f208782b64a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
