# Anchor-Pinned Long-Context Memory with Compressed State Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pinned-long-context-memory-with-compressed-state-anchors-eea790f631ab`
Run ID: `anchor-pinned-long-context-memory-with-compressed-state-anchors-eea790f631ab-20260621T214333789858+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf76d8b746b8

## What looked useful

Anchor conditioning matters, but per-anchor compressed state anchors did not provide a meaningful advantage over an anchor-aware global sketch and were far worse than a same-byte exact recent-window baseline in this proxy.

## Boundaries and scale limits

No learned transformer, natural-language corpus, KV-cache integration, or GPT-2-small-class training was run; results are CPU-only synthetic proxy evidence, not publication-grade validation of a model architecture.

## Claim scope

Synthetic associative-recall proxy with explicit anchor IDs, fixed-size int16 count sketches, 64 anchors, 64-value vocabulary, and same-byte comparisons against global compressed sketches and an exact recent-window baseline.

## Why it stopped

Proxy early falsification: fixed per-anchor compressed sketches did not beat the strongest local baseline and only marginally matched an anchor-aware global sketch, so the current mechanism is not worth paper-scale validation without a learned-memory follow-up.

## Recommended next action

Stop this run as a no-paper useful negative/proxy result; next run should test a learned tiny-transformer CSA against exact-window and anchor-aware compressed baselines with a >=5 percentage-point accuracy threshold on contexts exceeding the exact window.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer learned compressed state anchors versus exact-window baselines
- Success threshold: CSA improves aggregate and oldest-quartile accuracy by at least 5 percentage points over both exact-window and anchor-aware global compressed baselines at matched memory/parameter budget across at least 3 seeds.
- Stop condition: Stop if CSA fails to exceed either baseline by 5 percentage points after the bounded training budget or if oldest-quartile accuracy remains below the exact recent-window baseline.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-long-context-memory-with-compressed-state-anchors-eea790f631ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
