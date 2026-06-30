# Prompt-Suffix Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `prompt-suffix-speculative-decoding-19cb0b102fe8`
Run ID: `prompt-suffix-speculative-decoding-19cb0b102fe8-20260603T150659371909+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2995134c597b

## What looked useful

Across 782,336 GPT-2/Wikitext token positions, true future suffix tokens matched the target argmax only 33.34% of the time. For 16-token draft blocks, 66.58% rejected immediately, mean accepted prefix length was 0.527 tokens, and only 0.0245% of blocks were fully accepted. A 1024-window probability diagnostic found only 21.23% mean target probability on the true suffix token.

## Boundaries and scale limits

Proxy-only local benchmark: no learned drafter, no end-to-end serving kernel, no large instruction/code model, no FIM-trained target, and no real latency speedup measurement.

## Claim scope

For GPT-2 small on Wikitext-2, an oracle deterministic suffix drafter proposing true future tokens does not produce long greedy-accepted speculative blocks; simple prompt-suffix token drafting is therefore unlikely to deliver useful speedup in this setting.

## Why it stopped

Proxy evidence is negative for the simple mechanism and insufficient for a paper; full validation would require a real suffix-conditioned drafter and end-to-end speculative decoding measurements.

## Recommended next action

Stop this run as a proxy early falsification of simple deterministic prompt-suffix drafting; only pursue a follow-up if testing a learned suffix-conditioned drafter on an infill/code workload with direct latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Suffix-conditioned draft model on code infill traces
- Success threshold: At least 1.5x median end-to-end decoding speedup over greedy target decoding and at least 20% improvement over a prefix-only draft baseline on the same target/model/hardware, with exact output equivalence where required.
- Stop condition: Stop if accepted tokens per verification pass remain below 1.5 or measured median latency speedup is below 1.2x after a calibrated small code-infill benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-suffix-speculative-decoding-19cb0b102fe8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
