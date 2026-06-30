# Per-Token Importance Scoring for Selective KV Eviction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-token-importance-scoring-for-selective-kv-eviction-03b938efa935`
Run ID: `per-token-importance-scoring-for-selective-kv-eviction-03b938efa935-20260604T002521305719+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45d77e07dfa2

## What looked useful

Per-token attention-importance is a useful retention signal under cache pressure, especially at budget 8, but raw importance is not sufficient as a standalone eviction rule; preserving prefix/sink tokens plus recency dominated in this bounded direct test.

## Boundaries and scale limits

Only distilgpt2, two short embedded texts, two cache budgets, no long-context benchmark, no serving throughput benchmark, no optimized scorer, no 7B+ model, and no corpus-scale robustness or confidence intervals.

## Claim scope

On a CPU-local distilgpt2 direct pruned-KV teacher-forced probe over 82 scored tokens, accumulated attention-received per-token importance reduced NLL degradation versus recent-only and random cache eviction at budgets 16 and 8, but a sink-plus-recent hybrid was substantially stronger.

## Why it stopped

No-paper closure: direct local evidence is useful but too small for publication-grade validation, and the strongest result favors a hybrid policy rather than raw per-token importance alone.

## Recommended next action

Run a bounded deepen follow-up on GPT-2-small-class evaluation with hundreds of held-out sequences, longer contexts, multiple budgets, confidence intervals, and ablations for sinks, recency, and attention-importance before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded GPT-2-small KV eviction ablation for attention-importance, sinks, and recency
- Success threshold: Sink-plus-recent-plus-importance improves excess NLL over recent-only by at least 25% and over sink-plus-recent by at least 5% at two or more budgets with non-overlapping paired confidence intervals, while adding less than 10% scoring overhead in the measured harness.
- Stop condition: Stop if sink-plus-recent-plus-importance fails to beat sink-plus-recent by at least 5% excess-NLL reduction at the first two tested budgets or if attention-output scoring overhead dominates any quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/per-token-importance-scoring-for-selective-kv-eviction-03b938efa935`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
