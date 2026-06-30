# End-to-end GPT-2-small KV-cache pruning with layer/head position-aware selectors

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `end-to-end-gpt-2-small-kv-cache-pruning-with-layer-head-po-afef6eff63`
Run ID: `end-to-end-gpt-2-small-kv-cache-pruning-with-layer-head-po-afef6eff63-20260523T135335160128+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Position-aware residual selectors for KV outlier prediction: enoch://control-plane/projects/position-aware-residual-selectors-for-kv-outlier-predictio-023629249e/runs/position-aware-residual-selectors-for-kv-outlier-predictio-023629249e-20260523T132735004937+0000
- Parent run decision: Layer/head-specific position-aware KV outlier selectors on real text traces: enoch://control-plane/projects/layer-head-specific-position-aware-kv-outlier-selectors-on-b6f05de403/runs/layer-head-specific-position-aware-kv-outlier-selectors-on-b6f05de403-20260523T134334492652+0000

## What looked useful

The selector produced consistent quality gains at tight budgets: at 29% average KV fraction, LHPA mean dense-relative NLL delta was 0.796 vs 0.894 random and 0.921 sink+recent; at 46% KV, LHPA delta was 0.337 vs 0.388 random and 0.492 sink+recent. At 70% KV, random was slightly better than LHPA, and LHPA was slower than dense because of attention-output and Python selection overhead.

## Boundaries and scale limits

Validation is limited to GPT-2 small, WikiText-2 test text, 3 seeds, 24 chunks per seed/budget, sequence length 384, and logical per-layer KV pruning. The implementation is head-aware in scoring but not true variable-length per-head storage, and it does not demonstrate serving speedup.

## Claim scope

On GPT-2 small autoregressive WikiText-2 windows of length 384, a layer/head attention-history position selector modestly improves next-token NLL over recency, sink+recent, and random retained-position controls at aggressive 32/64-token cache budgets, but not over random at the 128-token budget.

## Why it stopped

Moderate direct evidence supports a bounded mechanism at aggressive budgets, but the effect is mixed, not robust against random at larger budget, and lacks end-to-end speed or true per-head storage evidence required for paper-readiness.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; do not recommend another chained follow-up under the controller cap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-gpt-2-small-kv-cache-pruning-with-layer-head-po-afef6eff63`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
