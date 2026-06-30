# Suffix-Tree Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-gb10-9000f2099c7d`
Run ID: `suffix-tree-speculative-decoding-on-gb10-9000f2099c7d-20260620T094333743143+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/198a2f451250

## What looked useful

Corrected controls show uniform random traces stay at 1.0x, while copy-burst traces reach about 2.07x idealized call speedup at draft 16 and periodic traces reach about 15.06x. Repeated prompt text reaches about 1.92x and saturates by draft 16 to 32. A CUDA distilgpt2 trace reached 7.89x only because the model output collapsed into repeated newlines, so it should be treated as a degeneracy diagnostic.

## Boundaries and scale limits

Tested 1K to 8K token traces, synthetic controls, repeated local prompt text, and one small CUDA distilgpt2 greedy trace that degenerated into newline repetition. No real verifier kernel, KV-cache timing, quality-preserving sampled decoding, broad prompt set, or larger model serving benchmark was run.

## Claim scope

An online suffix-context draft index can reduce idealized target verification calls on repeated ordered traces on GB10-local experiments, but the gain is strongly trace-dependent and not established as an end-to-end LLM serving speedup.

## Why it stopped

This is a no-paper useful-signal result: the mechanism works on repeated traces but the evidence is proxy/accounting-heavy and the only direct model trace was degenerate, so broad serving claims are not validated.

## Recommended next action

Run a bounded real-verifier benchmark on a small causal LM with non-degenerate prompts, measuring wall-clock tokens/s, accepted-token histograms, and output equivalence against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-verifier suffix-draft benchmark for non-degenerate small-LM prompts
- Success threshold: At least 1.2x measured wall-clock tokens/s improvement on a predeclared repetitive-prompt subset with exact greedy-output equivalence and no regression beyond 5% on low-repetition prompts when gated by acceptance diagnostics.
- Stop condition: Stop if measured wall-clock throughput is below 1.05x on repetitive prompts, if verifier overhead erases call-count savings, or if greedy outputs diverge from the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-gb10-9000f2099c7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
