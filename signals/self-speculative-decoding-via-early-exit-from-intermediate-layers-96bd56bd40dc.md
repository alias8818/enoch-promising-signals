# Self-Speculative Decoding via Early Exit from Intermediate Layers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-from-intermediate-layers-96bd56bd40dc`
Run ID: `self-speculative-decoding-via-early-exit-from-intermediate-layers-96bd56bd40dc-20260524T174323308336+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1d27f25872ce

## What looked useful

Layer-10, already 83% of GPT-2-small depth, matched final top-1 only 46.6%; cheaper layers were worse, and the conservative speed proxy stayed below 1.0 for all tested layers.

## Boundaries and scale limits

Evaluated 8,001 next-token positions from a public-domain text corpus on GPT-2-small only; timing is a forward-pass proxy and does not implement production KV-cache multi-token speculative decoding.

## Claim scope

On a bounded GPT-2-small natural-text probe, untrained intermediate-layer hidden states with the tied LM head are not accurate enough to serve as a simple deterministic self-speculative draft path.

## Why it stopped

Proxy early falsification: the simplest untrained intermediate-layer LM-head draft has too little final-token agreement to justify a paper or longer validation as-is.

## Recommended next action

Stop this no-paper run; only pursue a bounded follow-up if it adds confidence gating or a trained auxiliary exit head and measures real KV-cache decoding latency against a dense baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated trained early-exit heads for self-speculative GPT-2 decoding
- Success threshold: At least 1.15x median tokens/sec improvement over dense GPT-2-small on >=100 prompts with exact final-model greedy outputs and no quality regression under the chosen decoding rule.
- Stop condition: Stop if calibrated acceptance remains below 70% at any layer saving at least 25% of per-token draft compute, or if measured end-to-end decoding speed is <=1.0x dense baseline.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-from-intermediate-layers-96bd56bd40dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
