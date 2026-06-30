# Medusa-Lite Parameter-Shared Multi-Head

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medusa-lite-parameter-shared-multi-head-cad6530d1118`
Run ID: `medusa-lite-parameter-shared-multi-head-cad6530d1118-20260610T162241824508+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b835979da057

## What looked useful

Parameter sharing in Medusa-style future-token heads produced a reproducible compression/throughput benefit with small per-horizon CE degradation, but all-head exact-match was lower and evidence is not paper-ready.

## Boundaries and scale limits

Toy character-level model only; no GPT-2-small-class baseline, no pretrained LLM attachment, no tokenizer-level corpus, no autoregressive speculative decoding acceptance benchmark, and no production serving measurement.

## Claim scope

On a tiny character-level causal transformer trained on Tiny Shakespeare for 1000 steps across three seeds, a shared-trunk four-head Medusa auxiliary predictor reduced Medusa-head parameters by 49.8% and improved training throughput by 17.4%, while keeping per-horizon Medusa CE within +0.05 of independent heads.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a small direct toy test, not full validation of serving-quality speculative decoding.

## Recommended next action

Run a bounded deepen experiment on a tokenized GPT-2-small-class or frozen pretrained backbone measuring speculative acceptance length and generated-token throughput against independent Medusa heads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenized GPT-2-small Medusa-Lite Shared-Head Validation
- Success threshold: Shared heads reduce auxiliary parameters by at least 30%, keep validation Medusa CE within +0.05 per horizon, and keep speculative generated-token throughput within 5% of independent heads.
- Stop condition: Stop if shared heads lose more than 0.10 Medusa CE on any horizon or reduce speculative generated-token throughput by more than 10% after matched tuning.

## Evidence references

- Artifact root: `<local-path>/projects/medusa-lite-parameter-shared-multi-head-cad6530d1118`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
