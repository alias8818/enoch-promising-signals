# Identity-biased KV trace gates with measured skip savings

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `identity-biased-kv-trace-gates-with-measured-skip-savings-19e057074e`
Run ID: `identity-biased-kv-trace-gates-with-measured-skip-savings-19e057074e-20260519T163046599492+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Identity-biased KV trace gates with measured skip savings: internal_generated:identity-biased-kv-trace-gates-with-measured-skip-savings-19e057074e

## What looked useful

Identity traces beat random controls under high identity bias and retain dense-attention outputs with large KV evaluation skips, but recency is a much stronger baseline and was equal or better in most natural-text and moderate-bias settings. Identity-only gating needs actual-head evidence before paper claims.

## Boundaries and scale limits

No trained transformer weights, perplexity/task accuracy, autoregressive generation, fused GPU kernel, or end-to-end serving latency were tested. Runtime savings are score-count savings only; the Python gate path was slower than dense attention because selection was unfused.

## Claim scope

Bounded NumPy causal-attention trace validation over natural byte-token text and controlled recurrence traces shows identity-biased KV gates can skip 49.87% to 93.51% of KV score evaluations and preserve dense outputs under strong identity-biased attention, but they do not consistently beat a same-budget recency baseline.

## Why it stopped

Bounded direct trace validation found large score-count skip savings but failed the decisive same-budget recency control; this is not full LLM validation and is not paper-ready.

## Recommended next action

Stop this standalone identity-gate claim; the next bounded test should use actual small-transformer attention traces and only continue if identity-plus-recency beats recency-only by at least 0.02 output cosine or preserves perplexity at the same KV budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual-head identity-plus-recency KV gating on GPT-2-small attention traces
- Success threshold: At 12.5% KV budget, identity-plus-recency must improve mean output cosine by at least 0.02 over recency-only or reduce validation loss delta by at least 10% relative to recency-only while preserving at least 85% score-count skips.
- Stop condition: Stop if identity-plus-recency is within +/-0.005 output cosine of recency-only on actual attention traces or worsens validation loss at matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/identity-biased-kv-trace-gates-with-measured-skip-savings-19e057074e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
