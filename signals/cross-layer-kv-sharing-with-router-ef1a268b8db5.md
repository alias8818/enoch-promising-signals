# Cross-Layer KV Sharing with Router

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cross-layer-kv-sharing-with-router-ef1a268b8db5`
Run ID: `cross-layer-kv-sharing-with-router-ef1a268b8db5-20260524T194749720855+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a9550f8d4233

## What looked useful

At >=50% theoretical KV-cache saving, distilgpt2 delta NLL was +0.90 to +1.84 and gpt2 delta NLL was +1.51 to +3.32 with top-1 match rates at or below 0.391. Even single-layer sharing in distilgpt2 exceeded the +0.10 NLL tolerance, while the one nearly loss-neutral gpt2 case saved only 8.3%.

## Boundaries and scale limits

Tested only sshleifer/tiny-gpt2 as a harness smoke test, distilgpt2, and gpt2 on 252 scored local-corpus tokens for the medium probes; no trained router, no fine-tuning/alignment objective, no optimized decode kernel, and no broad benchmark suite.

## Claim scope

Naive fixed adjacent and oracle/similarity cross-layer K/V reuse in pretrained GPT-2-family decoders does not preserve next-token behavior at meaningful theoretical KV-cache savings on this bounded local corpus.

## Why it stopped

Proxy/local early falsification rather than full validation: pretrained GPT-2-family layers do not tolerate cross-layer K/V reuse at useful savings levels under fixed adjacent or oracle/similarity routing.

## Recommended next action

Stop this naive/router-proxy line as an early falsification; only pursue a separate bounded follow-up if adding an explicit K/V-alignment or router-training objective.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train an explicit K/V-alignment objective for cross-layer sharing
- Success threshold: At least 33% realized KV-cache memory saving and delta NLL <= 0.10 versus a dense/standard baseline on a held-out corpus, with router overhead included.
- Stop condition: Stop if after bounded fine-tuning no policy reaches 33% KV-cache saving with delta NLL <= 0.10, or if router overhead erases measured decode-time benefit.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-sharing-with-router-ef1a268b8db5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
