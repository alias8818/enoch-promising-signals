# Attention-Score KV Eviction vs Dense Baseline on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `attention-score-kv-eviction-vs-dense-baseline-on-gpt-2-small-8f81d9ab1c0f`
Run ID: `attention-score-kv-eviction-vs-dense-baseline-on-gpt-2-small-8f81d9ab1c0f-20260628T123206774046+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3761ac6f7de5

## What looked useful

Attention-score eviction reduced the multi-span NLL penalty versus recency from +4.6309 to +1.8474 at capacity 64, from +3.1014 to +0.8531 at capacity 128, and from +0.3797 to +0.1474 at capacity 256. Random retention was worse than attention at capacity 64 but slightly better at 128 and 256, so cumulative attention mass alone is not a clearly dominant heuristic.

## Boundaries and scale limits

Tested one model family/size, WikiText-2 only, 1024 aggregated multi-span eval tokens plus smoke/single-span checks, capacities 64/128/256, batch size 1, no long-context serving kernels, no generation-quality study, no multi-seed random replication beyond deterministic span seeds.

## Claim scope

On GPT-2-small evaluated token-by-token on four WikiText-2 raw test spans, simple cumulative attention-score KV eviction is much better than recency at fixed low/mid cache budgets but does not match dense KV cache and is not consistently better than random retention.

## Why it stopped

Bounded direct evidence shows the simple attention-score policy does not match dense and is not consistently better than random retention, so the current hypothesis is mixed and not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, test a hybrid attention-plus-recency policy with random-seed replication on at least two additional language-modeling datasets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Attention-Recency KV Eviction With Replicated Random Baselines
- Success threshold: Hybrid attention-recency must reduce delta NLL versus dense by at least 0.10 compared with the best random baseline at two or more capacities without losing to recency on any dataset.
- Stop condition: Stop if hybrid fails to beat the best random baseline on at least two datasets or if gains are below 0.05 NLL at all tested capacities.

## Evidence references

- Artifact root: `<local-path>/projects/attention-score-kv-eviction-vs-dense-baseline-on-gpt-2-small-8f81d9ab1c0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
