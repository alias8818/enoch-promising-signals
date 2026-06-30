# Real-model exact-anchor KV cache intervention on a small transformer

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-exact-anchor-kv-cache-intervention-on-a-small-t-7e9a99a578`
Run ID: `real-model-exact-anchor-kv-cache-intervention-on-a-small-t-7e9a99a578-20260629T062152902637+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Exact-Anchor KV Compression for CPU Long Context: enoch://control-plane/projects/exact-anchor-kv-compression-for-cpu-long-context-9d64efbf542a/runs/exact-anchor-kv-compression-for-cpu-long-context-9d64efbf542a-20260629T060212328418+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a3c7fc187826

## What looked useful

distilgpt2 exact-anchor KV swaps recovered a mean 0.898 clean-corrupt effect fraction across 12/12 cases, reverse swaps averaged 0.886, and non-anchor controls averaged 0.044 with all controls below 0.25 absolute effect fraction.

## Boundaries and scale limits

Single small model, synthetic one-token anchors, all-layer intervention, first-token log-odds only, no natural corpus, no multi-token anchors, no layer/head localization, no larger-model robustness.

## Claim scope

On 12 one-token synthetic memo prompts with distilgpt2 on CPU, replacing the exact cached answer-anchor key/value span across all layers causally recovered most of the clean-vs-corrupt answer-token log-odds gap after an answer cue.

## Why it stopped

Closed as no-paper useful signal: direct small-model evidence supports the mechanism, but robustness and localization evidence are insufficient for a publication-grade claim.

## Recommended next action

Run a bounded deepen test on GPT-2-small-class or Pythia-70M with layer/head ablations, multi-token anchors, and the same non-anchor controls before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer-localized exact-anchor KV interventions on GPT-2-small-class models
- Success threshold: Mean anchor effect fraction above 0.5 with at least 80% of cases above 0.25, and mean non-anchor/random controls below 0.15 absolute effect fraction across both one-token and multi-token suites.
- Stop condition: Stop if anchor effects fall below 0.25 mean effect fraction or controls exceed half the anchor effect in two independent model/prompt batches.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-exact-anchor-kv-cache-intervention-on-a-small-t-7e9a99a578`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
