# Speculative decoding on gb10 with exact no-speculation and n-gram baselines under bounded load

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-on-gb10-with-exact-no-speculation-and-n-gram-baselines-under-bounded-load-306ab084701c`
Run ID: `speculative-decoding-on-gb10-with-exact-no-speculation-and-n-gram-baselines-under-bounded-load-306ab084701c-20260611T102924653074+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/29ac784301c8

## What looked useful

Prompt lookup can be beneficial and exact for a narrow batch-1 GB10 case, but exactness depends on settings and the tested Transformers assisted backend does not support the bounded batch load needed for the broader claim.

## Boundaries and scale limits

Short fixed prompts, max 48 new tokens, three repeats, small 360M target model, Transformers generate backend only, no production request scheduler, no continuous batching, no larger 1B/7B-class model, and no real serving trace.

## Claim scope

On GB10 with PyTorch 2.12.0+cu130 and Transformers 4.57.6 using HuggingFaceTB/SmolLM2-360M as target and HuggingFaceTB/SmolLM2-135M as assistant, batch-1 prompt lookup with prompt_lookup_num_tokens=10 reached 2.03x exact-greedy throughput while matching greedy tokens on the benchmark prompts; assistant-model speculative decoding was slower at 0.70x, and assisted/prompt-lookup paths were unsupported for batch sizes 2 and 4 in this backend.

## Why it stopped

Mixed bounded evidence: prompt_lookup_10 was fast and exact only at batch size 1, assistant speculation was slower than exact greedy, and assisted decoding was unsupported for batch sizes 2 and 4 in the tested backend.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded test should use a backend or harness that can measure assisted decoding under request concurrency or continuous batching while preserving token-level exactness checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Request-concurrent prompt lookup and assistant speculation on GB10
- Success threshold: At least one assisted method must be token-exact versus greedy and improve median tokens/s by >=1.3x without worse p95 latency at a bounded concurrent load of at least 4 active requests.
- Stop condition: Stop if the backend cannot preserve greedy-token exactness, cannot exercise concurrent assisted requests, or assisted methods fail to beat exact greedy by 10% after warmup.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-on-gb10-with-exact-no-speculation-and-n-gram-baselines-under-bounded-load-3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
