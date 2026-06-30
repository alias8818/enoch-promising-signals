# KV-Cache Self-Speculative Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `kv-cache-self-speculative-decoding-without-draft-model-d47c4fda5973`
Run ID: `kv-cache-self-speculative-decoding-without-draft-model-d47c4fda5973-20260611T101841989615+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d95ce18e9046

## What looked useful

A KV-cache-only stale-repeat proposer is not promising for practical acceleration: realistic-context top-1 persistence is too low to clear a 1.25x optimistic speedup threshold, even before implementation overhead. High apparent speedups from greedy traces are explained by degenerate repeated-token/newline loops.

## Boundaries and scale limits

Tested on CPU with sshleifer/tiny-gpt2, distilgpt2, and EleutherAI/pythia-14m. The strongest negative evidence is a teacher-forced proxy over 2409-2410 real-text positions per model, not a full GPU serving implementation, not 1B+ models, and not sampling-preserving speculative decoding.

## Claim scope

For stale-KV no-draft self-speculation that repeats the current target-model top-1 token as a future block, small cached GPT-style models show useful acceptance only in degenerate greedy repetition loops; on teacher-forced real text contexts the optimistic model-call speedup is only about 1.05x to 1.09x.

## Why it stopped

Early falsification by bounded proxy and small direct traces: the direct greedy traces were dominated by degenerate repetition, while the non-degenerate teacher-forced proxy showed only 1.05x to 1.09x optimistic speedup, below the predeclared useful threshold.

## Recommended next action

Stop pursuing stale-repeat KV-cache self-speculation as a standalone acceleration method; only revisit the direction with a genuinely cheaper same-model proposal mechanism and require at least 1.25x wall-clock speedup on non-degenerate outputs.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-self-speculative-decoding-without-draft-model-d47c4fda5973`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
