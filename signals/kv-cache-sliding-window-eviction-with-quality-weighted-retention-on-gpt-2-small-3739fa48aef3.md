# KV-Cache Sliding-Window Eviction with Quality-Weighted Retention on GPT-2-Small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-sliding-window-eviction-with-quality-weighted-retention-on-gpt-2-small-3739fa48aef3`
Run ID: `kv-cache-sliding-window-eviction-with-quality-weighted-retention-on-gpt-2-small-3739fa48aef3-20260612T224834941193+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e67206aaa6d

## What looked useful

Attention-derived quality weighting produced much lower NLL than sliding-window retention: quality minus sliding was -5.232 NLL at budget 32 and -4.398 NLL at budget 64; quality also beat random older-token retention by -3.895 and -1.628 NLL respectively. Incremental full-cache scoring matched direct teacher-forced scoring within about 1e-5 on sanity checks.

## Boundaries and scale limits

Single model, one dataset split, 32 samples, short 160-token windows, two budgets, one attention-mass quality heuristic, no serving throughput benchmark, no long-context workload, no larger models, and no production cache implementation.

## Claim scope

On a bounded GPT-2-small inference probe over 32 WikiText-2 validation samples with 128-token prefixes and 32-token continuations, a cache policy that keeps a 16-token recent window plus high-attention older tokens outperformed same-budget pure sliding-window and random older-token controls on next-token NLL at budgets 32 and 64.

## Why it stopped

No-paper closure: this run produced a useful bounded mechanism signal, but the evidence is too narrow and implementation-prototype-specific for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with more samples, additional cache budgets/recent-window ratios, and a production-compatible cache object implementation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robustness sweep for attention-quality KV retention on GPT-2-small
- Success threshold: Quality retention improves mean continuation NLL over sliding by at least 0.25 at three or more budgets and beats random older-token retention at two or more budgets, with paired evidence and no scoring sanity failures.
- Stop condition: Stop if quality retention fails to beat random older-token retention at most budgets, if the effect vanishes under production-compatible cache handling, or if quality computation overhead dominates the practical cache-size benefit.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-sliding-window-eviction-with-quality-weighted-retention-on-gpt-2-small-3739fa48aef3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
