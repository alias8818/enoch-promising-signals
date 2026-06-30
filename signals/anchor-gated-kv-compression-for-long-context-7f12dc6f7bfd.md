# Anchor-Gated KV Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-gated-kv-compression-for-long-context-7f12dc6f7bfd`
Run ID: `anchor-gated-kv-compression-for-long-context-7f12dc6f7bfd-20260529T132813298770+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a077dad519f

## What looked useful

Anchor routing is useful when retrieval queries expose segment-anchor structure: at 1.56% retention, target recall was 0.9785 for anchor-gated selection versus about 0.02 for recent/uniform/anchor-recent baselines, using 319 mean score evaluations versus 8320 for full-cache query-top-k. In the anchor-free control, anchor-gated recall fell to 0.0195 while query-top-k stayed at 0.9277, showing a clear failure boundary.

## Boundaries and scale limits

No pretrained/model-level generation, perplexity, learned gates, multi-layer transformer interaction, or real decode latency was tested. Results are synthetic and selector-level only.

## Claim scope

Synthetic single-attention-read KV selection over 8192-token contexts: anchor-gated selection preserves retrieval targets at 1.56% and 6.25% KV retention when queries include target-segment anchor signal, but fails at chance when anchor signal is absent.

## Why it stopped

Closed as no-paper useful signal: the current evidence is synthetic selector-level evidence with a strong mechanism signal and failure boundary, not direct full validation.

## Recommended next action

Run a bounded model-level deepen test by inserting anchor-gated KV selection into a GPT-2-small-class or toy transformer decode loop and comparing retrieval accuracy/perplexity, memory, and latency against recent-window and full query-top-k controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-Level Anchor-Gated KV Decode Probe
- Success threshold: At a KV retention budget of 6.25% or lower, anchor-gated decode improves retrieval accuracy by at least 20 absolute percentage points over recent-window retention while staying within 25% of full query-top-k accuracy and using substantially fewer cache score evaluations.
- Stop condition: Stop if anchor-gated decode does not improve retrieval accuracy by at least 10 absolute percentage points over recent-window retention on the small model task, or if its measured latency exceeds full query-top-k at the same budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-compression-for-long-context-7f12dc6f7bfd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
