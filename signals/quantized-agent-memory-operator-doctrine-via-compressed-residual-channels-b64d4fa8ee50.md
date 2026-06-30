# Quantized Agent Memory: Operator Doctrine via Compressed Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-agent-memory-operator-doctrine-via-compressed-residual-channels-b64d4fa8ee50`
Run ID: `quantized-agent-memory-operator-doctrine-via-compressed-residual-channels-b64d4fa8ee50-20260619T105743284574+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/69005c8b0bbe

## What looked useful

Dense scalar quantization is a strong baseline for agent-memory compression on this proxy: int8 matched fp32 action accuracy at 3.96x compression and int4 was within 0.42 percentage points at 7.84x compression. Random compressed residual channels improved with channel width but still missed the 2-point tolerance even at 352/384 channels.

## Boundaries and scale limits

Synthetic vectors only; no real LLM agent, no real operator doctrine corpus, no learned memory writer/reader, no multi-turn persistence, no full downstream task evaluation. Channel bases were random orthonormal projections rather than learned/adaptive bases.

## Claim scope

On a deterministic synthetic action-labelled memory retrieval proxy with 2,048 entries, 4,096 noisy queries, 384-dimensional vectors, and 32 actions, random-projection compressed residual channels did not preserve operator-action accuracy within 2 percentage points of fp32 at any tested compression setting, while dense int4/int8 scalar quantization did.

## Why it stopped

Bounded synthetic proxy falsified the random compressed residual-channel version of the hypothesis, not a full validation or full rejection of all learned residual-channel variants.

## Recommended next action

Stop this run as a no-paper useful signal; test learned or PCA residual-channel bases against dense int4/int8 baselines before considering larger agent-memory validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned residual-channel bases for quantized agent memory
- Success threshold: At <=196 bytes per entry, learned residual channels must achieve action accuracy within 2 percentage points of fp32 and at least 1 percentage point above dense int4 on two of three noise levels.
- Stop condition: Stop if learned residual channels fail to beat dense int4 action accuracy at matched bytes per entry on the first two tested noise levels.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-memory-operator-doctrine-via-compressed-residual-channels-b64d4fa8ee50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
