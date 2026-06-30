# Cross-Tier KV-Cache Reuse in Model Cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-tier-kv-cache-reuse-in-model-cascades-6c84a6d4374f`
Run ID: `cross-tier-kv-cache-reuse-in-model-cascades-6c84a6d4374f-20260525T055011249385+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/db3d7bb517ac

## What looked useful

Layer-1 raw cache reuse was close to true-cache decoding (mean KL 0.0040, top-1 match 0.950) and beat zero/random controls, but 3-layer reuse was worse than zero on KL/top-10 overlap and 6-layer reuse strongly corrupted the distribution (mean KL 1.5883, top-1 match 0.275).

## Boundaries and scale limits

Tested 40 fixed prompts, one-step decode, gpt2/distilgpt2 only, no learned adapters, no different-width projection, no multi-token drift, no large-model or production serving latency validation.

## Claim scope

In a same-tokenizer, same-width GPT-2-family probe, direct raw KV-cache substitution from distilgpt2 into gpt2 preserves next-token behavior for one lower layer but degrades substantially when three or six lower layers are substituted.

## Why it stopped

Bounded direct evidence supports only shallow raw reuse and falsifies naive deeper raw KV reuse for this same-shape GPT-2 cascade; this is not a full validation or paper-ready positive result.

## Recommended next action

Stop this raw-cache-transfer run as no-paper useful signal; run a bounded follow-up that trains or fits lightweight per-layer KV adapters for 3-6 transferred layers and compares against zero/random controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned KV Adapters for Cross-Tier GPT-2 Cache Reuse
- Success threshold: For at least three transferred lower layers on held-out prompts: mean KL no worse than the zero-cache control, top-1 match at least 0.85, top-10 overlap at least 0.85, and estimated net prefill latency saving at least 10%.
- Stop condition: Stop if adapters fail to beat zero/random controls on held-out prompts or if adapter overhead eliminates the projected latency saving.

## Evidence references

- Artifact root: `<local-path>/projects/cross-tier-kv-cache-reuse-in-model-cascades-6c84a6d4374f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
