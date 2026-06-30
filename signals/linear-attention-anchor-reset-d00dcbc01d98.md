# Linear Attention Anchor Reset

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `linear-attention-anchor-reset-d00dcbc01d98`
Run ID: `linear-attention-anchor-reset-d00dcbc01d98-20260604T142711813563+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c108e0d23655

## What looked useful

Oracle segment resets improved local-remap accuracy from 0.0276 to 0.1127 and reduced contamination from 0.946 to 0.000 over 40 seeds, while exact resets harmed cross-segment retrieval accuracy to 0.0163 with NLL 12.36.

## Boundaries and scale limits

No training, no learned reset gate, no language modeling, no softmax-attention baseline, and no full-scale long-context benchmark; evidence is limited to deterministic synthetic inference on GB10.

## Claim scope

Synthetic recurrent linear-attention key-value retrieval with explicit segment boundaries: accumulator resets reduce stale state and improve current-segment remapping, but can erase needed cross-boundary memory.

## Why it stopped

Proxy-only mixed result: the mechanism helps boundary-local remapping but fails when memory must persist across the reset boundary.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a trained toy linear-attention model with a learned reset gate and explicit no-reset/decay controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Reset Gate for Toy Linear Attention
- Success threshold: Learned reset improves local-remap validation accuracy by at least 2x over no-reset and keeps cross-segment accuracy within 10 percent relative of the best non-oracle persistence baseline across at least three seeds.
- Stop condition: Stop if learned reset does not beat no-reset on local-remap after a short trained toy run, or if it improves local-remap only by destroying cross-segment memory.

## Evidence references

- Artifact root: `<local-path>/projects/linear-attention-anchor-reset-d00dcbc01d98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
