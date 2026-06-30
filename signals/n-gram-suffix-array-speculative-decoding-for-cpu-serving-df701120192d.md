# N-gram suffix-array speculative decoding for CPU serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-array-speculative-decoding-for-cpu-serving-df701120192d`
Run ID: `n-gram-suffix-array-speculative-decoding-for-cpu-serving-df701120192d-20260629T120109549083+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b2fd3306bddb

## What looked useful

Suffix-array drafting exploited repeated contexts and beat hash n-gram acceptance by small margins on repeated/local corpora, while the shuffled control collapsed. The data structure was 30x to 120x slower per lookup than hash n-grams in this bounded CPU probe, so the next useful test is a compiled/vectorized implementation before full serving integration.

## Boundaries and scale limits

No live LLM verifier, no production tokenizer, no end-to-end CPU serving stack, no large corpus, no compiled suffix-array/FM-index implementation, and no hardware cache profiling. Results are mechanism evidence only.

## Claim scope

On bounded <=18.3k-token corpora with regex tokenization and exact held-out replay, suffix-array n-gram drafting with context backoff slightly improves accepted tokens over a fixed hash n-gram baseline on repeated/local text, but lookup cost is tens of microseconds in Python and much slower than hash lookup.

## Why it stopped

Bounded proxy evidence is mixed: the repeated-context mechanism works, but the suffix-array approach is not compelling against a simpler hash n-gram baseline at current lookup cost and evidence depth.

## Recommended next action

Stop this run as no-paper useful evidence; if pursued, implement a compiled suffix-array/FM-index drafter and test it on real model token traces with a production tokenizer before any end-to-end serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compiled suffix-array drafter on real CPU token traces
- Success threshold: Suffix-array/FM-index achieves at least 10% relative accepted-token improvement over hash n-gram while keeping p95 lookup latency within 2x of hash lookup and preserving nonzero gains on real traces.
- Stop condition: Stop if compiled lookup p95 remains more than 2x hash lookup or acceptance gains stay below 10% relative on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-array-speculative-decoding-for-cpu-serving-df701120192d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
