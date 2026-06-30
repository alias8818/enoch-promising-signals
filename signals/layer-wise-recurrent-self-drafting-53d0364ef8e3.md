# Layer-Wise Recurrent Self-Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `layer-wise-recurrent-self-drafting-53d0364ef8e3`
Run ID: `layer-wise-recurrent-self-drafting-53d0364ef8e3-20260524T220245418562+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1f1cc68664d7

## What looked useful

Intermediate layers showed a cost/acceptance mismatch: depths 1-6 were cheap but accepted only 14-18% of first tokens, while depth 11 accepted 52% of first tokens and 1.03 tokens per 4-token block but cost 2.96 ms versus 3.27 ms for the full model. The best serial speed bound was 0.52x, below break-even.

## Boundaries and scale limits

Tested only GPT-2-small on 16 prompts, 128 rollout contexts, 128 recurrent 4-token draft blocks, greedy decoding, and a non-production partial-forward latency harness. Larger models, trained draft heads, sampling acceptance, and optimized KV-cache implementations were not evaluated.

## Claim scope

Naive untrained GPT-2-small layer-wise recurrent self-drafting, using intermediate hidden states projected through the tied LM head and greedy full-model verification, does not provide a decoding speedup on the tested prompt set.

## Why it stopped

Proxy early falsification, not full validation: the direct GPT-2-small greedy self-drafting test found no layer with both sufficient acceptance and sufficient cost reduction to imply speedup.

## Recommended next action

Stop this naive self-drafting path as a proxy early falsification; only revisit with a trained layer-specific draft head or cache-aware implementation that can beat the measured acceptance/cost tradeoff.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Layer-Specific Draft Head for GPT-2-Small Self-Drafting
- Success threshold: Held-out first-token acceptance at depth 3 or 6 of at least 45%, mean accepted tokens per 4-token block of at least 1.2, and measured or defensible cache-aware speed bound above 1.1x versus full greedy decoding.
- Stop condition: Stop if trained depths 3 and 6 remain below 35% first-token acceptance or if measured partial-forward plus verification latency cannot exceed a 1.0x speed bound.

## Evidence references

- Artifact root: `<local-path>/projects/layer-wise-recurrent-self-drafting-53d0364ef8e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
