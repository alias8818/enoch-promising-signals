# CPU-Optimized Sliding Window KV Cache with Importance Retention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-optimized-sliding-window-kv-cache-with-importance-retention-8bae63a8fba3`
Run ID: `cpu-optimized-sliding-window-kv-cache-with-importance-retention-8bae63a8fba3-20260525T092103052737+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/be15fec6b4ab

## What looked useful

Across 12 grid configurations with strong synthetic importance, sliding top-1 retrieval accuracy was 0.000 mean, random-old was 0.059 mean, and importance retention was 0.623 mean. Periodic importance refresh averaged 0.846x same-size sliding-cache throughput and 6.60x full-context throughput. Sensitivity showed the method collapses toward random retention when importance signal is absent or weak.

## Boundaries and scale limits

No real transformer inference, no real attention-derived importance, no language-model perplexity or downstream long-context benchmark, and no datacenter-scale validation. Sequence lengths were 2048 to 8192 with dim 64 synthetic KV arrays and 384 queries per configuration.

## Claim scope

Synthetic CPU benchmark only: recent-window KV cache plus top-scored old-token retention improves old-anchor retrieval over pure sliding and random-old controls when importance scores are informative.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal but not direct model evidence; it should not be treated as full validation.

## Recommended next action

Run a bounded direct follow-up by integrating periodic importance retention into a small CPU transformer decoding path and evaluating attention-derived importance on long-context retrieval accuracy plus latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU Transformer Decode Test for Attention-Derived Importance Retention
- Success threshold: At least +20 percentage points retrieval accuracy over pure sliding at equal or lower KV capacity, with latency no worse than 1.5x same-size sliding cache and a clear advantage over random-old retention.
- Stop condition: Stop if model-derived importance does not beat random-old retention by at least 10 percentage points or if periodic refresh exceeds 2x same-size sliding latency on the target CPU setup.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-optimized-sliding-window-kv-cache-with-importance-retention-8bae63a8fba3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
