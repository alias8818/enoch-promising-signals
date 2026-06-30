# Pretrained Decoder KV Patch Test for Anchor-Preserved Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pretrained-decoder-kv-patch-test-for-anchor-preserved-comp-9a64963949`
Run ID: `pretrained-decoder-kv-patch-test-for-anchor-preserved-comp-9a64963949-20260527T195011049320+0000`

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

- Parent run decision: Anchor-Preserved KV Cache Compression: enoch://control-plane/projects/anchor-preserved-kv-cache-compression-3ae73f8de7f7/runs/anchor-preserved-kv-cache-compression-3ae73f8de7f7-20260527T160111087449+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/529125218837

## What looked useful

Contextualized K/V states for retained anchors can carry useful information about removed context at moderate retention, but sparse 25% anchor retention is not robust and can underperform a simple compressed re-encode baseline.

## Boundaries and scale limits

Single small pretrained decoder, short contexts, bundled real-text passages, one deterministic anchor schedule, CPU inference only; not benchmark-corpus, long-context, multi-model, learned-compression, or publication-grade evidence.

## Claim scope

On distilgpt2 with 48 deterministic real-text windows and 128-token contexts, anchor KV patching improved next-token continuation distribution similarity versus compressed anchor re-encoding at 50% retention, but worsened it at 25% retention.

## Why it stopped

Tier 1 direct test produced a mixed no-paper result: mechanism support at 50% retention and early falsification at 25% retention, insufficient for paper readiness.

## Recommended next action

Run a bounded deepen follow-up on a larger benchmark sample with a retention sweep around 25%-62.5% and at least one additional pretrained decoder; stop if 50% retention fails to improve KL by at least 20% against compressed re-encode on both models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retention Sweep for Anchor-Preserved KV Patching on Benchmark Text
- Success threshold: At 50% retention, KV patching must reduce mean KL(full||candidate) by at least 20% versus compressed re-encoding on both tested models, with improvement on at least 70% of paired windows; 25% retention may remain negative if the threshold transition is clear.
- Stop condition: Stop if 50% retention fails the KL improvement threshold on either model, or if identity/full-retention controls fail to recover full-context distributions.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-decoder-kv-patch-test-for-anchor-preserved-comp-9a64963949`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
