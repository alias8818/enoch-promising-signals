# N-gram speculative decoding for CPU inference speedup

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-decoding-for-cpu-inference-speedup-c3374dbf5a0e`
Run ID: `n-gram-speculative-decoding-for-cpu-inference-speedup-c3374dbf5a0e-20260608T121129074383+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1d3749dd7343

## What looked useful

Corrected 18-run grid produced median projected speedup 1.7647x at 10% overhead and best 2.2966x; worst corrected config still projected 1.4306x at 10% overhead. Initial Alice results were discarded after detecting train/eval leakage from corpus repetition.

## Boundaries and scale limits

Trace/cost-model only; no transformer inference runtime, no production tokenizer, no measured CPU LLM tokens/sec, and only two public text corpora with train/eval splits up to 700k/220k bytes.

## Claim scope

A byte-level n-gram continuation cache trained on held-out-separated public text can accept enough drafted tokens to project CPU decoding speedups under explicit low-overhead verification cost assumptions.

## Why it stopped

The mechanism is supported by corrected trace evidence, but CPU inference speedup itself was only proxied rather than directly measured.

## Recommended next action

Stop as no-paper useful signal; next bounded action is direct CPU LLM runtime validation on a small quantized model with identical prompts and thread settings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM validation of n-gram speculative decoding
- Success threshold: Geometric mean tokens/sec improvement of at least 1.2x across at least 50 prompts, with exact greedy-output equivalence and measured overhead below the projected acceptance benefit.
- Stop condition: Stop if acceptance-adjusted throughput is below 1.05x or outputs diverge from greedy baseline on any deterministic prompt.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-cpu-inference-speedup-c3374dbf5a0e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
