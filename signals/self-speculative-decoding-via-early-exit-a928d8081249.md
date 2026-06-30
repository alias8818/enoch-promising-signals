# Self-Speculative Decoding via Early Exit

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-a928d8081249`
Run ID: `self-speculative-decoding-via-early-exit-a928d8081249-20260529T201542020620+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/766a0e159b49

## What looked useful

Mid-layer exits had very low acceptance (0-8.3% for 4-token drafts) and 0.37-0.40x emitted-token-normalized throughput. Late exits improved acceptance but lost compute advantage; layer 11 with 2-token drafts was best at 58.3% acceptance and 0.929x emitted-token-normalized throughput, still below baseline.

## Boundaries and scale limits

Only GPT-2 small, short fixed prompts, greedy decoding, layers 3/6/9/10/11, draft lengths 2 and 4, and a diagnostic PyTorch implementation were tested; this is not a large-model or optimized serving-kernel validation.

## Claim scope

For pretrained GPT-2 small on 12 fixed natural-language prompts, untrained intermediate-layer early exits using the final LM head did not produce emitted-token speedup under exact greedy self-speculative verification.

## Why it stopped

Proxy-scale but direct mechanism test found no emitted-token speedup; this is an early falsification rather than a full validation of all self-speculative decoding variants.

## Recommended next action

Stop this naive untrained early-exit variant as an early bounded falsification; the next bounded test should train or calibrate early-exit heads and require greater than 1.10x emitted-token throughput before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit heads for self-speculative GPT-2 decoding
- Success threshold: At least 1.10x emitted-token-normalized throughput versus greedy baseline with exact final-model greedy outputs and no degradation in generated token sequence.
- Stop condition: Stop if trained heads remain below 1.00x emitted-token-normalized throughput or require exits so late that idealized layer-latency speedup is below 1.00x.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-a928d8081249`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
