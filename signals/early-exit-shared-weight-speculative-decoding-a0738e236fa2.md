# Early-Exit Shared-Weight Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `early-exit-shared-weight-speculative-decoding-a0738e236fa2`
Run ID: `early-exit-shared-weight-speculative-decoding-a0738e236fa2-20260526T033011043199+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a28d37830bd4

## What looked useful

Shared-weight early exits can produce high distribution overlap, but this local probe suggests a tradeoff: making exits target-like can erase final-depth quality advantage, while preserving final-depth advantage lowers acceptance enough that estimated gains averaged only 1.06x under optimistic assumptions.

## Boundaries and scale limits

Toy recurrent character LM, 180k-character Tiny Shakespeare subset, simple layer-cost model, no transformer attention, no KV-cache, no tokenizer-scale vocabulary, and no wall-clock serving implementation.

## Claim scope

Bounded NumPy toy character-LM probe of shared recurrent weights with early exits: high early-exit acceptance appeared only when auxiliary exit training made the final target no better than early exits; when final depth was trained as the stronger target, estimated speculative speedup was marginal across three seeds.

## Why it stopped

Proxy early falsification rather than full validation: the strict final-depth-only control produced only marginal estimated speedup, and the superficially high-acceptance auxiliary-loss run did not retain a stronger final target.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete test is a tiny transformer self-speculative decoding implementation with real end-to-end latency and a success threshold above overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Wall-Clock Self-Speculative Early-Exit Test
- Success threshold: At least 1.20x measured end-to-end decoding speedup over final-depth decoding with no statistically meaningful target-distribution or validation-quality regression.
- Stop condition: Stop if final exit is not better than early exits, measured speedup is below 1.10x after overhead, or acceptance falls below the break-even threshold for the chosen draft depth and gamma.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-shared-weight-speculative-decoding-a0738e236fa2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
