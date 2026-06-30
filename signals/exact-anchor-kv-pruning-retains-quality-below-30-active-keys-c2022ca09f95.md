# Exact-Anchor KV Pruning Retains Quality Below 30% Active Keys

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `exact-anchor-kv-pruning-retains-quality-below-30-active-keys-c2022ca09f95`
Run ID: `exact-anchor-kv-pruning-retains-quality-below-30-active-keys-c2022ca09f95-20260628T110206740033+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c6936620b079

## What looked useful

Exact unshifted anchor pruning was a clear negative in the bounded direct probe: at 25.3% and 28.4% active keys it increased loss by +1.1471 and +0.9619 versus dense and underperformed attention-only top-k. Biasing the anchor score reduced damage but still did not beat attention-only top-k.

## Boundaries and scale limits

Does not test larger LLMs, long-context task suites, generation quality, decode-time cache efficiency, hardware latency, or multi-seed robustness. The exact-anchor selector is oracle-style and uses dense attention output before pruning.

## Claim scope

Pretrained distilgpt2 causal LM inference on Wikitext-2 validation blocks, using oracle per-layer/head/query exact unshifted anchor-direction KV pruning below 30% active causal keys.

## Why it stopped

Direct bounded evidence on a pretrained LM falsifies the scoped below-30% exact-anchor quality-retention claim; this is not a full-scale validation but is strong enough to avoid paper-positive treatment.

## Recommended next action

Stop this exact claim as unsupported; only pursue a separate bounded follow-up if testing biased anchor scoring against attention top-k on longer-context tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Biased anchor-direction pruning versus attention top-k on long-context probes
- Success threshold: At less than 30% active keys, biased anchor pruning must reduce loss or task error versus attention-only top-k by at least 5% relative while remaining within 10% perplexity or accuracy degradation versus dense.
- Stop condition: Stop if biased anchor variants fail to beat attention-only top-k on the first long-context benchmark at below-30% active keys.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-pruning-retains-quality-below-30-active-keys-c2022ca09f95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
