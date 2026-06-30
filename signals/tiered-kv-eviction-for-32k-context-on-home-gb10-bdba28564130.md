# Tiered KV eviction for 32k context on home GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiered-kv-eviction-for-32k-context-on-home-gb10-bdba28564130`
Run ID: `tiered-kv-eviction-for-32k-context-on-home-gb10-bdba28564130-20260610T232621928435+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/603d8d89d296

## What looked useful

Across 32k-context sweeps with budgets 2048, 4096, and 8192 over five seeds, tiered retention improved retained attention mass over sliding by 0.303, 0.258, and 0.165 respectively, and improved needle retention over sliding by 0.875, 0.638, and 0.380. Compared with heavy-hitter-only retention, tiered preserved equal or better needle retention while increasing retained mass by 0.504, 0.493, and 0.408.

## Boundaries and scale limits

No real transformer inference was run; attention traces were synthetic; compressed KV was modeled as fixed cost and utility rather than real quantized activations; no perplexity, answer accuracy, allocator memory, or production decode throughput was measured.

## Claim scope

On synthetic 32k-token attention traces with local, sink, semantic-reuse, and long-range needle components, a tiered KV retention policy with full recent tokens, full heavy hitters, and compressed old tokens preserved more retained attention mass than sliding-window and heavy-hitter-only baselines under equal full-KV-equivalent memory budgets.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic mechanism probe, not full validation of real transformer KV eviction.

## Recommended next action

Run a bounded real-model inference follow-up that implements sliding, heavy-hitter, and tiered KV policies in a small/medium long-context transformer and measures needle accuracy, logprob degradation, decode throughput, and actual memory pressure at 16k-32k context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 32k KV eviction quality and memory probe
- Success threshold: Tiered policy matches or exceeds heavy-hitter needle accuracy, improves long-document logprob/perplexity versus sliding by at least 20% of the gap to full cache, and reduces KV memory by at least 35% versus full 32k cache without more than 15% decode throughput loss.
- Stop condition: Stop if tiered loses more than 5 percentage points of needle accuracy versus heavy-hitter or shows worse logprob/perplexity than sliding at equal memory budget in two independent prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-eviction-for-32k-context-on-home-gb10-bdba28564130`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
