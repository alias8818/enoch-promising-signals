# Compare Attention-Sink Retention Against Heavy-Hitter KV Eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compare-attention-sink-retention-against-heavy-hitter-kv-e-82a0b2cf5d`
Run ID: `compare-attention-sink-retention-against-heavy-hitter-kv-e-82a0b2cf5d-20260602T164000940663+0000`

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

- Parent run decision: Attention-Sink Bounded KV Eviction: enoch://control-plane/projects/attention-sink-bounded-kv-eviction-808f27a739ff/runs/attention-sink-bounded-kv-eviction-808f27a739ff-20260602T121813606155+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/250464260a3e

## What looked useful

Heavy-hitter retention beat attention-sink retention on mean NLL at all tested budgets: sink-minus-heavy-hitter mean NLL was 0.226 at budget 64, 0.389 at budget 128, and 0.275 at budget 192, with positive paired bootstrap 95% intervals. Sink retention still beat recent-only strongly, so sinks remain useful, but they were not competitive with heavy-hitter selection in this controlled comparison.

## Boundaries and scale limits

Small direct Tier 1 inference test only: 8 chunks, 224 target-token comparisons per budget, distilgpt2, sequence length 384, no true online KV-cache maintenance, no larger models, no long-context task benchmark, and no serving latency measurement.

## Claim scope

On distilgpt2 with WikiText-2 validation chunks, retained-subset scoring, preserved original position ids, and equal budgets of 64, 128, and 192 tokens, cumulative-attention heavy-hitter retention has lower mean next-token NLL than attention-sink plus recent-window retention.

## Why it stopped

Tier 1 controlled direct test produced a useful no-paper signal; it is not paper-positive because the retained cache is approximated by recomputing retained subsets and the evaluation is small.

## Recommended next action

Run a true online KV-cache eviction follow-up that maintains layerwise cached K/V tensors while comparing sink+recent against H2O-style heavy-hitter+recent on GPT-2-small-class models and longer contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online KV-Cache Sink-vs-Heavy-Hitter Retention on GPT-2-Small-Class Long Contexts
- Success threshold: Heavy-hitter plus recent achieves mean NLL at least 0.15 lower than sink plus recent at two or more cache budgets, with paired bootstrap 95% intervals above zero and no more than 25% slower scoring latency.
- Stop condition: Stop if online heavy-hitter fails to beat sink by 0.15 mean NLL at two budgets, if the bootstrap intervals include zero for all budgets, or if the implementation overhead exceeds 25% latency without a compensating quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/compare-attention-sink-retention-against-heavy-hitter-kv-e-82a0b2cf5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
